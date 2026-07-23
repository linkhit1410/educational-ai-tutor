# Week 3 Tutoring Scenario Analysis

## Purpose

The purpose of this analysis is to test whether the tutor can respond differently to different types of student questions.

A useful educational tutor should not use the same response style for every question. Concept questions, debugging questions, assignment clarification questions, and reflection questions each require a different tutoring approach.

---

## Scenario 1: Concept Learning

### Example Question

What is inheritance?

### Detected Scenario

concept_learning

### Retrieved Course Materials

The tutor retrieved CISC 230 materials from:

- `concepts/oop_concepts.txt`
- `lectures/chapter-9.txt :: Slide 2`
- `lectures/chapter-9.txt :: Slide 4`
- `lectures/chapter-9.txt :: Slide 5`

These materials were relevant because Chapter 9 focuses on inheritance and explains superclass, subclass, parent class, child class, reusable classes, and the is-a relationship.

### Observation

The retrieval system worked much better after switching from whole-file retrieval to chunk-based retrieval. Before this change, the tutor retrieved almost an entire lecture file when only one word matched. After the change, the tutor retrieved specific slide chunks from Chapter 9.

The response was mostly correct and course-related, but at first the tutor still added outside examples such as houses, vehicles, and cars. This showed that retrieval alone does not fully control the model’s behavior.

### What Worked Well

- The tutor detected the question as concept learning.
- The retrieved materials were relevant to inheritance.
- The response used important course terms such as superclass, subclass, parent class, child class, and is-a relationship.
- The response included a check-for-understanding question.

### What Needs Improvement

- The tutor should avoid outside examples unless they appear in the retrieved course materials.
- The response should stay more tightly grounded in the retrieved slides.
- The tutor should ask students to explain the idea in their own words instead of offering extra examples.

### Educational Value

This scenario supports learning because it helps students understand a core Java/OOP concept using CISC 230 terminology. It also shows why course grounding and strict tutoring behavior are both necessary.

---

## Scenario 2: Concept Learning

### Example Question

What is polymorphism?

### Expected Detected Scenario

concept_learning

### Expected Tutoring Strategy

For a polymorphism question, the tutor should explain the concept using CISC 230 materials, especially Chapter 10 and the polymorphism case study. It should focus on ideas such as polymorphic references, dynamic binding, inheritance, interfaces, and method calls through shared types.

### Observation

The retrieval test showed that the system can retrieve relevant polymorphism materials, including:

- `concepts/oop_concepts.txt`
- `lectures/polymorphism-case-study.txt`
- `lectures/chapter-10.txt`

This is promising because polymorphism is a difficult concept for beginning Java students. The tutor should be especially careful to avoid adding unsupported examples and should use the course’s terminology.

### What Worked Well

- Relevant polymorphism files were found.
- The tutor has access to both general concept notes and professor lecture material.
- The polymorphism case study can help support more advanced questions about variable type, object type, casting, and method calls.

### What Needs Improvement

- More testing is needed in the Streamlit app.
- The tutor should be evaluated for whether it explains polymorphism clearly without overwhelming the student.
- The tutor should avoid giving examples that are not in the retrieved materials.

### Educational Value

Polymorphism is difficult because students must understand the difference between reference type and object type. A good tutor response should guide students carefully and ask them to reason about which method is called and why.

---

## Scenario 3: Assignment Clarification

### Example Question

What concepts does Homework 2 focus on?

### Expected Detected Scenario

assignment_clarification

### Expected Tutoring Strategy

For assignment clarification, the tutor should help the student understand the assignment goals and relevant concepts. It should not complete the assignment or provide full solution code.

The tutor should respond by:

- Identifying the concepts involved.
- Clarifying requirements.
- Suggesting how the student can break down the task.
- Asking what part of the assignment is confusing.
- Avoiding full solutions.

### Observation

This scenario still needs more testing with actual assignment materials. The current tutor can detect assignment-related wording, but the quality of the response depends on whether safe assignment descriptions or policies are included in the course materials.

### What Worked Well

- The prototype has an assignment clarification scenario.
- The prompt includes rules against completing homework solutions.
- The system can be extended to retrieve safe assignment descriptions.

### What Needs Improvement

- The tutor should only use assignment materials that the professor approves.
- Homework solutions or answer keys should not be included in retrieval.
- The tutor should distinguish clarification from solution generation.

### Educational Value

Assignment clarification can support academic integrity when handled carefully. The tutor can help students understand what they are being asked to do without doing the work for them.

---

## Scenario 4: Debugging Support

### Example Question

Why am I getting a NullPointerException?

### Expected Detected Scenario

debugging

### Expected Tutoring Strategy

For debugging questions, the tutor should not immediately give fixed code. Instead, it should help the student understand the cause of the error and guide them through the debugging process.

The tutor should ask about:

- The error message.
- The line number.
- The object or variable involved.
- What the student expected to happen.
- What actually happened.

### Observation

The prototype includes a debugging scenario, but more testing is needed with common Java errors. The tutor should help students understand why the problem occurred instead of simply identifying the bug.

### What Worked Well

- Debugging keywords are included in scenario detection.
- The tutoring strategy tells the model not to immediately give fixed code.
- The tutor can potentially use course materials about errors, exceptions, objects, and references.

### What Needs Improvement

- The tutor should ask for the student’s code or error message when needed.
- The tutor should guide students step by step.
- The tutor should avoid rewriting full solutions.

### Educational Value

Debugging is a major learning opportunity in programming. A good debugging tutor helps students develop problem-solving skills by teaching them how to inspect evidence, form hypotheses, and test their understanding.

---

## Scenario 5: Reflection

### Example Question

I think inheritance should be used here. Am I on the right track?

### Expected Detected Scenario

reflection

### Expected Tutoring Strategy

For reflection questions, the tutor should not simply say yes or no. It should ask the student to justify their thinking and compare possible design choices.

The tutor should ask questions such as:

- What is the relationship between the classes?
- Is this really an is-a relationship?
- Would composition or aggregation be more appropriate?
- What shared behavior belongs in the superclass?
- What behavior should remain specific to the subclass?

### Observation

The prototype includes a reflection scenario. This is important because object-oriented design often requires judgment, not just memorization. The tutor should help students reason about design choices instead of making the decision for them.

### What Worked Well

- Reflection keywords are included in scenario detection.
- The tutor strategy encourages independent thinking.
- This scenario connects well to Chapter 7 object-oriented design and Chapter 9 inheritance.

### What Needs Improvement

- More testing is needed with realistic design questions.
- The tutor should avoid making final design decisions too quickly.
- The tutor should ask the student to explain their reasoning.

### Educational Value

Reflection questions help students become more independent programmers. Instead of only asking “what is the answer,” students learn to evaluate whether a design choice makes sense.

---

## Overall Findings

This scenario analysis shows that different student questions require different tutoring behavior.

Concept-learning questions need clear explanations and check-for-understanding questions.

Debugging questions need step-by-step diagnosis and reasoning support.

Assignment clarification questions need academic-integrity safeguards.

Reflection questions need prompts that encourage students to justify their thinking.

The current tutor now has the basic structure to support these scenarios, but more testing is needed. The strongest current scenario is concept learning because it has already been tested with inheritance and polymorphism retrieval. Debugging, assignment clarification, and reflection should be tested more deeply next.

---

## Main Takeaway

A useful AI tutor should not respond to every student question in the same way. Tutoring quality depends on matching the response strategy to the student’s need.

The Week 3 prototype begins to support this by detecting tutoring scenarios and using different response strategies. This is an important step toward making the system educationally helpful rather than simply informative.
