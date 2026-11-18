import pytest
from scoring.score import calculate_score

def test_excellent():
    assert calculate_score(80) == "Excellent"

def test_good():
    assert calculate_score(60) == "Good"

def test_needs_improvement():
    assert calculate_score(30) == "Needs Improvement"

def test_rejects_out_of_range():
    with pytest.raises(ValueError):
        calculate_score(120)
