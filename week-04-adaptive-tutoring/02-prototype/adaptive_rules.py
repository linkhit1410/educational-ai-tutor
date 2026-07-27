"""
Adaptive tutoring rules for Week 4.

This module classifies:
1. Student intent
2. Student effort level
3. Academic-integrity risk
4. Recommended support level

The goal is to help the tutor decide how much support to provide.
"""

from dataclasses import dataclass


@dataclass
class AdaptiveDecision:
    intent: str
    effort_level: str
    support_level: str
    integrity_risk: str
    rationale: str


def classify_intent(question: str) -> str:
    """Classify what the student appears to be trying to accomplish."""
    q = question.lower()

    direct_solution_terms = [
        "write my homework",
        "write my assignment",
        "solve this",
        "give me the answer",
        "give me the full code",
        "do this for me",
        "complete my assignment",
        "answer key",
    ]

    assignment_terms = [
        "homework",
        "assignment",
        "lab",
        "project",
        "require",
        "requirements",
        "what does",
        "supposed to",
    ]

    debugging_terms = [
        "error",
        "exception",
        "nullpointer",
        "arrayindexoutofbounds",
        "cannot find symbol",
        "not working",
        "bug",
        "debug",
        "crash",
        "line",
        "stack trace",
    ]

    reflection_terms = [
        "am i on the right track",
        "does this make sense",
        "should i use",
        "is this a good design",
        "i think",
        "not sure whether",
        "belongs in",
    ]

    concept_terms = [
        "what is",
        "explain",
        "difference between",
        "how does",
        "why does",
        "define",
    ]

    high_effort_terms = [
        "i created",
        "i wrote",
        "i tried",
        "my code",
        "my method",
        "my class",
        "my constructor",
        "overridden",
        "superclass",
        "subclass",
    ]

    if any(term in q for term in direct_solution_terms):
        return "direct_solution_request"

    if any(term in q for term in debugging_terms):
        if any(term in q for term in high_effort_terms):
            return "high_effort_technical_help"
        return "debugging_support"

    if any(term in q for term in reflection_terms):
        return "reflection_or_design_reasoning"

    if any(term in q for term in assignment_terms):
        return "assignment_clarification"

    if any(term in q for term in concept_terms):
        return "concept_learning"

    if any(term in q for term in high_effort_terms):
        return "high_effort_technical_help"

    return "general_tutoring"


def estimate_effort(question: str) -> str:
    """Estimate how much effort the student has shown."""
    q = question.lower()

    low_effort_terms = [
        "solve this",
        "give me the answer",
        "write my homework",
        "write my assignment",
        "do this for me",
        "full code",
    ]

    high_effort_terms = [
        "i created",
        "i wrote",
        "i tried",
        "i tested",
        "my code",
        "my method",
        "my class",
        "my constructor",
        "error message",
        "line",
        "expected",
        "actual",
        "overridden",
        "superclass",
        "subclass",
    ]

    non_graded_terms = [
        "practice example",
        "non-homework example",
        "small example",
        "made-up example",
        "not for homework",
    ]

    if any(term in q for term in low_effort_terms):
        return "low_effort"

    if any(term in q for term in non_graded_terms):
        return "non_graded_learning_request"

    if any(term in q for term in high_effort_terms):
        return "high_effort"

    if len(question.split()) <= 4:
        return "low_effort"

    return "moderate_effort"


def select_support_level(intent: str, effort_level: str) -> tuple[str, str]:
    """Choose a support level and rationale."""
    if intent == "direct_solution_request":
        return (
            "Level 1: Reflection prompt and refusal",
            "The student appears to be asking for a complete solution, so the tutor should protect academic integrity and redirect toward learning support.",
        )

    if intent == "concept_learning":
        return (
            "Level 2: Conceptual hint",
            "The student is asking to understand a concept, so the tutor should give a clear course-grounded explanation and a check-for-understanding question.",
        )

    if intent == "assignment_clarification":
        return (
            "Level 3: Strategic guidance",
            "The student is asking about assignment expectations, so the tutor should clarify goals without solving the assignment.",
        )

    if intent == "debugging_support" and effort_level in ["low_effort", "moderate_effort"]:
        return (
            "Level 1 or 2: Ask for evidence and give a conceptual hint",
            "The student named a problem but has not provided enough evidence, so the tutor should ask for the error message, line number, and relevant code.",
        )

    if intent in ["debugging_support", "high_effort_technical_help"] and effort_level == "high_effort":
        return (
            "Level 4: Targeted technical hint",
            "The student has shown effort, so the tutor can provide more specific debugging guidance without rewriting the full solution.",
        )

    if intent == "reflection_or_design_reasoning":
        return (
            "Level 1 or 3: Reflection prompt or strategic guidance",
            "The student is evaluating a design decision, so the tutor should ask them to justify their reasoning before giving stronger guidance.",
        )

    if effort_level == "non_graded_learning_request":
        return (
            "Level 6: Worked example for non-graded content",
            "A small worked example may be appropriate only when the request is clearly not for graded work.",
        )

    return (
        "Level 2 or 3: Conceptual hint or strategic guidance",
        "The student request is general, so the tutor should provide limited guidance and ask a follow-up question.",
    )


def assess_integrity_risk(intent: str, effort_level: str) -> str:
    """Assess academic-integrity risk."""
    if intent == "direct_solution_request":
        return "high"

    if effort_level == "low_effort":
        return "medium"

    if intent == "assignment_clarification":
        return "medium"

    return "low"


def make_adaptive_decision(question: str) -> AdaptiveDecision:
    """Return the full adaptive decision for a student question."""
    intent = classify_intent(question)
    effort_level = estimate_effort(question)
    support_level, rationale = select_support_level(intent, effort_level)
    integrity_risk = assess_integrity_risk(intent, effort_level)

    return AdaptiveDecision(
        intent=intent,
        effort_level=effort_level,
        support_level=support_level,
        integrity_risk=integrity_risk,
        rationale=rationale,
    )
