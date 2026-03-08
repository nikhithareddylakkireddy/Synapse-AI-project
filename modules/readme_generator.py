from ai_utils import ask_ai

def generate_readme(files):

    prompt = f"""
You are a professional software documentation expert.

Generate a complete README.md for a project with these files:

{files}

Include sections:

1. Project Title
2. Project Description
3. Features
4. Installation
5. Usage
6. Technologies Used
7. Future Improvements
"""

    response = ask_ai(prompt)

    return response