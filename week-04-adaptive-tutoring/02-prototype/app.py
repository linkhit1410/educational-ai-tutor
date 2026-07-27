from pathlib import Path
import re

import streamlit as st

from adaptive_rules import make_adaptive_decision
from model_client import get_model_response
from retrieval import format_retrieved_context, retrieve_course_context
from tutor_behavior import detect_scenario


COURSE_MATERIALS_DIR = Path(__file__).resolve().parents[1] / "00-course-materials"

KNOWN_OUTSIDE_EXAMPLES = (
    "animal",
    "dog",
    "cat",
    "vehicle",
    "car",
    "house",
    "houses",
    "game",
    "games",
    "shape",
    "shapes",
)


def load_policy_context() -> str:
    """
    Load only CISC 230 policy files.

    This bypasses normal keyword retrieval so a direct-solution request cannot
    retrieve unrelated lecture chunks because of words such as "write."
    """
    if not COURSE_MATERIALS_DIR.exists():
        return ""

    policy_paths = sorted(
        path
        for path in COURSE_MATERIALS_DIR.rglob("*.txt")
        if "polic" in path.name.lower()
        or "polic"
        in str(path.parent.relative_to(COURSE_MATERIALS_DIR)).lower()
    )

    sections = []

    for path in policy_paths:
        try:
            content = path.read_text(
                encoding="utf-8",
                errors="ignore",
            ).strip()
        except OSError as error:
            print(f"Could not read policy file {path}: {error}")
            continue

        if not content:
            continue

        source = path.relative_to(COURSE_MATERIALS_DIR)

        sections.append(
            f"Source: {source}\n"
            f"Content: {content}"
        )

    return "\n\n---\n\n".join(sections)


def build_policy_only_prompt(
    adaptive_decision,
    policy_context: str,
) -> str:
    """
    Build the strict prompt used for high-risk direct-solution requests.
    """
    return f"""
You are an educational AI tutor for CISC 230.

This request has been classified as high academic-integrity risk.

Adaptive decision:
- Student intent: {adaptive_decision.intent}
- Student effort level: {adaptive_decision.effort_level}
- Academic-integrity risk: {adaptive_decision.integrity_risk}
- Recommended support level: {adaptive_decision.support_level}
- Rationale: {adaptive_decision.rationale}

The following CISC 230 policy context is your only source:

<course_policy_context>
{policy_context}
</course_policy_context>

Required response behavior:
- Use only the policy context above.
- Refuse to write, solve, or complete the homework.
- Do not provide complete solution code.
- Do not guess what Homework 3 contains.
- Do not describe assignment requirements that are not explicitly stated
  in the policy context.
- Do not add programming explanations, examples, analogies, code, or facts
  from outside the policy context.
- Briefly redirect the student toward permitted learning support, such as
  explaining a concept, interpreting wording they provide, reviewing their
  own attempt, or debugging code they wrote.
- Ask one short question about what they have tried or which concept they
  want help understanding.
- Keep the response supportive and concise.
"""


