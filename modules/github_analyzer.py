import requests
from ai_utils import ask_ai

def analyze_repo(repo_url):

    parts = repo_url.split("/")
    owner = parts[-2]
    repo = parts[-1]

    api = f"https://api.github.com/repos/{owner}/{repo}/contents"

    r = requests.get(api)

    files = []

    if r.status_code == 200:

        for file in r.json():
            files.append(file["name"])

    file_list = ", ".join(files)

    prompt = f"""
    Analyze this GitHub project.

    Files:
    {file_list}

    Explain:
    - purpose
    - tech stack
    - improvements
    """

    return ask_ai(prompt)