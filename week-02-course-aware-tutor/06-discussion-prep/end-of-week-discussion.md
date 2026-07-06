# Week 2 End-of-Week Discussion Prep

## Main Week 2 Message

The main thing I learned this week is that retrieval can help transform a generic chatbot into a course-aware learning assistant.

However, retrieval alone is not enough. The tutor still needs careful course-material selection, stronger prompting, academic-integrity rules, and evaluation.

---

## 1. Why is retrieval important in educational AI?

Retrieval is important because educational AI should not rely only on the model’s general knowledge. A general model may give answers that are technically correct but disconnected from the course.

In education, the tutor should understand:

- Course vocabulary
- Instructor expectations
- Assignment structure
- Current course topics
- Academic-integrity policies

In our project, retrieval allows the tutor to search selected CISC230 materials before answering. This helps the tutor respond in a way that is more aligned with the course.

Our system changed from:

Student question → AI model

to:

Student question → retrieved CISC230 material → AI model → course-aware response

---

## 2. Did retrieval improve the tutor?

Yes, retrieval improved the tutor at the initial prototype level.

Example:

Question:
What is inheritance?

Without retrieval:
The tutor gave a correct but generic answer.

With retrieval:
The tutor retrieved course context from `oop_concepts.txt` and used terms such as:

- superclass
- subclass
- shared behavior
- override
- reuse fields and methods

This made the response more course-aligned and educationally useful.

Main finding:
Retrieval helped the tutor sound less like a generic chatbot and more like a course-aware teaching assistant.

---

## 3. Did retrieval introduce any new risks?

Yes. Retrieval introduced new risks.

The biggest risk is solution leakage. If the tutor has access to unsafe documents, such as answer keys or completed homework solutions, it could accidentally reveal assignment answers.

Another risk is that retrieval does not fully prevent hallucinations. During the polymorphism test, the tutor retrieved correct context but initially generated an unsupported example and implied it came from course materials. This showed that even grounded responses still need careful prompting and evaluation.

Main finding:
Retrieval improves grounding, but it also makes document selection more important.

Possible document categories:

Safe:
- Syllabus
- Course policies
- Lecture notes
- Concept explanations

Caution:
- Homework descriptions
- Rubrics
- Starter code
- Lab instructions

Restricted:
- Solutions
- Answer keys
- Previous student submissions
- Completed assignments

---

## 4. How should the tutor handle assignment-related questions?

The tutor should support learning without completing the assignment for the student.

For general concept questions:
The tutor can explain concepts, give small examples, and ask follow-up questions.

For debugging questions:
The tutor should ask what the student tried, help interpret errors, and guide the student step by step.

For assignment clarification:
The tutor can explain requirements, summarize expectations, and suggest a plan.

For complete solution requests:
The tutor should politely refuse to provide full code or a full answer. Then it should offer hints, conceptual help, or a step-by-step approach.

Example policy:

If a student asks:
“Can you write my assignment for me?”

The tutor should respond:
“I can’t write the complete assignment for you, but I can help you understand the requirements, break the task into smaller steps, or debug the code you have started.”

---

## 5. What educational behaviors should be added next?

The next educational behaviors could include:

- Stronger Socratic questioning
- Hint levels
- Asking students what they already tried
- Debugging support
- Reflection prompts
- Assignment-specific guardrails
- Better refusal behavior for full-solution requests
- Source-aware responses
- More transparent uncertainty

A useful next feature would be hint levels:

Level 1: Ask a guiding question  
Level 2: Give a conceptual hint  
Level 3: Give pseudocode or a partial example  
Level 4: Help debug student-written code  

This would make the tutor more like a real tutor instead of a direct answer generator.

---

# What Success Looks Like

## 1. Explain why retrieval matters

I can explain that retrieval matters because it grounds the tutor in course materials instead of relying only on general model knowledge.

## 2. Demonstrate a course-aware tutor

I can demonstrate the Streamlit prototype with retrieval turned on. The app retrieves relevant CISC230 context and uses it in the tutor response.

## 3. Compare grounded and ungrounded responses

I compared responses with retrieval off and retrieval on.

Example:
“What is inheritance?”

Retrieval off:
Generic explanation.

Retrieval on:
Course-aware explanation using retrieved CISC230 vocabulary.

## 4. Discuss academic-integrity implications

I can explain that retrieval makes the tutor more helpful but also more risky if unsafe documents are included. The tutor should not retrieve or reveal solutions, answer keys, or completed assignments.

## 5. Connect technical decisions to educational goals

Technical decision:
Use retrieval from course materials.

Educational goal:
Make the tutor more aligned with CISC230 and more useful for learning.

Technical decision:
Add academic-integrity rules to the prompt.

Educational goal:
Help students learn without giving away complete homework solutions.

Technical decision:
Show retrieved context in the app.

Educational goal:
Make the tutor’s answer easier to inspect and evaluate.

---

# Final Week 2 Reflection Point

The goal of Week 2 was not to build a perfect retrieval system. The goal was to understand how educational context changes tutor behavior.

My main takeaway is:

Retrieval improves course alignment, but it does not automatically make the tutor educationally safe. A course-aware tutor still needs safe document selection, strong prompting, academic-integrity policies, and careful evaluation.