def build_strict_course_prompt(
    student_question: str,
    scenario: str,
    adaptive_decision,
    course_context: str,
) -> str:
    """
    Build a context-only prompt for non-high-risk tutoring requests.
    """
    return f"""
You are an educational AI tutor for CISC 230.

You must answer only from the retrieved CISC 230 materials below.

<retrieved_course_context>
{course_context}
</retrieved_course_context>

Student question:
{student_question}

Tutoring scenario:
{scenario}

Adaptive decision:
- Student intent: {adaptive_decision.intent}
- Student effort level: {adaptive_decision.effort_level}
- Academic-integrity risk: {adaptive_decision.integrity_risk}
- Recommended support level: {adaptive_decision.support_level}
- Rationale: {adaptive_decision.rationale}

Strict grounding rules:
- Use only facts, terminology, examples, and code explicitly present in
  <retrieved_course_context>.
- Do not use general Java knowledge or background knowledge to fill gaps.
- Do not invent examples, analogies, classes, objects, methods,
  assignments, or scenarios.
- Do not use Animal/Dog/Cat, Vehicle/Car, houses, games, shapes, or any
  other example unless it explicitly appears in
  <retrieved_course_context>.
- Do not claim the course materials say something they do not say.
- Do not infer missing assignment details from the student's question.
- If the context is insufficient, say:
  "The retrieved CISC 230 materials do not contain enough information to
  answer that question accurately."
- After that sentence, ask the student to provide the relevant slide,
  assignment wording, error message, or code excerpt.
- Never provide a complete graded-work solution.

Adaptive tutoring rules:
- For concept learning, give a concise course-grounded explanation and end
  with one short check-for-understanding question.
- For debugging, distinguish between a retrieved course example and
  the student's actual code.
- A retrieved example may show one possible cause, but never state that
  it is the cause of the student's error unless the student's own code
  supports that conclusion.
- If the student has not provided their code, line number, or complete
  error details, explicitly say that the exact cause cannot yet be
  determined.
- Briefly describe only what the retrieved course example demonstrates.
- Then ask for the relevant code line and the complete error message.
- For assignment clarification, clarify only requirements shown in the
  retrieved context and do not solve the assignment.
- For high-effort work, provide a targeted hint without rewriting the full
  solution.
- Keep the response supportive and concise, usually one or two short
  paragraphs.
"""


def find_unsupported_known_examples(
    response: str,
    course_context: str,
) -> list[str]:
    """
    Detect known outside examples when they do not appear in retrieved context.

    This validation guard checks for examples that previously leaked into
    course-grounded answers.
    """
    unsupported = []

    response_lower = response.lower()
    context_lower = course_context.lower()

    for example in KNOWN_OUTSIDE_EXAMPLES:
        pattern = rf"\b{re.escape(example)}\b"

        appears_in_response = re.search(
            pattern,
            response_lower,
        )

        appears_in_context = re.search(
            pattern,
            context_lower,
        )

        if appears_in_response and not appears_in_context:
            unsupported.append(example)

    return unsupported


def find_unsupported_generated_identifiers(
    response: str,
    course_context: str,
) -> list[str]:
    """
    Detect invented quoted names and method-style identifiers.

    Examples:
    - "Bird"
    - "Duck"
    - "Eagle"
    - makeSound()
    """
    quoted_identifiers = re.findall(
        r"""["']([A-Za-z_][A-Za-z0-9_]*)["']""",
        response,
    )

    method_identifiers = re.findall(
        r"\b([A-Za-z_][A-Za-z0-9_]*)\s*\(\)",
        response,
    )

    candidates = set(
        quoted_identifiers + method_identifiers
    )

    context_lower = course_context.lower()
    unsupported = []

    for identifier in candidates:
        pattern = rf"\b{re.escape(identifier.lower())}\b"

        if not re.search(pattern, context_lower):
            unsupported.append(identifier)

    return sorted(unsupported)


def build_context_only_fallback(
    course_context: str,
) -> str:
    """
    Return a safe answer copied directly from retrieved course content
    if the model continues introducing unsupported material.
    """
    content_sections = re.findall(
        r"Content:\s*(.*?)(?=\n\n---\n\n|\Z)",
        course_context,
        flags=re.DOTALL,
    )

    for section in content_sections:
        cleaned = re.sub(
            r"--- Slide \d+ ---\s*",
            "",
            section,
        ).strip()

        if cleaned.lower().startswith("source file:"):
            continue

        if len(cleaned.split()) < 8:
            continue

        return (
            "According to the retrieved CISC 230 materials:\n\n"
            f"{cleaned}\n\n"
            "Which part of this course definition would you like "
            "to examine more closely?"
        )

    return (
        "The retrieved CISC 230 materials do not contain enough "
        "information to answer that question accurately. Please "
        "provide the relevant slide, assignment wording, error "
        "message, or code excerpt."
    )


