from ai_utils import ask_ai

def analyze_decision(options):

    prompt = f"""
You are an expert decision-making assistant.

Analyze the following options:

{options}

For each option provide:

1. Risks
2. Benefits
3. Long-term impact

After analyzing all options, clearly recommend the BEST option.

Final section format:

Best Choice:
Explain which option is best and why.
"""

    response = ask_ai(prompt)

    return response