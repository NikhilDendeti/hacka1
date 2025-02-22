from django.core.management.base import BaseCommand
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from groq import Groq
import logging
from llama_index.core.tools import FunctionTool

# Configure logging
logging.basicConfig(level=logging.INFO)

# Set API Key Directly
GROQ_API_KEY = "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"

# Initialize Groq Client with API Key
client = Groq(api_key=GROQ_API_KEY)

# --- Register Functions as Tools ---
def rephrase_text_tool(text: str, difficulty_level: str = "simple"):
    completion = client.chat.completions.create(
        model="deepseek-r1-distill-llama-70b",
        messages=[{"role": "system", "content": f"Rephrase this text to be {difficulty_level}: {text}"}],
        temperature=0.6,
        max_completion_tokens=4096,
        top_p=0.95,
        stream=False,
        stop=None,
    )
    return completion.choices[0].message.content.strip()

def pronounce_word_tool(word: str):
    completion = client.chat.completions.create(
        model="deepseek-r1-distill-llama-70b",
        messages=[{"role": "system", "content": f"Provide phonetic spelling and pronunciation tips for: {word}"}],
        temperature=0.6,
        max_completion_tokens=4096,
        top_p=0.95,
        stream=False,
        stop=None,
    )
    return completion.choices[0].message.content.strip()

def health_query_tool(question: str):
    completion = client.chat.completions.create(
        model="deepseek-r1-distill-llama-70b",
        messages=[{"role": "system", "content": f"Answer this health-related question: {question}"}],
        temperature=0.6,
        max_completion_tokens=4096,
        top_p=0.95,
        stream=False,
        stop=None,
    )
    return completion.choices[0].message.content.strip()

# Register functions as tools
rephrase_text_tool = FunctionTool.from_defaults(rephrase_text_tool)
pronounce_word_tool = FunctionTool.from_defaults(pronounce_word_tool)
health_query_tool = FunctionTool.from_defaults(health_query_tool)

# --- Categorize User Query Using DeepSeek Model ---
def categorize_query(query: str):
    completion = client.chat.completions.create(
        model="deepseek-r1-distill-llama-70b",
        messages=[{"role": "system", "content": f"Categorize the following query into one of these categories: [rephrase, pronunciation, health_query] and return only the category name: {query}"}],
        temperature=0.3,
        max_completion_tokens=10,
        top_p=0.9,
        stream=False,
        stop=None,
    )
    return completion.choices[0].message.content.strip().lower()

# --- Process and Categorize User Query ---
def categorize_and_respond(query: str):
    category = categorize_query(query)
    return {"category": category}

# --- Django Views ---
@csrf_exempt
def process_query(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            query = data.get("query", "")
            return JsonResponse(categorize_and_respond(query))
        except Exception as e:
            logging.error(f"Error in processing query: {str(e)}")
            return JsonResponse({"error": "Query processing failed"}, status=500)
    return JsonResponse({"error": "Invalid request"}, status=400)

def root(request):
    return JsonResponse({"message": "Welcome to the AI Learning Assistant API"})

# --- Django Management Command for Running Chatbot ---
class Command(BaseCommand):
    help = "Run the chatbot AI assistant"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Chatbot is running. Type 'exit' to stop."))

        while True:
            user_input = input("User: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Exiting chatbot.")
                break

            response = categorize_and_respond(user_input)
            print(f"Chatbot Category: {response['category']}")

# --- Default Questions for Testing ---
def default_questions():
    return {
        "rephrase": "Can you simplify this sentence: 'The cataclysmic event resulted in widespread devastation'?",
        "pronunciation": "How do you pronounce 'photosynthesis'?",
        "health_query": "What are the symptoms of dehydration?"
    }