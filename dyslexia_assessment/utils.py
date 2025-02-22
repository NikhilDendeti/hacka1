import random

def analyze_dyslexia_test(data):
    # Extract user-provided test data with default values
    word_confusion_errors = int(data.get("word_confusion_errors", 0))
    reading_time = float(data.get("reading_time", 0))
    letter_confusion_errors = int(data.get("letter_confusion_errors", 0))

    # Ensure values are non-negative
    word_confusion_errors = max(0, word_confusion_errors)
    reading_time = max(0, reading_time)
    letter_confusion_errors = max(0, letter_confusion_errors)

    # 1️⃣ **Calculate Word Recognition Score**
    word_confusion_score = max(0, 100 - (word_confusion_errors * 10))

    # 2️⃣ **Calculate Reading Speed Score**
    reading_speed = max(20, 250 - reading_time)

    # 3️⃣ **Calculate Letter Confusion Score**
    letter_confusion_score = max(0, 100 - (letter_confusion_errors * 15))

    # 4️⃣ **Final Severity Score (Weighted Calculation)**
    severity_score = (word_confusion_score * 0.3) + (reading_speed * 0.3) + (letter_confusion_score * 0.4)

    # 5️⃣ **Determine Severity Level**
    if severity_score < 40:
        severity = "Severe"
    elif severity_score < 70:
        severity = "Moderate"
    else:
        severity = "Mild"

    return {
        "word_confusion_score": word_confusion_score,
        "reading_speed": reading_speed,
        "letter_confusion_score": letter_confusion_score,
        "final_severity_score": severity_score,
        "severity": severity
    }





