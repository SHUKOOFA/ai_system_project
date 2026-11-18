def generate_questions(role: str) -> list[str]:
    if not role or not role.strip():
        raise ValueError("Role must not be empty.")
    role = role.strip()
    return [
        f"Tell me about your experience relevant to {role}.",
        f"Which technical skills are important for {role}?",
        f"Describe how you would solve a challenging problem in {role}.",
    ]
