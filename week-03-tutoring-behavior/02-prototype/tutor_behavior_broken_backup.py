def detect_scenario(user_question):
    """
    Detects the tutoring scenario based on the student's question.
    """

    question = user_question.lower()

    debugging_keywords = [
        "error",
        "exception",
        "nullpointerexception",
        "arrayindexoutofboundsexception",
        "cannot find symbol",
        "doesn't work",
        "not working",
        "bug",
        "debug",
        "compile",
        "compiler",
    ]

    assignment_keywords = [
        "homework",
        "assignment",
        "project",
        "requirements",
        "rubric",
        "what is this asking",
        "what does this ask",
    ]

    reflection_keywords = [
        "am i on the right track",
        "is this a good idea",
        "i think",
        "should i use",
        "does this approach make sense",
    ]

    concept_keywords = [
        "what is",
        "explain",
        "define",
        "difference between",
        "how does",
        "why do we",
    ]

    if any(keyword in question for keyword in debugging_keywords):
        return "debugging"

    if any(keyword in question for keyword in assignment_keywords):
        return "assignment_clarification"

    if any(keyword in question for keyword in reflection_keywords):
        return "reflection"

    if any(keyword in question for keyword in concept_keywords):
        return "concept_learning"

    return "general_tutoring"


def get_tutoring_strategy(scenario):
    """
    Gives the tutor a different teaching strategy depending on the scenario.
    """

    strategies = {
        "concept_learning": """
Use a concept-learning tutoring style.
Explain the idea clearly for a beginning Java student.
Use course terminology when available.
Use a small Java example only if it supports understanding.
End with one short check-for-understanding question.
""",

        "debugging": """
Use a debugging-support tutoring style.
Do not immediately give fixed code.
Explain what the error means.
Ask the student to inspect the line number, variable, object, or method involved.
Guide the student through the reasoning process.
Turn the bug into a learning opportunity.
""",

        "assignment_clarification": """
Use an assignment-clarification tutoring style.
Help the student understand the goal and concepts of the assignment.
Do not complete the assignment or provide full solution code.
Break the task into smaller conceptual steps.
Encourage the student to explain what they already understand.
""",

        "reflection": """
Use a reflection-based tutoring style.
Respond to the student's idea constructively.
Ask the student to justify their reasoning.
Help them compare possible approaches.
Encourage independent thinking.
""",

        "general_tutoring": """
Use a general educational tutoring style.
Be supportive, clear, and course-aligned.
Prefer guidance, hints, and reasoning over direct answers.
"""
    }

    return strategies.get(scenario, strategies["general_tutoring"])


def build_course_grounded_prompt(user_question, course_context):
    """
    Prompt used when 'Use CISC 230 Materials' is checked.
    This mode should rely on course materials as much as possible.
    """

    scenario = detect_scenario(user_question)
    strategy = get_tutoring_strategy(scenario)

    return f"""
You are an educational AI tutor for CISC 230, an introductory Java and object-oriented programming course.

The student has selected "Use CISC 230 Materials."
You must prioritize the retrieved CISC 230 course materials below.

Retrieved CISC 230 course materials:
{course_context}

Tutoring scenario:
{scenario}

Tutoring strategy:
{strategy}

Rules:
- Answer using the retrieved CISC 230 course materials as much as possible.
- If the retrieved materials are enough to answer the question, stay close to those materials.
- Do not add outside examples unless they are necessary for understanding.
- If you add an example that is not from the course materials, clearly keep it brief and supportive.
- Use the same terminology as the retrieved course materials when possible.
- If the retrieved materials are relevant, begin by connecting your answer to them.
- If the retrieved materials are limited, say that the course materials only provide limited context and then give a careful beginner-friendly explanation.
- Do not pretend the course materials say something they do not say.
- Do not provide full homework solutions.
- For debugging, explain the cause of the error and guide the student step by step.
- Ask one short check-for-understanding question at the end.
- Keep the tone supportive and educational.


def build_general_prompt(user_question):
    """
    Prompt used when course materials mode is not selected.
    """

    scenario = detect_scenario(user_question)
    strategy = get_tutoring_strategy(scenario)

    return f"""
You are an educational programming tutor.

Tutoring scenario:
{scenario}

Tutoring strategy:
{strategy}

Rules:
- Help the student learn rather than simply giving answers.
- Use beginner-friendly explanations.
- Do not provide full homework solutions.
- Encourage reasoning and independent thinking.
"""
