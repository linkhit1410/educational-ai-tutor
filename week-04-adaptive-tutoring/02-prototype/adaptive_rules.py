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
    """
    Classify what the student appears to be trying to accomplish.

    Classification uses ordered rules so that direct-solution requests
    are detected before ordinary assignment questions.
    """
    q = question.lower()

    direct_solution_terms = [
        "write my homework",
        "write my assignment",
        "write the complete",
        "complete my homework",
        "complete my assignment",
        "complete this for me",
        "give me the answer",
        "give me the full code",
        "give me complete code",
        "solve this for me",
        "do this for me",
        "answer key",
        "ready to submit",
        "so i can submit it",
        "submit it for me",
    ]

    assignment_clarification_terms = [
        "what does the assignment mean",
        "what does the homework mean",
        "what does the lab mean",
        "what does the project mean",
        "assignment requirement",
        "assignment instructions",
        "homework requirement",
        "lab requirement",
        "project requirement",
        "supposed to do",
        "required to use",
    ]

    debugging_terms = [
        "error",
        "exception",
        "nullpointer",
        "arrayindexoutofbounds",
        "cannot find symbol",
        "not working",
        "doesn't work",
        "does not work",
        "bug",
        "debug",
        "crash",
        "stack trace",
        "compiler error",
        "runtime error",
        "expected",
        "actual",
        "prints",
        "returns",
        "output",
        "stops when",
        "i traced",
        "fix it",
    ]

    concept_terms = [
        "what is",
        "explain",
        "difference between",
        "how does",
        "why does",
        "define",
        "is that correct",
        "am i correct",
        "does that mean",
        "i think",
    ]

    reflection_terms = [
        "am i on the right track",
        "does this design make sense",
        "should i use inheritance",
        "should i use composition",
        "is this a good design",
        "which design is better",
        "where should this method belong",
        "belongs in",
        "design choice",
        "tradeoff",
    ]

    technical_help_terms = [
        "my method",
        "my class",
        "my constructor",
        "overridden method",
        "superclass reference",
        "subclass object",
        "here is my code",
        "code snippet",
    ]

    # Direct requests for completed work receive the highest priority.
    if any(term in q for term in direct_solution_terms):
        return "direct_solution_request"

    # Assignment clarification is distinct from asking for completed work.
    if any(term in q for term in assignment_clarification_terms):
        return "assignment_clarification"

    # Debugging is based on evidence of incorrect behavior or errors.
    if any(term in q for term in debugging_terms):
        return "debugging_support"

    # Design reflection is narrower than simply saying "I think."
    if any(term in q for term in reflection_terms):
        return "reflection_or_design_reasoning"

    # Misconception checks and explanatory questions are concept learning.
    if any(term in q for term in concept_terms):
        return "concept_learning"

    if any(term in q for term in technical_help_terms):
        return "high_effort_technical_help"

    return "general_tutoring"

def estimate_effort(question: str) -> str:
    """
    Estimate demonstrated student effort.

    Effort is based on evidence of work, not merely phrases such as
    "my code" or "my assignment."
    """
    q = question.lower()

    direct_solution_terms = [
        "solve this",
        "give me the answer",
        "write my homework",
        "write my assignment",
        "write the complete",
        "complete this for me",
        "do this for me",
        "full code",
        "fix it",
        "so i can submit it",
        "ready to submit",
    ]

    non_graded_terms = [
        "practice example",
        "non-homework example",
        "small example",
        "made-up example",
        "not for homework",
        "not graded",
    ]

    # Requests for complete work do not demonstrate meaningful effort.
    if any(term in q for term in direct_solution_terms):
        return "low_effort"

    if any(term in q for term in non_graded_terms):
        return "non_graded_learning_request"

    evidence_groups = [
        # Evidence of an attempted action
        [
            "i tried",
            "i tested",
            "i traced",
            "i changed",
            "i wrote",
            "i created",
            "i implemented",
        ],

        # Comparison between expected and observed behavior
        [
            "expected",
            "actual",
            "instead",
            "but it",
            "prints",
            "returns",
            "output",
        ],

        # Concrete debugging evidence
        [
            "error message",
            "stack trace",
            "exception",
            "compiler error",
            "runtime error",
            "line number",
        ],

        # Student reasoning or a hypothesis
        [
            "i think",
            "i suspect",
            "my hypothesis",
            "i noticed",
            "because",
        ],

        # Evidence that relevant code was supplied
        [
            "here is my code",
            "code snippet",
            "relevant code",
            "method below",
            "class below",
        ],
    ]

    evidence_score = sum(
        1
        for group in evidence_groups
        if any(term in q for term in group)
    )

    if evidence_score >= 2:
        return "high_effort"

    if evidence_score == 1:
        return "moderate_effort"

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
    """
    Assess academic-integrity risk using both intent and effort.

    A short concept question is not automatically risky. Risk increases
    when the student requests completed work or assignment-specific help.
    """
    if intent == "direct_solution_request":
        return "high"

    if intent == "assignment_clarification":
        return "medium"

    if intent == "debugging_support" and effort_level == "low_effort":
        return "medium"

    if intent == "high_effort_technical_help":
        return "low"

    if intent in [
        "concept_learning",
        "reflection_or_design_reasoning",
        "general_tutoring",
    ]:
        return "low"

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
