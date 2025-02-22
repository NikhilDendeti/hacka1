import json
import os
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from random import sample
from .models import UserGameResult, GameLevel
from .utils import calculate_score, get_next_level


# Load JSON File Dynamically
def load_questions():
    """Load questions from JSON file"""
    json_path = os.path.join(settings.BASE_DIR, "game/questions.json")
    with open(json_path, "r") as file:
        return json.load(file)

@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_gamified_questions(request):
    """
    Fetch game questions based on the user's level and severity from JSON.
    """
    user = request.user

    # Assume user has an attribute for severity & level stored
    user_severity = request.GET.get("severity", "mild")  # Default to "mild"
    user_level = request.GET.get("level", "level1")  # Default to "level1"

    # Load questions from JSON
    questions_data = load_questions()

    # Validate Severity and Level
    if user_severity not in questions_data["Word Scramble Master"]:
        return Response({"error": "Invalid severity level"}, status=400)

    if user_level not in questions_data["Word Scramble Master"][user_severity]:
        return Response({"error": "Invalid game level"}, status=400)

    # Get the questions for the requested level
    questions = questions_data["Word Scramble Master"][user_severity][user_level]

    if not questions:
        return Response({"error": "No questions found"}, status=404)

    # Return only a random set of 5 questions to avoid repetition
    question_data = sample(questions, min(5, len(questions)))

    return Response({"questions": question_data}, status=200)

@api_view(["POST"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_score(request):
    """Stores game results and checks if user qualifies for next level"""
    user = request.user
    correct_answers = request.data.get("correct_answers", 0)
    total_questions = request.data.get("total_questions", 1)  # Avoid division by zero
    current_level = request.data.get("level", "mild_level1")  # Default level

    # Calculate the user's score
    score = calculate_score(correct_answers, total_questions)

    # Get or create the user's game progress
    level_instance, _ = GameLevel.objects.get_or_create(name=current_level)
    game_result, created = UserGameResult.objects.get_or_create(user=user, level=level_instance)

    # Update user score & attempts
    game_result.score = score
    game_result.attempts += 1

    # Check if the user qualifies for the next level
    if score >= 70:
        next_level = get_next_level(current_level)
        if next_level:
            # Ensure the next level exists before assigning
            next_level_instance, _ = GameLevel.objects.get_or_create(name=next_level)
            game_result.unlocked_next = True
            UserGameResult.objects.get_or_create(user=user, level=next_level_instance)
        else:
            game_result.unlocked_next = False  

    game_result.save()

    return Response({
        "score": score,
        "current_level": current_level,
        "unlocked_next": game_result.unlocked_next,
        "next_level": next_level if score >= 70 else "Retry the same level"
    }, status=200)

@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_levels_status(request):
    """Fetch the levels unlocked and progress of a user"""
    user = request.user
    game_results = UserGameResult.objects.filter(user=user).values("level__name", "score", "attempts", "unlocked_next")

    return Response({"progress": list(game_results)}, status=200)
