# Week 4: Student Intent Categories

## Purpose

The purpose of this document is to categorize different types of student requests.

In adaptive tutoring, the tutor should not only identify the topic. It should also ask:

What is the student trying to accomplish?

A student asking "What is polymorphism?" needs a different response from a student asking "Can you write my assignment?" Even if both questions are related to programming, they show different intent, effort, and academic-integrity risk.

---

# Category 1: Concept Learning

## Example Questions

- What is polymorphism?
- What is inheritance?
- What is an interface?
- What is exception handling?

## Student Intent

The student is trying to understand a course concept.

## Appropriate Tutor Response

The tutor should provide a clear, course-grounded explanation using CISC 230 materials. The response should be concise and should include a check-for-understanding question.

## Support Level

Level 2: Conceptual Hint

## Why This Promotes Learning

This helps students build foundational understanding without overwhelming them or giving away assignment solutions.

---

# Category 2: Assignment Clarification

## Example Questions

- What does Homework 3 require?
- What concepts does this assignment focus on?
- Am I supposed to use inheritance here?
- What is this lab asking me to practice?

## Student Intent

The student is trying to understand the assignment requirements or the concepts involved.

## Appropriate Tutor Response

The tutor should clarify the assignment goal, identify relevant course concepts, and help the student plan next steps. It should not write the solution or provide full code.

## Support Level

Level 3: Strategic Guidance

## Why This Promotes Learning

This helps students understand what they are being asked to do while preserving their responsibility to complete the work.

---

# Category 3: Debugging Support

## Example Questions

- Why am I getting a NullPointerException?
- Why does my loop go out of bounds?
- Why am I getting cannot find symbol?
- My overridden method is not being called. What should I check?

## Student Intent

The student is trying to understand and fix an error.

## Appropriate Tutor Response

The tutor should guide the student through the debugging process. It should ask for the error message, line number, relevant code, expected behavior, and actual behavior. It should explain the underlying concept behind the error.

## Support Level

Level 3 or Level 4, depending on effort.

## Why This Promotes Learning

Debugging helps students learn how Java works. The tutor should help students reason through evidence instead of simply correcting the code.

---

# Category 4: Reflection or Design Reasoning

## Example Questions

- I think inheritance should be used here. Am I on the right track?
- Should this method belong in the superclass or subclass?
- Is this a good object-oriented design?
- Does this relationship seem like an is-a relationship?

## Student Intent

The student is trying to evaluate a design decision.

## Appropriate Tutor Response

The tutor should ask the student to explain their reasoning and compare design options. It should not make the final decision immediately.

## Support Level

Level 1 or Level 3

## Why This Promotes Learning

Reflection helps students become more independent programmers. It encourages them to justify design choices instead of relying on the tutor to decide.

---

# Category 5: Direct Solution Request

## Example Questions

- Can you write my Homework 3?
- Solve this assignment.
- Give me the full code.
- What is the answer?

## Student Intent

The student appears to be asking the tutor to complete the work for them.

## Appropriate Tutor Response

The tutor should refuse to provide a complete solution. It should redirect the student toward learning support by offering to explain the relevant concept, give a hint, or help break down the problem.

## Support Level

Level 1 or Level 2

## Why This Promotes Learning

This protects academic integrity and prevents the tutor from replacing the student's learning process.

---

# Category 6: High-Effort Technical Help

## Example Questions

- I created an abstract superclass and three subclasses, but my overridden methods are not behaving correctly.
- I tried using an ArrayList, but my loop skips one element.
- I wrote my constructor, but the fields are still not initialized correctly.
- I tested my method with two inputs, but one case fails.

## Student Intent

The student has already attempted the work and needs specific guidance.

## Appropriate Tutor Response

The tutor can provide more targeted help because the student has shown effort. It should still avoid completing the full solution, but it can help identify the likely concept or next debugging step.

## Support Level

Level 4 or Level 5

## Why This Promotes Learning

Students who show effort may be ready for more specific feedback. This rewards productive struggle while still requiring the student to do the final reasoning and implementation.

---

# Summary Table

| Intent Category | Student Goal | Tutor Strategy | Support Level |
|---|---|---|---|
| Concept Learning | Understand a concept | Explain using course materials | Level 2 |
| Assignment Clarification | Understand requirements | Clarify and guide planning | Level 3 |
| Debugging Support | Fix and understand an error | Ask diagnostic questions | Level 3 or 4 |
| Reflection | Evaluate reasoning | Ask student to justify choices | Level 1 or 3 |
| Direct Solution Request | Get the answer/code | Refuse and redirect | Level 1 or 2 |
| High-Effort Technical Help | Improve attempted work | Give targeted guidance | Level 4 or 5 |

---

# Main Takeaway

Student intent matters because the same programming topic can require different tutoring behavior.

A question about inheritance could be a concept-learning question, an assignment clarification question, a debugging question, or a design reflection question. The tutor should adapt based on what the student is trying to accomplish and how much effort the student has shown.
