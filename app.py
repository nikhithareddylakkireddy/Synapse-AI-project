import streamlit as st

st.set_page_config(
    page_title="Synapse AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

import requests
import graphviz
from datetime import datetime

from modules.dev_assistant import explain_code, debug_error
from modules.github_analyzer import analyze_repo
from modules.code_quality import analyze_code_quality
from modules.pdf_explainer import explain_pdf
from modules.meeting_analyzer import analyze_meeting
from modules.career_simulator import suggest_career
from modules.decision_ai import analyze_decision

from modules.chat_with_code import chat_with_code
from modules.readme_generator import generate_readme
from modules.architecture_diagram import generate_architecture


# ---------------- LANDING PAGE ----------------

if "entered" not in st.session_state:
    st.session_state.entered = False

if not st.session_state.entered:

    st.title("👋 Hi Developer")
    st.subheader("Ready to Understand Any Codebase Instantly?")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("📁 Analyze GitHub repositories")

    with col2:
        st.info("💬 Chat with your code")

    with col3:
        st.info("📄 Generate documentation")

    if st.button("🚀 Enter Synapse AI"):
        st.session_state.entered = True
        st.rerun()

    st.stop()


# ---------------- HISTORY STORAGE ----------------

if "history" not in st.session_state:
    st.session_state.history = []

if "show_history" not in st.session_state:
    st.session_state.show_history = False


def save_history(q, a):
    st.session_state.history.append({
        "time": datetime.now().strftime("%H:%M:%S"),
        "q": q,
        "a": a
    })


# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.title("🤖 SYNAPSE AI")
    st.caption("Personal AI Intelligence Platform")

    menu = st.radio(
        "Navigation",
        [
            "Dashboard",
            "Analyze Repository",
            "Repository File Explorer",
            "Chat with Code",
            "Code Debugger",
            "Interview Prep",
            "Generate README",
            "Code Quality Review",
            "Architecture Diagram",
            "Research Explainer",
            "Meeting Analyzer",
            "Career Simulator",
            "Decision AI"
        ]
    )

    st.divider()

    if st.button("📜 History"):
        st.session_state.show_history = True

    history_text = ""

    for item in st.session_state.history:
        history_text += f"\n[{item['time']}]\nQUESTION:\n{item['q']}\n\nANSWER:\n{item['a']}\n\n"

    st.download_button(
        "⬇ Download History",
        history_text,
        file_name="synapse_ai_history.txt"
    )


# ---------------- TITLE ----------------

st.title("🚀 Synapse AI")


# ---------------- HISTORY PAGE ----------------

if st.session_state.show_history:

    st.header("📜 Query History")

    for item in reversed(st.session_state.history):

        st.subheader(item["time"])
        st.write("Question:", item["q"])
        st.write("Answer:", item["a"])
        st.divider()


# ---------------- DASHBOARD ----------------

elif menu == "Dashboard":

    st.markdown("""
    ## Your AI Powered Brain  
    Choose a module to begin.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("📁 Analyze Repository")

    with col2:
        st.info("💬 Chat with Code")

    with col3:
        st.info("🐞 Code Debugger")

    col4, col5, col6 = st.columns(3)

    with col4:
        st.info("📄 Generate README")

    with col5:
        st.info("🔎 Code Quality Review")

    with col6:
        st.info("🏗 Architecture Diagram")

    col7, col8, col9 = st.columns(3)

    with col7:
        st.info("📚 Research Explainer")

    with col8:
        st.info("🎤 Meeting Analyzer")

    with col9:
        st.info("🎓 Career Simulator")


# ---------------- ANALYZE REPOSITORY ----------------

elif menu == "Analyze Repository":

    st.header("📁 Repository Analyzer")

    repo = st.text_input("GitHub Repo URL")

    if st.button("Analyze"):

        result = analyze_repo(repo)

        st.write(result)

        save_history(repo, result)


# ---------------- REPOSITORY FILE EXPLORER ----------------

elif menu == "Repository File Explorer":

    st.header("📂 Repository File Explorer")

    repo = st.text_input("Paste GitHub Repository URL")

    if st.button("Load Repository Files"):

        try:

            parts = repo.strip("/").split("/")
            owner = parts[-2]
            repo_name = parts[-1]

            api_url = f"https://api.github.com/repos/{owner}/{repo_name}/contents"

            response = requests.get(api_url)

            if response.status_code != 200:
                st.error("Could not fetch repository")

            else:

                data = response.json()

                st.success("Repository loaded!")

                st.subheader("Repository Files")

                for file in data:
                    st.write(file["name"])

                save_history(repo, "Repository files fetched")

        except:
            st.error("Invalid GitHub URL")


# ---------------- CHAT WITH CODE ----------------

elif menu == "Chat with Code":

    st.header("💬 Chat with Code")

    code = st.text_area("Paste code")
    question = st.text_input("Ask question")

    if st.button("Ask"):

        result = chat_with_code(code, question)

        st.write(result)

        save_history(question, result)


# ---------------- CODE DEBUGGER ----------------

elif menu == "Code Debugger":

    st.header("🐞 Code Debugger")

    code = st.text_area("Paste your code")
    error = st.text_area("Paste error message")

    if st.button("Debug"):

        result = debug_error(error, code)

        st.write(result)

        save_history(error, result)


# ---------------- INTERVIEW PREP ----------------

elif menu == "Interview Prep":

    st.header("💬 Interview Preparation")

    role = st.text_input("Enter Job Role (Example: Python Developer)")

    level = st.selectbox(
        "Select Difficulty Level",
        ["Beginner", "Intermediate", "Advanced"]
    )

    if st.button("Generate Interview Questions"):

        questions = f"""
### Interview Questions for {role} ({level})

1. What is Python?
2. Explain Object-Oriented Programming.
3. What is the difference between list and tuple?
4. What are Python decorators?
5. What is exception handling?
6. What is a REST API?
7. Difference between GET and POST requests.
8. What is multithreading?
9. What is a virtual environment?
10. Explain Python's dynamic typing.
"""

        answers = """
### Answers

1. Python is a high-level programming language used for web development, AI, data science, and automation.

2. Object-Oriented Programming organizes software into objects and classes.

3. Lists are mutable while tuples are immutable.

4. Decorators modify functions without changing their code.

5. Exception handling manages runtime errors using try, except, finally.

6. REST API allows communication between systems using HTTP requests.

7. GET retrieves data while POST sends data.

8. Multithreading allows concurrent execution of tasks.

9. Virtual environments isolate project dependencies.

10. Dynamic typing means variable types are determined at runtime.
"""

        st.subheader("Interview Questions")
        st.write(questions)

        st.subheader("Answers")
        st.write(answers)

        save_history(role + " " + level, questions + answers)


# ---------------- README GENERATOR ----------------

elif menu == "Generate README":

    st.header("📄 README Generator")

    files = st.text_area("Paste project structure")

    if st.button("Generate"):

        result = generate_readme(files)

        st.code(result)

        save_history(files, result)


# ---------------- CODE QUALITY ----------------

elif menu == "Code Quality Review":

    st.header("🔎 Code Quality Review")

    code = st.text_area("Paste code")

    if st.button("Analyze"):

        result = analyze_code_quality(code)

        st.write(result)

        save_history(code, result)


# ---------------- ARCHITECTURE ----------------

elif menu == "Architecture Diagram":

    st.header("🏗 Architecture Diagram")

    files = st.text_area("Paste project files")

    if st.button("Generate"):

        explanation = generate_architecture(files)

        st.write(explanation)

        diagram = graphviz.Digraph()

        diagram.node("User")
        diagram.node("Frontend")
        diagram.node("Backend")
        diagram.node("Database")

        diagram.edges([
            ("User","Frontend"),
            ("Frontend","Backend"),
            ("Backend","Database")
        ])

        st.graphviz_chart(diagram)

        save_history(files, explanation)


# ---------------- RESEARCH EXPLAINER ----------------

elif menu == "Research Explainer":

    st.header("📚 Research Paper Explainer")

    pdf = st.file_uploader("Upload PDF")

    if pdf:

        result = explain_pdf(pdf)

        st.write(result)

        save_history("PDF", result)


# ---------------- MEETING ANALYZER ----------------

elif menu == "Meeting Analyzer":

    st.header("🎤 Meeting Analyzer")

    transcript = st.text_area("Paste transcript")

    if st.button("Analyze"):

        result = analyze_meeting(transcript)

        st.write(result)

        save_history(transcript, result)


# ---------------- CAREER SIMULATOR ----------------

elif menu == "Career Simulator":

    st.header("🎓 Career Simulator")

    skills = st.text_input("Skills")
    interest = st.text_input("Interest")

    if st.button("Suggest Career"):

        result = suggest_career(skills, interest)

        st.write(result)

        save_history(skills + interest, result)


# ---------------- DECISION AI ----------------

elif menu == "Decision AI":

    st.header("⚖ Decision AI")

    if "options" not in st.session_state:
        st.session_state.options = ["",""]

    for i in range(len(st.session_state.options)):
        st.session_state.options[i] = st.text_input(f"Option {i+1}", st.session_state.options[i])

    if st.button("➕ Add Option"):
        st.session_state.options.append("")

    if st.button("Analyze Decision"):

        text=""

        for i,opt in enumerate(st.session_state.options):
            text += f"Option {i+1}: {opt}\n"

        result = analyze_decision(text)

        st.write(result)

        save_history(text, result)