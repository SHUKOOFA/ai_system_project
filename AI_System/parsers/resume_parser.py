def parse_resume(text: str) -> dict:
    """Return a simple structured representation of resume text."""
    if not isinstance(text, str):
        raise TypeError("Resume text must be a string.")
    cleaned = " ".join(text.split())
    return {"resume_text": cleaned, "word_count": len(cleaned.split())}
