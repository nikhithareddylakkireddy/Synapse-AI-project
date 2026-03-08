from ai_utils import ask_ai

def analyze_code_quality(code):

    prompt = f"""
You are a software code reviewer.

Analyze the following code and give a structured report.

Code:
{code}

Provide analysis in this format:

Readability:
- Explain readability of the code.

Complexity:
- Explain complexity level.

Performance Issues:
- Mention any performance problems.

Improvements:
- Suggest improvements.

Finally give a score for the code quality.

Score format:
Code Quality Score: X/10

Explain why you gave that score.
"""

    return ask_ai(prompt)