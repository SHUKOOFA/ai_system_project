from parsers.resume_parser import parse_resume
from screening_ai.screener import screen_candidate
from interview_ai.questions import generate_questions

def test_parser():
    result = parse_resume("  Python   SQL  ")
    assert result["word_count"] == 2
    assert result["resume_text"] == "Python SQL"

def test_screening():
    assert screen_candidate("Python SQL", "Python SQL")["status"] == "Shortlisted"

def test_questions():
    questions = generate_questions("Data Scientist")
    assert len(questions) == 3
    assert all("Data Scientist" in question for question in questions)
