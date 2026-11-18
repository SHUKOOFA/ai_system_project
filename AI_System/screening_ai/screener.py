from ats_engine.matcher import match_resume

def screen_candidate(resume: str, job_description: str) -> dict:
    score = match_resume(resume, job_description)
    return {"match_score": score, "status": "Shortlisted" if score >= 50 else "Needs Review"}
