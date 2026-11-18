from parsers.resume_parser import parse_resume
from screening_ai.screener import screen_candidate
from interview_ai.questions import generate_questions
from scoring.score import calculate_score
from utils.logger import get_logger

logger = get_logger(__name__)

def main():
    resume = "Python SQL Machine Learning Data Science"
    job = "Python SQL Machine Learning"
    parsed = parse_resume(resume)
    result = screen_candidate(resume, job)
    rating = calculate_score(result["match_score"])
    questions = generate_questions("Data Scientist")
    logger.info("Candidate screening completed")
    print("\n=== AI SYSTEM DEMO ===")
    print("Resume:", parsed)
    print("Screening:", result)
    print("Rating:", rating)
    for i, question in enumerate(questions, 1):
        print(f"{i}. {question}")

if __name__ == "__main__":
    main()
