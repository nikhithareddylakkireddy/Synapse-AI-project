from ai_utils import ask_ai

def suggest_career(skills, interest):

    prompt = f"""
    Suggest career paths.

    Skills:
    {skills}

    Interests:
    {interest}

    Provide roadmap.
    """

    return ask_ai(prompt)