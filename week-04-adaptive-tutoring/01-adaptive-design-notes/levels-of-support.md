# Week 4: Levels of Adaptive Support

## Purpose

The purpose of this document is to design different levels of support that the AI tutor can provide.

In earlier weeks, the tutor focused on answering questions using CISC 230 course materials. In Week 4, the focus shifts to adaptation. The tutor should not give every student the same amount of help. Instead, it should consider the student's intent, demonstrated effort, and learning needs.

The main question is:

How much support will help this student learn without replacing their own thinking?

---

## Why Levels of Support Matter

Students ask for help in different ways.

Some students may ask very low-effort questions, such as:

"Solve this."

Other students may show partial understanding, such as:

"I think inheritance might help here, but I'm not sure."

Other students may show significant effort, such as:

"I created an abstract superclass and three subclasses, but my overridden methods are not behaving correctly."

These students should not receive the same response. A student who has shown more effort may be ready for more specific guidance, while a student asking for a full solution should receive a refusal plus learning-oriented support.

---

# Level 1: Reflection Prompt

## Description

At this level, the tutor mainly asks the student to explain their thinking. The tutor does not provide a direct hint yet.

## When It Should Be Used

This level should be used when:

- The student has made a vague request.
- The student has not shown much effort.
- The student asks whether they are on the right track.
- The tutor needs to understand the student's reasoning first.

## Why It Is Educationally Appropriate

Reflection prompts help students become active participants in the learning process. They encourage students to explain what they know, what they tried, and where they are confused.

## When It Should Not Be Used

This level should not be used when the student is clearly stuck after showing effort. In that case, the tutor should provide a more concrete hint.

## Example

Student:  
"I think inheritance should be used here. Am I on the right track?"

Tutor strategy:  
Ask the student to explain the relationship between the classes and whether it is an is-a relationship.

---

# Level 2: Conceptual Hint

## Description

At this level, the tutor gives a small conceptual hint without giving the solution.

## When It Should Be Used

This level should be used when:

- The student asks a concept question.
- The student shows some confusion.
- The student needs help connecting the problem to a course concept.
- The student has not provided enough detail for specific code guidance.

## Why It Is Educationally Appropriate

Conceptual hints help students connect their problem to the underlying idea. This supports understanding without completing the task for them.

## When It Should Not Be Used

This level may not be enough when the student has already tried a solution and needs more specific debugging guidance.

## Example

Student:  
"What is polymorphism?"

Tutor strategy:  
Explain the concept using CISC 230 terminology, then ask the student to describe how superclass references and subclass objects are related.

---

# Level 3: Strategic Guidance

## Description

At this level, the tutor helps the student plan an approach or decide what to check next.

## When It Should Be Used

This level should be used when:

- The student has shown moderate effort.
- The student needs help organizing their next step.
- The student is debugging but has not isolated the issue yet.
- The student is working on design choices.

## Why It Is Educationally Appropriate

Strategic guidance supports problem solving. It helps students learn a process they can reuse later.

## When It Should Not Be Used

This level should not turn into a complete solution or full code.

## Example

Student:  
"My inheritance hierarchy feels wrong."

Tutor strategy:  
Ask the student to list the superclass and subclasses, identify shared fields or methods, and check whether each subclass truly has an is-a relationship with the superclass.

---

# Level 4: Targeted Technical Hint

## Description

At this level, the tutor gives a more specific hint about the likely issue, while still avoiding a full solution.

## When It Should Be Used

This level should be used when:

- The student has shown clear effort.
- The student provides an error message or code snippet.
- The tutor can identify a likely misconception.
- The student needs a specific next debugging step.

## Why It Is Educationally Appropriate

Students who show effort may benefit from more detailed guidance because they have already engaged with the problem. This level rewards productive effort while still preserving learning.

## When It Should Not Be Used

This level should not be used for low-effort requests like "write my assignment."

## Example

Student:  
"I created a superclass and three subclasses. My overridden methods are not behaving correctly."

Tutor strategy:  
Ask the student to compare the method signatures and check whether the method name, return type, and parameters match the superclass method.

---

# Level 5: Structural Guidance or Pseudocode

## Description

At this level, the tutor may provide structure, steps, or pseudocode, but not full assignment code.

## When It Should Be Used

This level should be used carefully when:

- The student has shown substantial effort.
- The work is not a graded assignment solution.
- The student needs help organizing logic.
- The tutor can support planning without writing final code.

## Why It Is Educationally Appropriate

Pseudocode can help students understand structure while still requiring them to write and understand the actual implementation.

## When It Should Not Be Used

This level should not be used when:

- The student asks for full homework code.
- The task is clearly graded.
- The response would remove the student’s responsibility to solve the problem.

## Example

Student:  
"I understand the concept, but I do not know how to organize the steps."

Tutor strategy:  
Provide a high-level outline or pseudocode and ask the student to translate it into Java.

---

# Level 6: Worked Example for Non-Graded Content

## Description

At this level, the tutor may explain a complete worked example only when it is clearly not the student’s graded assignment.

## When It Should Be Used

This level should be rare. It may be appropriate when:

- The example is not part of a graded assignment.
- The example is small and instructional.
- The goal is to demonstrate a general concept.
- The tutor clearly separates the example from the student’s own work.

## Why It Is Educationally Appropriate

Worked examples can support learning when they are used for concept demonstration rather than assignment completion.

## When It Should Not Be Used

This level should not be used for:

- Homework solutions.
- Lab solutions.
- Test questions.
- Student requests to complete graded work.

## Example

Student:  
"Can you show a small non-homework example of method overriding?"

Tutor strategy:  
Provide a short conceptual example only if allowed by course policy and then ask the student to explain what makes it overriding.

---

# Summary Table

| Support Level | Type of Help | Best For | Risk Level |
|---|---|---|---|
| Level 1 | Reflection prompt | Low detail or design reflection | Low |
| Level 2 | Conceptual hint | Concept learning | Low |
| Level 3 | Strategic guidance | Planning and design | Medium |
| Level 4 | Targeted technical hint | Debugging after effort | Medium |
| Level 5 | Structural guidance or pseudocode | High-effort planning | Higher |
| Level 6 | Worked example | Non-graded concept learning only | Highest |

---

# Main Takeaway

Adaptive tutoring means choosing the right amount of help for the student’s situation.

The tutor should provide less direct help when the student shows low effort or asks for a full answer. It can provide more specific guidance when the student demonstrates effort, shares their reasoning, or provides evidence such as code, an error message, or a design attempt.

The goal is to support learning while protecting academic integrity.
