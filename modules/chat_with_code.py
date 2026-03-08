from ai_utils import ask_ai

def chat_with_code(code, question):

    prompt = f"""
You are an expert software developer.

Here is the code:
{code}

User question:
{question}

Explain clearly and help the user understand the code.
"""

    response = ask_ai(prompt)

    return response