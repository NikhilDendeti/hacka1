GAME_LEVELS = {
    "mild": ["mild_level1", "mild_level2", "mild_level3"],
    "moderate": ["moderate_level1", "moderate_level2", "moderate_level3"],
    "severe": ["severe_level1", "severe_level2", "severe_level3"]
}

def calculate_score(correct_answers, total_questions):
    """Calculate percentage score"""
    return (correct_answers / total_questions) * 100

def get_next_level(current_level):
    """Fetch next level based on the sequence"""
    for category, levels in GAME_LEVELS.items():
        if current_level in levels:
            index = levels.index(current_level)
            return levels[index + 1] if index + 1 < len(levels) else None
    return None

GAME_LEVELS = {
    "mild": ["mild_level1", "mild_level2", "mild_level3"],
    "moderate": ["moderate_level1", "moderate_level2", "moderate_level3"],
    "severe": ["severe_level1", "severe_level2", "severe_level3"],
}

