from ai_utils import ask_ai

def analyze_meeting(transcript):

    prompt = f"""
    Analyze this meeting transcript.

    Provide:
    - summary
    - action items
    - key decisions

    Transcript:
    {transcript}
    """

    return ask_ai(prompt)