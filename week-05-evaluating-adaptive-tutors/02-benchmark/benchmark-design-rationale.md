# Benchmark Design Rationale

## Purpose of the Benchmark

The Week 5 benchmark is designed to evaluate how three tutoring systems respond to realistic CISC 230 student interactions.

The benchmark will be applied consistently to:

1. a general-purpose language model,
2. a course-aware tutor,
3. and an adaptive tutor.

Its purpose is not merely to test whether the systems can produce correct answers. It is designed to examine whether they provide educationally appropriate support, align with course expectations, respond to student effort, encourage independent reasoning, and maintain academic-integrity boundaries.

## Benchmark Size

The benchmark will contain 24 tutoring scenarios.

Each scenario will be submitted to all three tutoring systems, producing:

* 24 general-purpose responses,
* 24 course-aware responses,
* and 24 adaptive-tutor responses.

This creates a total of 72 responses for evaluation.

A 24-scenario benchmark is large enough to reveal patterns across categories while remaining manageable for manual scoring and qualitative analysis during Week 5.

## Scenario Categories

The benchmark includes six categories required by the Week 5 evaluation plan.

Each category contains four scenarios.

| Category                        | Number of scenarios |
| ------------------------------- | ------------------: |
| Concept learning                |                   4 |
| Debugging support               |                   4 |
| Assignment clarification        |                   4 |
| Reflection and design reasoning |                   4 |
| Direct solution requests        |                   4 |
| Mixed or ambiguous situations   |                   4 |
| **Total**                       |              **24** |

## Category Rationale

### 1. Concept Learning

Concept-learning prompts evaluate whether a tutor can explain programming ideas accurately and educationally.

These scenarios may include topics such as:

* classes and objects,
* inheritance,
* polymorphism,
* abstract classes,
* and method overriding.

This category is necessary because concept explanation is one of the most common uses of an educational tutor.

A strong response should do more than define a term. It should help the student connect ideas, understand why the concept matters, and reason about examples.

### 2. Debugging Support

Debugging scenarios evaluate whether the tutor helps students investigate errors without immediately rewriting their program.

These scenarios may include:

* compiler errors,
* runtime exceptions,
* incorrect output,
* problems with inheritance or overriding,
* and code that does not behave as expected.

Debugging is especially important because students may provide different amounts of evidence.

Some may only say that their code does not work, while others may provide:

* code excerpts,
* error messages,
* attempted fixes,
* predicted behavior,
* and observed output.

This category allows the evaluation to test whether the adaptive tutor recognizes demonstrated effort and provides appropriately targeted support.

### 3. Assignment Clarification

Assignment-clarification scenarios evaluate whether the tutor can help students understand instructions, requirements, terminology, or expected program behavior without completing the assignment.

These prompts may ask:

* what an assignment requirement means,
* how to interpret a phrase in the instructions,
* which concepts are relevant,
* or how to break the assignment into smaller steps.

This category is included because assignment questions are not always requests for solutions. A tutor should distinguish legitimate clarification from requests to complete assessed work.

### 4. Reflection and Design Reasoning

Reflection and design scenarios evaluate whether the tutor encourages students to explain and justify their programming choices.

These prompts may involve:

* choosing between inheritance and composition,
* evaluating a class hierarchy,
* comparing two implementation strategies,
* identifying tradeoffs,
* or reflecting on why a design behaves in a certain way.

This category is important because educational tutoring should support reasoning, not only factual recall or code correction.

### 5. Direct Solution Requests

Direct-solution prompts explicitly ask the tutor to produce completed homework, assignment code, or answers that the student could submit.

These scenarios are necessary for evaluating academic-integrity safeguards.

A strong tutoring response should:

* refuse to complete the assessed work,
* explain the boundary briefly,
* redirect the student toward a learning-oriented next step,
* and still provide a useful way to begin.

A response may be safe but educationally weak if it refuses without offering meaningful support. Therefore, both safety and helpfulness must be evaluated.

### 6. Mixed or Ambiguous Situations

Mixed or ambiguous prompts contain incomplete, conflicting, or uncertain signals about student intent and effort.

Examples may include:

* a student asking for help while providing only part of an assignment,
* a request that could be either conceptual or solution-seeking,
* a debugging question without enough technical evidence,
* or a student who shows some work but also requests the final answer.

This category is included because real student interactions do not always fit cleanly into one category.

These scenarios test whether the tutor handles uncertainty carefully instead of making overly confident assumptions.

## Effort-Level Distribution

The benchmark will include low-, moderate-, and high-effort interactions.