def get_grounded_response(
    final_prompt: str,
    student_question: str,
    course_context: str,
) -> str:
    """
    Generate a draft, then run a strict grounding-review pass.

    If unsupported names or examples remain after review, return a
    deterministic response taken directly from the retrieved context.
    """
    draft_messages = [
        {
            "role": "system",
            "content": final_prompt,
        },
        {
            "role": "user",
            "content": student_question,
        },
    ]

    draft_response = get_model_response(
        draft_messages,
        use_course_materials=True,
        selected_backend="Ollama",
    )

    review_prompt = f"""
You are a strict grounding reviewer for a CISC 230 educational tutor.

Student question:
{student_question}

The following retrieved CISC 230 context is the only permitted source:

<retrieved_course_context>
{course_context}
</retrieved_course_context>

Draft response:
<draft_response>
{draft_response}
</draft_response>

Rewrite the draft so that it follows these rules:
- Every technical statement must be directly supported by the retrieved
  CISC 230 context.
- Remove every example, analogy, class name, object name, method name,
  code fragment, or scenario that does not explicitly appear in the
  retrieved context.
- Do not replace removed examples with different invented examples.
- Do not use outside Java or object-oriented programming knowledge.
- Preserve a concise, supportive tutoring style.
- End with one short check-for-understanding question.
- Return only the corrected tutor response.
"""

    review_messages = [
        {
            "role": "system",
            "content": review_prompt,
        },
        {
            "role": "user",
            "content": (
                "Review and rewrite the draft using only the "
                "retrieved context."
            ),
        },
    ]

    reviewed_response = get_model_response(
        review_messages,
        use_course_materials=True,
        selected_backend="Ollama",
    )

    # Remove XML-style wrapper tags sometimes produced by the model,
    # such as <corrected_response>.
    reviewed_response = re.sub(
        r"</?[A-Za-z_][A-Za-z0-9_-]*>",
        "",
        reviewed_response,
    ).strip()

    # Keep only one check-for-understanding question.
    question_marks = [
        index
        for index, character in enumerate(reviewed_response)
        if character == "?"
    ]

    if len(question_marks) > 1:
        reviewed_response = reviewed_response[
            : question_marks[0] + 1
        ].strip()

    unsupported_examples = find_unsupported_known_examples(
        reviewed_response,
        course_context,
    )

    unsupported_identifiers = (
        find_unsupported_generated_identifiers(
            reviewed_response,
            course_context,
        )
    )

    if unsupported_examples or unsupported_identifiers:
        return build_context_only_fallback(
            course_context
        )

    return reviewed_response




def build_abstract_class_technical_response(
    course_context: str,
) -> str:
    """
    Give a targeted, course-grounded hint for a student's abstract-class
    implementation without writing the complete solution.
    """
    context_lower = course_context.lower()

    has_abstract_class_guidance = (
        "does not have to contain abstract methods" in context_lower
        and "must override the abstract methods of the parent" in context_lower
    )

    if has_abstract_class_guidance:
        return (
            "The retrieved Chapter 9 materials say that an abstract class "
            "may contain both abstract methods without definitions and "
            "non-abstract methods with full definitions. They also say that "
            "a child class must override the parent's abstract methods, or "
            "the child must also be declared abstract.\n\n"
            "Compare the method declaration in your superclass with the "
            "corresponding method in the subclass where the behavior is "
            "wrong. What are the two method declarations, and what behavior "
            "did you expect versus what actually happened?"
        )

    return (
        "The retrieved CISC 230 materials discuss abstract classes, but they "
        "do not provide enough context to identify the problem in your "
        "implementation.\n\n"
        "What are the superclass method declaration, the subclass method "
        "declaration, the expected behavior, and the actual behavior?"
    )

