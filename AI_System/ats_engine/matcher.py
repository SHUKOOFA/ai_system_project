import re

def _tokens(text: str) -> set[str]:
    return set(re.findall(r"\\b[\\w+#.]+\\b", text.lower()))

def match_resume(resume: str, job_description: str) -> float:
    """Percentage of unique job-description keywords found in the resume."""
    job_words = _tokens(job_description)
    if not job_words:
        return 0.0
    return round(len(_tokens(resume) & job_words) / len(job_words) * 100, 2)
