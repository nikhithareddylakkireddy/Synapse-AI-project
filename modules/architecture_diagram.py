from ai_utils import ask_ai
import graphviz

def generate_architecture(files):

    prompt = f"""
Explain the architecture of this project.

Files:
{files}

Explain:
1. Frontend
2. Backend
3. Database
4. Workflow
5. Key components
"""

    explanation = ask_ai(prompt)

    return explanation


def generate_architecture_diagram():

    diagram = graphviz.Digraph()

    diagram.node("User", "User")
    diagram.node("Frontend", "Frontend\n(HTML/CSS/JS)")
    diagram.node("Backend", "Backend\n(Python App)")
    diagram.node("Database", "Database\n(SQLite/MySQL)")

    diagram.edges([
        ("User", "Frontend"),
        ("Frontend", "Backend"),
        ("Backend", "Database"),
        ("Database", "Backend"),
        ("Backend", "Frontend")
    ])

    return diagram