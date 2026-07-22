import streamlit as st

from retrieval import retrieve_course_context, format_retrieved_context
from tutor_behavior import (
    detect_scenario,
    build_course_grounded_prompt,
    build_general_prompt,
)
from model_client import get_model_response


st.set_page_config(
    page_title="CISC 230 AI Tutor",
    page_icon="📘",
    layout="centered",
)

st.title("CISC 230 AI Tutor")

st.write(
    "This prototype supports educational tutoring behavior for CISC 230. "
    "When course materials mode is enabled, the tutor uses retrieved CISC 230 materials and local Ollama."
)

use_course_materials = st.checkbox("Use CISC 230 Materials", value=True)

if use_course_materials:
    selected_backend = "Ollama"
    st.info(
        "Course materials mode is active. OpenAI is disabled in this mode. "
        "The tutor will use local Ollama with retrieved CISC 230 materials."
    )
else:
    selected_backend = st.selectbox(
        "Model backend for comparison mode",
        ["Ollama", "OpenAI"],
        index=0,
    )
    st.warning(
        "General comparison mode is active. Responses may not be grounded in CISC 230 materials."
    )

student_question = st.text_area(
    "Ask a CISC 230 question:",
    placeholder="Example: What is polymorphism?",
    height=120,
)

if st.button("Ask Tutor"):
    if not student_question.strip():
        st.warning("Please enter a question first.")
    else:
        scenario = detect_scenario(student_question)

        st.subheader("Detected Tutoring Scenario")
        st.write(scenario)

        if use_course_materials:
            retrieved_results = retrieve_course_context(student_question)
            course_context = format_retrieved_context(retrieved_results)

            st.subheader("Retrieved CISC 230 Materials")
            st.text(course_context)

            system_prompt = build_course_grounded_prompt(
                student_question,
                course_context,
            )
        else:
            system_prompt = build_general_prompt(student_question)

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": student_question},
        ]

        try:
            response = get_model_response(
                messages=messages,
                use_course_materials=use_course_materials,
                selected_backend=selected_backend,
            )

            st.subheader("Tutor Response")
            st.write(response)

        except Exception as e:
            st.error(f"Error: {e}")
