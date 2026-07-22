import streamlit as st
import requests

st.set_page_config(page_title="Educational AI Tutor Prototype", page_icon="🎓")

st.title("Educational AI Tutor Prototype")
st.write(
    "Ask a programming question. This prototype uses a local Ollama model "
    "and is designed to guide learning instead of simply giving complete answers."
)

MODEL_NAME = "llama3.2"

SYSTEM_PROMPT = """
You are an educational AI tutor for introductory programming students.

Your goals:
- Help students learn, not just complete work.
- Ask guiding questions when appropriate.
- Give hints before giving full solutions.
- Encourage students to explain what they tried.
- Help students debug step by step.
- Avoid writing complete homework solutions.

If a student asks for a full assignment solution, politely refuse to provide the full answer,
then offer to help them break the problem into smaller steps.
"""

student_question = st.text_area(
    "Student question:",
    placeholder="Example: Why am I getting a NullPointerException in Java?"
)

if st.button("Ask Tutor"):
    if not student_question.strip():
        st.warning("Please enter a question first.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    "http://localhost:11434/api/generate",
                    json={
                        "model": MODEL_NAME,
                        "prompt": SYSTEM_PROMPT + "\n\nStudent question: " + student_question,
                        "stream": False
                    },
                    timeout=120
                )

                response.raise_for_status()
                answer = response.json().get("response", "")

                st.subheader("Tutor Response")
                st.write(answer)

            except requests.exceptions.ConnectionError:
                st.error(
                    "Could not connect to Ollama. Make sure the Ollama app is open, "
                    "then try again."
                )
            except Exception as e:
                st.error(f"Something went wrong: {e}")