# Define 10 sets of 10 questions each
QUESTION_SETS = [
    {
        "id": 1,
        "questions": [
            {"type": "word_confusion", "question": "Which word is correct?", "options": ["Beleive", "Believe"], "answer": "Believe"},
            {"type": "word_confusion", "question": "Choose the right word:", "options": ["Their", "Thier"], "answer": "Their"},
            {"type": "reading_comprehension", "passage": "The sun sets in the west.", "question": "Where does the sun set?", "options": ["East", "West"], "answer": "West"},
            {"type": "letter_confusion", "question": "Identify the correct letter:", "options": ["b", "d"], "answer": "b"},
            {"type": "word_confusion", "question": "Which is correct?", "options": ["Affect", "Effect"], "answer": "Effect"},
            {"type": "reading_comprehension", "passage": "Dogs are loyal animals.", "question": "Which animal is known for loyalty?", "options": ["Cats", "Dogs"], "answer": "Dogs"},
            {"type": "word_confusion", "question": "Select the correct spelling:", "options": ["Recieve", "Receive"], "answer": "Receive"},
            {"type": "reading_comprehension", "passage": "A car has four wheels.", "question": "How many wheels does a car have?", "options": ["Two", "Four"], "answer": "Four"},
            {"type": "letter_confusion", "question": "Identify the letter:", "options": ["p", "q"], "answer": "p"},
            {"type": "letter_confusion", "question": "Select the correct option:", "options": ["b", "d"], "answer": "b"}
        ]
    },
    {
        "id": 2,
        "questions": [
            {"type": "word_confusion", "question": "Choose the right word:", "options": ["Accept", "Except"], "answer": "Accept"},
            {"type": "reading_comprehension", "passage": "Fish live in water.", "question": "Where do fish live?", "options": ["Land", "Water"], "answer": "Water"},
            {"type": "word_confusion", "question": "Select the correct spelling:", "options": ["Definately", "Definitely"], "answer": "Definitely"},
            {"type": "letter_confusion", "question": "Identify the correct letter:", "options": ["q", "p"], "answer": "q"},
            {"type": "word_confusion", "question": "Which is correct?", "options": ["Its", "It's"], "answer": "It's"},
            {"type": "reading_comprehension", "passage": "Birds have feathers.", "question": "What do birds have?", "options": ["Fur", "Feathers"], "answer": "Feathers"},
            {"type": "word_confusion", "question": "Choose the correct word:", "options": ["Lose", "Loose"], "answer": "Lose"},
            {"type": "reading_comprehension", "passage": "A bike has two wheels.", "question": "How many wheels does a bike have?", "options": ["Two", "Four"], "answer": "Two"},
            {"type": "letter_confusion", "question": "Identify the letter:", "options": ["q", "p"], "answer": "q"},
            {"type": "letter_confusion", "question": "Select the correct option:", "options": ["d", "b"], "answer": "d"}
        ]
    },
    {
        "id": 3,
        "questions": [
            {"type": "word_confusion", "question": "Choose the correct word:", "options": ["Brake", "Break"], "answer": "Brake"},
            {"type": "word_confusion", "question": "Select the right word:", "options": ["Bare", "Bear"], "answer": "Bear"},
            {"type": "reading_comprehension", "passage": "The Earth revolves around the Sun.", "question": "What does the Earth revolve around?", "options": ["Moon", "Sun"], "answer": "Sun"},
            {"type": "letter_confusion", "question": "Identify the correct letter:", "options": ["p", "q"], "answer": "p"},
            {"type": "word_confusion", "question": "Which is correct?", "options": ["Peace", "Piece"], "answer": "Piece"},
            {"type": "reading_comprehension", "passage": "The heart pumps blood.", "question": "What does the heart do?", "options": ["Pump air", "Pump blood"], "answer": "Pump blood"},
            {"type": "word_confusion", "question": "Which is correct?", "options": ["Stationery", "Stationary"], "answer": "Stationery"},
            {"type": "reading_comprehension", "passage": "The moon reflects sunlight.", "question": "What does the moon reflect?", "options": ["Sunlight", "Starlight"], "answer": "Sunlight"},
            {"type": "letter_confusion", "question": "Identify the letter:", "options": ["p", "q"], "answer": "p"},
            {"type": "letter_confusion", "question": "Select the correct option:", "options": ["b", "d"], "answer": "b"}
        ]
    },
     {
        "id": 4,
        "questions": [
            {"type": "word_confusion", "question": "Which word is correct?", "options": ["Principal", "Principle"], "answer": "Principal"},
            {"type": "word_confusion", "question": "Choose the right word:", "options": ["Capital", "Capitol"], "answer": "Capital"},
            {"type": "reading_comprehension", "passage": "The stars shine at night.", "question": "When do the stars shine?", "options": ["Day", "Night"], "answer": "Night"},
            {"type": "letter_confusion", "question": "Identify the correct letter:", "options": ["m", "n"], "answer": "m"},
            {"type": "word_confusion", "question": "Which is correct?", "options": ["Than", "Then"], "answer": "Then"},
            {"type": "reading_comprehension", "passage": "Water is essential for life.", "question": "What is essential for life?", "options": ["Water", "Fire"], "answer": "Water"},
            {"type": "word_confusion", "question": "Which is correct?", "options": ["Elicit", "Illicit"], "answer": "Elicit"},
            {"type": "reading_comprehension", "passage": "Cows produce milk.", "question": "What do cows produce?", "options": ["Eggs", "Milk"], "answer": "Milk"},
            {"type": "letter_confusion", "question": "Identify the letter:", "options": ["g", "q"], "answer": "g"},
            {"type": "letter_confusion", "question": "Select the correct option:", "options": ["d", "b"], "answer": "d"}
        ]
    },
    {
        "id": 5,
        "questions": [
            {"type": "word_confusion", "question": "Choose the correct word:", "options": ["To", "Too"], "answer": "Too"},
            {"type": "word_confusion", "question": "Select the right word:", "options": ["Allusion", "Illusion"], "answer": "Allusion"},
            {"type": "reading_comprehension", "passage": "A train runs on tracks.", "question": "What does a train run on?", "options": ["Tracks", "Road"], "answer": "Tracks"},
            {"type": "letter_confusion", "question": "Identify the correct letter:", "options": ["m", "n"], "answer": "m"},
            {"type": "word_confusion", "question": "Which is correct?", "options": ["Weather", "Whether"], "answer": "Weather"},
            {"type": "reading_comprehension", "passage": "Frogs live in ponds.", "question": "Where do frogs live?", "options": ["Desert", "Pond"], "answer": "Pond"},
            {"type": "word_confusion", "question": "Which is correct?", "options": ["Canvas", "Canvass"], "answer": "Canvas"},
            {"type": "reading_comprehension", "passage": "A guitar has strings.", "question": "What does a guitar have?", "options": ["Keys", "Strings"], "answer": "Strings"},
            {"type": "letter_confusion", "question": "Identify the letter:", "options": ["p", "q"], "answer": "p"},
            {"type": "letter_confusion", "question": "Select the correct option:", "options": ["b", "d"], "answer": "b"}
        ]
    },
    {
        "id": 6,
        "questions": [
            {"type": "word_confusion", "question": "Which word is correct?", "options": ["Complement", "Compliment"], "answer": "Complement"},
            {"type": "word_confusion", "question": "Choose the right word:", "options": ["Assent", "Ascent"], "answer": "Ascent"},
            {"type": "reading_comprehension", "passage": "The elephant is the largest land animal.", "question": "What is the largest land animal?", "options": ["Elephant", "Tiger"], "answer": "Elephant"},
            {"type": "letter_confusion", "question": "Identify the correct letter:", "options": ["b", "d"], "answer": "b"},
            {"type": "word_confusion", "question": "Which is correct?", "options": ["Medal", "Meddle"], "answer": "Medal"},
            {"type": "reading_comprehension", "passage": "The sun rises in the east.", "question": "Where does the sun rise?", "options": ["West", "East"], "answer": "East"},
            {"type": "word_confusion", "question": "Which is correct?", "options": ["Course", "Coarse"], "answer": "Course"},
            {"type": "reading_comprehension", "passage": "Apples grow on trees.", "question": "Where do apples grow?", "options": ["Ground", "Trees"], "answer": "Trees"},
            {"type": "letter_confusion", "question": "Identify the letter:", "options": ["p", "q"], "answer": "p"},
            {"type": "letter_confusion", "question": "Select the correct option:", "options": ["b", "d"], "answer": "b"}
        ]
    },
    {
        "id": 7,
        "questions": [
            {"type": "word_confusion", "question": "Which word is correct?", "options": ["Naval", "Navel"], "answer": "Naval"},
            {"type": "word_confusion", "question": "Choose the right word:", "options": ["Fewer", "Less"], "answer": "Fewer"},
            {"type": "reading_comprehension", "passage": "Turtles live for a long time.", "question": "What animal lives a long time?", "options": ["Dog", "Turtle"], "answer": "Turtle"},
            {"type": "letter_confusion", "question": "Identify the correct letter:", "options": ["m", "n"], "answer": "m"},
            {"type": "word_confusion", "question": "Which is correct?", "options": ["Patience", "Patients"], "answer": "Patience"},
            {"type": "reading_comprehension", "passage": "Roses are red, violets are blue.", "question": "What color are roses?", "options": ["Yellow", "Red"], "answer": "Red"},
            {"type": "word_confusion", "question": "Which is correct?", "options": ["Dual", "Duel"], "answer": "Dual"},
            {"type": "reading_comprehension", "passage": "Clouds are made of water.", "question": "What are clouds made of?", "options": ["Cotton", "Water"], "answer": "Water"},
            {"type": "letter_confusion", "question": "Identify the letter:", "options": ["p", "q"], "answer": "p"},
            {"type": "letter_confusion", "question": "Select the correct option:", "options": ["b", "d"], "answer": "b"}
        ]
    },
    {
        "id": 8,
        "questions": [
            {"type": "word_confusion", "question": "Which word is correct?", "options": ["Cite", "Site"], "answer": "Cite"},
            {"type": "word_confusion", "question": "Choose the right word:", "options": ["Lead", "Led"], "answer": "Led"},
            {"type": "reading_comprehension", "passage": "Honey is made by bees.", "question": "What makes honey?", "options": ["Bees", "Ants"], "answer": "Bees"},
            {"type": "letter_confusion", "question": "Identify the correct letter:", "options": ["n", "m"], "answer": "n"},
            {"type": "word_confusion", "question": "Which is correct?", "options": ["Dairy", "Diary"], "answer": "Dairy"},
            {"type": "reading_comprehension", "passage": "Snow is white and cold.", "question": "What color is snow?", "options": ["White", "Black"], "answer": "White"},
            {"type": "word_confusion", "question": "Which is correct?", "options": ["Sail", "Sale"], "answer": "Sail"},
            {"type": "reading_comprehension", "passage": "An owl is active at night.", "question": "When is an owl active?", "options": ["Day", "Night"], "answer": "Night"},
            {"type": "letter_confusion", "question": "Identify the letter:", "options": ["g", "q"], "answer": "g"},
            {"type": "letter_confusion", "question": "Select the correct option:", "options": ["d", "b"], "answer": "d"}
        ]
    },
    {
        "id": 9,
        "questions": [
            {"type": "word_confusion", "question": "Which word is correct?", "options": ["Flour", "Flower"], "answer": "Flour"},
            {"type": "word_confusion", "question": "Choose the right word:", "options": ["Hear", "Here"], "answer": "Hear"},
            {"type": "reading_comprehension", "passage": "Penguins live in cold places.", "question": "Where do penguins live?", "options": ["Cold", "Hot"], "answer": "Cold"},
            {"type": "letter_confusion", "question": "Identify the correct letter:", "options": ["p", "q"], "answer": "p"},
            {"type": "word_confusion", "question": "Which is correct?", "options": ["Metal", "Medal"], "answer": "Medal"},
            {"type": "reading_comprehension", "passage": "A rabbit has long ears.", "question": "What animal has long ears?", "options": ["Rabbit", "Cat"], "answer": "Rabbit"},
            {"type": "word_confusion", "question": "Which is correct?", "options": ["Principal", "Principle"], "answer": "Principal"},
            {"type": "reading_comprehension", "passage": "Kangaroos hop to move.", "question": "How do kangaroos move?", "options": ["Hop", "Run"], "answer": "Hop"},
            {"type": "letter_confusion", "question": "Identify the letter:", "options": ["g", "q"], "answer": "g"},
            {"type": "letter_confusion", "question": "Select the correct option:", "options": ["b", "d"], "answer": "b"}
        ]
    },
    {
        "id": 10,
        "questions": [
            {"type": "word_confusion", "question": "Which word is correct?", "options": ["Stationery", "Stationary"], "answer": "Stationery"},
            {"type": "word_confusion", "question": "Choose the right word:", "options": ["Loose", "Lose"], "answer": "Lose"},
            {"type": "reading_comprehension", "passage": "A bat is active at night.", "question": "When is a bat active?", "options": ["Day", "Night"], "answer": "Night"},
            {"type": "letter_confusion", "question": "Identify the correct letter:", "options": ["m", "n"], "answer": "m"},
            {"type": "word_confusion", "question": "Which is correct?", "options": ["Lightning", "Lightening"], "answer": "Lightning"},
            {"type": "reading_comprehension", "passage": "Zebras have black and white stripes.", "question": "What color are zebra stripes?", "options": ["Red and White", "Black and White"], "answer": "Black and White"},
            {"type": "word_confusion", "question": "Which is correct?", "options": ["Advice", "Advise"], "answer": "Advice"},
            {"type": "reading_comprehension", "passage": "A lion is the king of the jungle.", "question": "Which animal is called the king of the jungle?", "options": ["Tiger", "Lion"], "answer": "Lion"},
            {"type": "letter_confusion", "question": "Identify the letter:", "options": ["p", "q"], "answer": "p"},
            {"type": "letter_confusion", "question": "Select the correct option:", "options": ["b", "d"], "answer": "b"}
        ]
    }
]

def get_random_question_set():
    """Returns a randomly selected set of 10 questions"""
    return random.choice(QUESTION_SETS)["questions"]
