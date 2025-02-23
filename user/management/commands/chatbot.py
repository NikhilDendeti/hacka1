from django.core.management.base import BaseCommand
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from groq import Groq
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Set your Groq API key securely
GROQ_API_KEY = "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"

# Initialize Groq Client
client = Groq(api_key=GROQ_API_KEY)

# --- AI Functionalities ---
def rephrase_text(text: str, difficulty_level: str = "simple"):
    prompt = f"Rephrase the following text to {difficulty_level} language: {text}"
    return query_llama(prompt)

def pronounce_word(word: str):
    prompt = f"Provide phonetic spelling and pronunciation tips for the word '{word}'."
    return query_llama(prompt)

def health_query(question: str):
    prompt = f"Answer the health-related question: '{question}'. Be concise and clear."
    return query_llama(prompt)

# --- Core AI Query Function ---
def query_llama(prompt: str):
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "system", "content": prompt}],
        temperature=0.5,
        max_completion_tokens=2048,
        top_p=0.9,
        stream=False,
        stop=None,
    )
    return completion.choices[0].message.content.strip()

# --- Categorize User Query ---
def categorize_query(query: str):
    prompt = (
        f"Categorize the following query strictly into one of these categories: "
        f"[rephrase, pronunciation, health_query]. Return only the category name. Query: '{query}'"
    )
    category = query_llama(prompt).lower()
    if category in ['rephrase', 'pronunciation', 'health_query']:
        return category
    else:
        return 'unknown'

# --- Categorize and Respond ---
def categorize_and_respond(query: str):
    category = categorize_query(query)
    if category == "rephrase":
        response = rephrase_text(query)
    elif category == "pronunciation":
        response = pronounce_word(query)
    elif category == "health_query":
        response = health_query(query)
    else:
        response = "Sorry, I couldn't categorize your request. Please clarify."

    return {"category": category, "response": response}

# --- Django Views ---
@csrf_exempt
def process_query(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            query = data.get("query", "")
            return JsonResponse(categorize_and_respond(query))
        except Exception as e:
            logging.error(f"Error processing query: {str(e)}")
            return JsonResponse({"error": "Query processing failed."}, status=500)
    return JsonResponse({"error": "Invalid request."}, status=400)

def root(request):
    return JsonResponse({"message": "Welcome to the AI Learning Assistant API"})

# --- Django Management Command for Running Chatbot ---
class Command(BaseCommand):
    help = "Run the AI-powered chatbot interactively"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Chatbot is running. Type 'exit' to stop."))

        while True:
            user_input = input("User: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Exiting chatbot.")
                break

            response_data = categorize_and_respond(user_input)
            print(f"Chatbot ({response_data['category']}): {response_data['response']}")

# --- Default Test Questions ---
def default_questions():
    return {
        "rephrase": "Can you simplify this sentence: 'The cataclysmic event resulted in widespread devastation'?",
        "pronunciation": "How do you pronounce 'photosynthesis'?",
        "health_query": "What are the symptoms of dehydration?"
    }