| Effort level    | Target number of scenarios |
| --------------- | -------------------------: |
| Low effort      |                          8 |
| Moderate effort |                          8 |
| High effort     |                          8 |
| **Total**       |                     **24** |

### Low Effort

Low-effort prompts provide little or no evidence that the student has attempted the problem.

Examples include:

* asking for a complete answer,
* stating that something does not work without details,
* requesting an explanation without identifying the confusing part,
* or pasting an assignment prompt with no attempt.

### Moderate Effort

Moderate-effort prompts show some engagement but provide incomplete reasoning or evidence.

Examples include:

* describing an attempted approach,
* identifying a likely problem,
* sharing a partial code excerpt,
* or asking for help with one stage of a larger task.

### High Effort

High-effort prompts provide meaningful evidence of student work.

Examples include:

* sharing relevant code and an exact error message,
* explaining expected and observed behavior,
* listing attempted fixes,
* giving a hypothesis,
* or asking a focused question after substantial progress.

Balanced effort levels are important because effort adaptation is a central feature of the adaptive tutor.

## Academic-Integrity Risk Distribution

Each scenario will also receive an academic-integrity risk label.

The labels are:

* low,
* medium,
* high.

### Low Risk

Low-risk prompts focus on general concept learning, reflection, or debugging that is not clearly connected to completing assessed work.

### Medium Risk

Medium-risk prompts may relate to an assignment but primarily request clarification, limited guidance, or feedback on an attempted solution.

### High Risk

High-risk prompts ask for completed code, final answers, or substantial portions of work that could be submitted directly.

The direct-solution category will primarily contain high-risk scenarios. Other categories may contain low- or medium-risk scenarios depending on the wording and context.

## Intended Support Levels

The benchmark will record an expected support level for each scenario.

The support levels are based on the Week 4 adaptive tutoring framework:

* **Level 1:** refusal, reflection prompt, or evidence request,
* **Level 2:** conceptual hint,
* **Level 3:** strategic guidance,
* **Level 4:** targeted technical hint.

The expected support level will not represent one exact required response. Instead, it will describe the approximate amount and type of assistance that would be educationally appropriate.

## Scenario Metadata

Each benchmark scenario will include the following fields:

| Field                    | Purpose                                                |
| ------------------------ | ------------------------------------------------------ |
| `scenario_id`            | Provides a unique identifier                           |
| `category`               | Identifies the tutoring situation                      |
| `student_prompt`         | Contains the exact input sent to each system           |
| `effort_level`           | Labels demonstrated effort as low, moderate, or high   |
| `integrity_risk`         | Labels academic-integrity risk as low, medium, or high |
| `expected_support_level` | Records the approximate appropriate support level      |
| `expected_behavior`      | Describes important qualities of a strong response     |
| `course_topic`           | Identifies the relevant CISC 230 topic                 |
| `notes`                  | Records design or evaluation considerations            |

These fields will support consistent scoring and later analysis.

## Benchmark Balance

The benchmark will be considered reasonably balanced when:

* all six categories contain four scenarios,
* low-, moderate-, and high-effort prompts are represented,
* low-, medium-, and high-integrity-risk situations are represented,
* both conceptual and code-related questions are included,
* assignment-related and non-assignment-related prompts are included,
* and prompts vary in specificity and difficulty.

Perfect statistical balance is not required for this small exploratory study. However, major categories and risk conditions should not be represented by only one isolated example.

## Realism

The scenarios will be written to resemble questions that CISC 230 students might realistically ask.

Prompts will vary in style. Some will be complete and carefully written, while others may be short, informal, uncertain, or incomplete.

This variation is intentional because real tutoring interactions do not always use precise academic language.

## Consistency Across Systems

The exact same student prompt will be submitted to each tutoring system.

The prompts will not be rewritten to make one system perform better.

Responses will be saved without editing before evaluation. If a system fails, returns no response, or produces an error, that outcome will be documented.

## Benchmark Limitations

The benchmark has several limitations:

* It contains researcher-created scenarios rather than a large collection of authentic student conversations.
* Twenty-four scenarios cannot represent every possible tutoring interaction.
* Scenario labels involve human judgment.
* Some categories may overlap.
* Prompt wording may influence system behavior.
* A system may behave differently across repeated generations.

These limitations will be considered when interpreting the results.

## Expected Evaluation Value

The benchmark should make it possible to determine whether performance differences appear consistently across multiple situations.

In particular, it will help evaluate whether the adaptive tutor:

* responds more appropriately to demonstrated effort,
* better distinguishes learning requests from solution requests,
* provides useful guidance without excessive disclosure,
* remains aligned with course materials,
* and supports independent student reasoning.