def build_low_evidence_debugging_response(
    course_context: str,
) -> str:
    """
    Give a safe, course-grounded response when the student names an
    error but has not supplied enough evidence to diagnose their code.
    """
    context_lower = course_context.lower()

    has_null_example = (
        "astring = null" in context_lower
        and "astring.length()" in context_lower
    )

    if has_null_example:
        return (
            "The retrieved CISC 230 example shows one possible pattern: "
            "`aString` is set to `null`, and the next line calls "
            "`aString.length()`. That example does not establish the "
            "cause of your own error because you have not provided your "
            "code or complete error message.\n\n"
            "What complete error message and relevant code line does "
            "your program show?"
        )

    return (
        "The retrieved CISC 230 materials contain information related "
        "to this error, but they do not establish the cause in your "
        "program because your code and complete error message were not "
        "provided.\n\n"
        "What complete error message and relevant code line does your "
        "program show?"
    )

st.title("CISC 230 Adaptive AI Tutor")

st.write(
    "This tutor uses CISC 230 course materials and adaptive tutoring rules. "
    "It considers the student's question type, effort level, "
    "academic-integrity risk, and the appropriate level of support."
)

st.info(
    "Course materials mode is always active. High-risk requests use only "
    "course policy context; other requests use strictly retrieved "
    "CISC 230 materials."
)

student_question = st.text_area(
    "Enter your CISC 230 question:",
    placeholder=(
        "Example: I created a superclass, but I am not sure where "
        "this method belongs."
    ),
)

if st.button("Ask Tutor"):
    if not student_question.strip():
        st.warning("Please enter a question first.")

    else:
        scenario = detect_scenario(student_question)

        adaptive_decision = make_adaptive_decision(
            student_question
        )

        is_high_risk_request = (
            adaptive_decision.intent == "direct_solution_request"
            or adaptive_decision.integrity_risk == "high"
        )

        if is_high_risk_request:
            course_context = load_policy_context()

            if not course_context:
                st.error(
                    "No CISC 230 course policy file was found. "
                    "Check week-04-adaptive-tutoring/"
                    "00-course-materials."
                )
                st.stop()

            final_prompt = build_policy_only_prompt(
                adaptive_decision,
                course_context,
            )

            retrieval_mode = "Policy-only routing"

        else:
            retrieved_results = retrieve_course_context(
                student_question,
                max_results=4,
            )

            course_context = format_retrieved_context(
                retrieved_results
            )

            final_prompt = build_strict_course_prompt(
                student_question,
                scenario,
                adaptive_decision,
                course_context,
            )

            retrieval_mode = "Topic-based course retrieval"

        needs_more_debugging_evidence = (
            adaptive_decision.intent == "debugging_support"
            and adaptive_decision.effort_level
            in {"low_effort", "moderate_effort"}
        )

        is_abstract_class_technical_help = (
            adaptive_decision.intent == "high_effort_technical_help"
            and "abstract" in student_question.lower()
        )

        if needs_more_debugging_evidence:
            tutor_response = build_low_evidence_debugging_response(
                course_context
            )
        elif is_abstract_class_technical_help:
            tutor_response = build_abstract_class_technical_response(
                course_context
            )
        else:
            tutor_response = get_grounded_response(
                final_prompt,
                student_question,
                course_context,
            )

        st.subheader("Detected Tutoring Scenario")
        st.write(scenario)

        st.subheader("Adaptive Decision")
        st.write(
            f"**Student intent:** "
            f"{adaptive_decision.intent}"
        )
        st.write(
            f"**Effort level:** "
            f"{adaptive_decision.effort_level}"
        )
        st.write(
            f"**Support level:** "
            f"{adaptive_decision.support_level}"
        )
        st.write(
            f"**Academic-integrity risk:** "
            f"{adaptive_decision.integrity_risk}"
        )
        st.write(
            f"**Rationale:** "
            f"{adaptive_decision.rationale}"
        )

        st.subheader("Retrieval Mode")
        st.write(retrieval_mode)

        st.subheader("Retrieved CISC 230 Materials")
        st.text(course_context)

        st.subheader("Tutor Response")
        st.write(tutor_response)
