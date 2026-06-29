# Local Model Observations

## Overview

For this exploration, I tested a local language model using Ollama. I asked beginner-level Java questions to see whether the model behaved more like a tutor or more like a general chatbot. I focused on three areas: explaining a concept, helping with debugging, and responding to a request for a complete homework solution.

---

## Test 1: Inheritance in Java

### Question Asked

What is inheritance in Java? Explain it like you are tutoring a beginner.

### Summary of Model Output

The model explained inheritance as a way to create a new class based on an existing class. It described the existing class as the superclass or parent class and the new class as the subclass or child class. It used a family-tree analogy and gave an example with an `Animal` class and a `Dog` class.

### Observation

This response was helpful because it explained inheritance in beginner-friendly language and connected the concept to code. The model used an analogy, explained important vocabulary, and gave an example. However, the code example also included a technical mistake. It created an `Animal` reference to a `Dog` object and then tried to call `animal.bark()`, even though `bark()` is not defined in the `Animal` class. This would cause an error in Java. This shows that the model can explain concepts clearly, but its code examples still need to be checked carefully.

---

## Test 2: NullPointerException

### Question Asked

Why am I getting a NullPointerException in Java? Explain it like you are helping me debug, not just giving me the answer.

### Summary of Model Output

The model explained that a NullPointerException happens when a program tries to use an object reference that is `null`. It suggested debugging steps such as identifying the line of code causing the exception, checking variable declarations, inspecting object references, and looking at the stack trace. It also asked the student to share their code snippet.

### Observation

This response felt more like tutoring because it did not immediately give one final answer. Instead, it encouraged the student to debug and think through the problem. I liked that it asked for the code snippet and stack trace because that makes the interaction more specific and helpful. However, the example it gave had technical problems. It claimed that printing a null `String` field would likely cause a NullPointerException, but Java would usually print `null` instead. It also tried to access a private field directly from another class, which would cause a compile error. This shows that the model can guide students in a useful way, but it can also make mistakes that beginners might not notice.

---

## Test 3: Homework Solution Request

### Question Asked

Can you write my Java homework assignment for me? I need a complete solution with code.

### Summary of Model Output

The model first said that it could not provide a complete homework solution and would instead guide the student through the process. However, immediately after saying that, it gave a complete Java program for a sample banking assignment.

### Observation

This was one of the most important results. The model appeared to support academic integrity at first because it said it would not give a complete solution. However, it still provided a full program that a student could copy. This shows that a general language model may not be reliable as an educational tutor without stronger design rules. For this project, an AI tutor should avoid giving complete assignment solutions. Instead, it should ask what the student has tried, give small hints, explain concepts, and guide the student step by step.

---

## Overall Reflection

Using Ollama helped me understand both the strengths and limitations of local language models in programming education. The model was useful for explanations, examples, and general debugging advice. However, it also made technical mistakes and sometimes gave too much help. These observations suggest that simply running a local model is not enough to create a good AI tutor. A stronger educational AI tutor needs to be designed to support learning, encourage independent thinking, check for understanding, and avoid giving complete assignment answers.
