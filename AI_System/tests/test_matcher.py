from ats_engine.matcher import match_resume

def test_full_match():
    assert match_resume("Python SQL Machine Learning", "Python SQL") == 100.0

def test_partial_match():
    assert match_resume("Python", "Python SQL") == 50.0

def test_empty_job_description():
    assert match_resume("Python SQL", "") == 0.0
