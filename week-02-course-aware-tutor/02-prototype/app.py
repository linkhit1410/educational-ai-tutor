import streamlit as st
import requests
from retrieval import retrieve_context
from model_client import generate_response

st.set_page_config(page_title="Course-Aware AI Tutor Prototype", page_icon="🎓")

st.title("Course-Aware AI Tutor Prototype")
st.write(
    "Ask a programming question. This prototype can use CISC230 course materials "
    "to give more course-aware tutoring support."
)

BASE_SYSTEM_PROMPT = """
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

COURSE_AWARE_PROMPT = """
You are a course-aware educational AI tutor for CISC230.

Use the course context below when it is relevant.
Your response should align with the course materials, course policies, and current concepts.

Do not claim that an example, phrase, or requirement comes from the course materials unless it appears in the retrieved course context.
If the retrieved course context is limited, say that the available course context is limited and provide a general explanation.
Use small examples only when they support learning, and clearly label them as general examples unless they appear in the course context.
When giving programming examples, prefer Java unless the course context says otherwise.

Important tutoring rules:
- Help students learn, not just complete work.
- Ask guiding questions when appropriate.
- Give hints before giving full solutions.
- Encourage students to explain what they tried.
- Help students debug step by step.
- Do not write complete homework solutions.
- Do not provide full assignment code.
- If a student asks for a full solution, politely refuse and offer conceptual help, hints, or a step-by-step plan.

Course Context:
{course_context}
"""

model_backend = st.selectbox(
    "Model backend:",
    [
        "Ollama - llama3.2",
        "OpenAI API - gpt-4o-mini"
    ]
)

student_question = st.text_area(
    "Student question:",
    placeholder="Example: What is inheritance?"
)

use_retrieval = st.checkbox("Use CISC230 course materials", value=True)

if st.button("Ask Tutor"):
    if not student_question.strip():
        st.warning("Please enter a question first.")
    else:
        with st.spinner("Thinking..."):
            try:
                if use_retrieval:
                    course_context = retrieve_context(student_question)

                    prompt = (
                        COURSE_AWARE_PROMPT.format(course_context=course_context)
                        + "\n\nStudent question: "
                        + student_question
                    )

                    st.subheader("Retrieved Course Context")
                    st.text(course_context)

                else:
                    prompt = BASE_SYSTEM_PROMPT + "\n\nStudent question: " + student_question

                answer = generate_response(prompt, model_backend)

                st.subheader("Tutor Response")
                st.write(answer)

            except requests.exceptions.ConnectionError:
                st.error(
                    "Could not connect to Ollama. Make sure the Ollama app is open, "
                    "then try again."
                )
            except Exception as e:
                st.error(f"Something went wrong: {e}")
