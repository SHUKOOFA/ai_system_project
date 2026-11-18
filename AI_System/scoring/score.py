def calculate_score(match_score: float) -> str:
    if not 0 <= match_score <= 100:
        raise ValueError("Match score must be between 0 and 100.")
    if match_score >= 75:
        return "Excellent"
    if match_score >= 50:
        return "Good"
    return "Needs Improvement"
