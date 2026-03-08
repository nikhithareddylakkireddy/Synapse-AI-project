import PyPDF2
from ai_utils import ask_ai

def explain_pdf(pdf):

    reader = PyPDF2.PdfReader(pdf)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    text = text[:3000]

    prompt = f"""
    Explain this research paper simply.

    {text}

    Give:
    - summary
    - key concepts
    """

    return ask_ai(prompt)