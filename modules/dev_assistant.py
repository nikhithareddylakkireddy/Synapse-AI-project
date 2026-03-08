from ai_utils import ask_ai

def explain_code(code):

    prompt = f"""
    Explain this code clearly.

    {code}
    """

    return ask_ai(prompt)


def debug_error(error, code):

    prompt = f"""
    Explain the error and fix the code.

    Error:
    {error}

    Code:
    {code}
    """

    return ask_ai(prompt)