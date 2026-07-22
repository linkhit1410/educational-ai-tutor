import streamlit as st

from retrieval import retrieve_course_context, format_retrieved_context
from tutor_behavior import detect_scenario, build_course_grounded_prompt
from model_client import get_model_response


st.set_page_config(page_title="CISC 230 AI Tutor", page_icon="📘")

st.title("CISC 230 AI Tutor")
st.write(
    "This tutor uses retrieved CISC 230 course materials to support learning "
    "through hints, explanations, and guided questions."
)

st.info(
    "Course materials mode is always active. The tutor retrieves CISC 230 materials "
    "and uses the local Ollama model. OpenAI/general chatbot mode is disabled."
)

student_question = st.text_area(
    "Enter your CISC 230 question:",
    placeholder="Example: What is inheritance?"
)

if st.button("Ask Tutor"):
    if not student_question.strip():
        st.warning("Please enter a question first.")
    else:
        scenario = detect_scenario(student_question)

        retrieved_results = retrieve_course_context(student_question, max_results=4)
        course_context = format_retrieved_context(retrieved_results)

        prompt = build_course_grounded_prompt(student_question, course_context)

        messages = [
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": student_question
            }
        ]

        with st.spinner("Retrieving CISC 230 materials and generating tutor response..."):
            tutor_response = get_model_response(
                messages,
                use_course_materials=True,
                selected_backend="Ollama"
            )

        st.subheader("Detected Tutoring Scenario")
        st.write(scenario)

        st.subheader("Retrieved CISC 230 Materials")
        st.text(course_context)

        st.subheader("Tutor Response")
        st.write(tutor_response)
