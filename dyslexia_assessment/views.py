from django.shortcuts import render
from dyslexia_assessment.utils import get_random_question_set, analyze_dyslexia_test
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from dyslexia_assessment.models import DyslexiaTestResult

@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def dyslexia_test(request):
    try:
        data = request.data
        if not data:
            return Response({"error": "No data provided"}, status=400)

        # Analyze the test results using AI processing function
        results = analyze_dyslexia_test(data)

        # Save results to the database
        test_result = DyslexiaTestResult.objects.create(
            user=request.user,  # Store user ID
            word_confusion_score=results["word_confusion_score"],
            reading_speed=results["reading_speed"],
            letter_confusion_score=results["letter_confusion_score"],
            final_severity_score=results["final_severity_score"],
            severity=results["severity"]
        )

        return Response({
            "message": "Test result saved successfully.",
            "test_id": test_result.id,  # Return the test ID for reference
            **results  
        }, status=201)

    except Exception as e:
        return Response({"error": str(e)}, status=500)
    

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_questions(request):
    """API to return a random set of dyslexia test questions."""
    questions = get_random_question_set()
    return Response({"questions": questions})
