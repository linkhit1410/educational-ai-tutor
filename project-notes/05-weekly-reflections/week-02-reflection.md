# Week 2 Reflection: Building a Course-Aware AI Tutor

## Week 2 Focus

During Week 2, I focused on making the AI tutor course-aware. In Week 1, the prototype could answer general programming questions, but it did not understand a specific course, instructor expectations, assignment structure, or course vocabulary.

The main goal of Week 2 was to explore how course materials can ground the tutor’s responses. Instead of sending the student question directly to the model, I changed the system so the tutor first retrieves relevant CISC230 course material and then uses that context when generating a response.

The system changed from:

Student question → AI model → tutor response

to:

Student question → retrieved course material → AI model → course-aware tutor response

This helped me understand how retrieval can transform a generic chatbot into the beginning of a course-aware learning assistant.

---

# Educational Objectives

## 1. Explain why educational grounding is important

Educational grounding is important because a programming answer can be technically correct but still not appropriate for a specific course. A general AI model may explain a concept using unfamiliar vocabulary, a different programming language, advanced ideas students have not learned yet, or advice that does not match the instructor’s expectations.

In this project, educational grounding means giving the tutor access to selected CISC230 materials before it answers. This helps the tutor respond in a way that is more connected to the course.

For example, when I asked:

What is inheritance?

Without retrieval, the tutor gave a correct but generic explanation. It used a general analogy and a Vehicle/Car example. The answer was understandable, but it did not feel connected to CISC230 specifically.

With retrieval, the tutor found course context from `oop_concepts.txt`:

Inheritance allows one class to reuse fields and methods from another class.  
The superclass contains shared behavior, and the subclass can add or override behavior.

Then the tutor used course-related terms such as superclass, subclass, shared behavior, override, and reuse fields and methods.

This showed me that grounding improves course alignment. The tutor becomes more useful educationally because it can connect its explanation to the way the course presents the concept.

## 2. Discuss the risks of hallucinations in educational systems

Hallucinations are risky in educational systems because students may trust an answer simply because it sounds confident. If a tutor gives incorrect or unsupported information, students might learn the wrong concept, follow incorrect instructions, or believe something came from the course when it did not.

I saw this risk during the polymorphism test. The retrieval system found the correct course context:

Polymorphism allows code to work with objects of different classes through a shared type.  
For example, a method may accept a superclass type while receiving subclass objects.

However, the model initially generated a C++ example and implied that the example came from the course materials. This was a problem because the retrieved context did not include that example. Also, if CISC230 expects Java, then a C++ example is not course-aligned.

This was an important finding because it showed that retrieval helps, but it does not completely prevent hallucinations. The model can still add unsupported examples or make claims beyond the retrieved material.

To improve this, I updated the course-aware prompt. I added instructions telling the tutor not to claim that an example, phrase, or requirement comes from the course materials unless it appears in the retrieved context. After this improvement, the tutor gave a Java example and did not falsely claim that the example came from the course materials.

This taught me that retrieval and prompting must work together. Retrieval provides context, but the prompt still has to control how the model uses that context.

## 3. Describe how course context influences learning support

Course context influences learning support because students need help that fits their current course, not just a general explanation. A tutor should understand what concepts students are learning, what vocabulary the course uses, what level of detail is appropriate, and what assignments or policies matter.

In my prototype, course context influenced the tutor by giving it relevant CISC230 material before answering. This changed the tutor’s behavior in several ways:

- It used vocabulary from the course materials.
- It gave responses that were more aligned with CISC230.
- It had less need to guess about course concepts.
- It became easier to compare course-aware and generic answers.

For example, the inheritance response with retrieval focused on superclass, subclass, reuse, shared behavior, and overriding. These terms matched the retrieved course material. This made the answer more educationally useful because it supported the student using the same language they are likely seeing in the course.

This showed me that course-aware support is not only about correctness. It is also about level, timing, vocabulary, and alignment with what students are expected to learn.

## 4. Reflect on the relationship between tutoring and academic integrity

Tutoring and academic integrity are closely connected. A good tutor should help students learn, but it should not replace the student’s own work.

A tutor can support learning by:

- Explaining concepts
- Asking guiding questions
- Giving hints
- Helping students debug step by step
- Suggesting a plan
- Encouraging students to explain what they tried

But a tutor should avoid:

- Writing complete homework solutions
- Providing full assignment code
- Revealing answer keys
- Completing the work for the student

Retrieval makes academic integrity more complicated. If the tutor retrieves lecture notes, course policies, rubrics, or assignment descriptions, it can give better support. However, if the tutor retrieves solutions, answer keys, or completed examples, it could accidentally leak answers.

Because of this, course-aware tutoring needs document safety rules. Some documents may be safe, some may need caution, and some should be excluded completely.

My current prototype includes a course policy file that tells the tutor not to provide complete homework solutions or full assignment code. The prompt also tells the tutor to refuse full solution requests and instead offer conceptual help, hints, or a step-by-step plan.

My main reflection is that academic integrity cannot be handled only by saying “be helpful.” The tutor needs specific policies for different types of student questions.

For example:

General concept question:
“What is polymorphism?”
The tutor can explain the concept and give a small example.

Assignment-specific request:
“Write my Homework 2 code.”
The tutor should refuse to provide the full solution and instead offer hints or a plan.

Debugging question:
“My code gives an error.”
The tutor should ask what the student tried and help debug step by step.

---

# Technical Objectives

## 1. Organize and prepare course materials for AI use

I completed an initial version of this objective.

I created a dedicated course-materials folder:

week-02-course-aware-tutor/01-course-materials/

Inside that folder, I added sample CISC230-style materials:

- course_policies.txt
- oop_concepts.txt

The materials were saved as plain text files so the retrieval system could read them easily.

The course policy file included tutoring rules such as not providing complete homework solutions or full assignment code. The OOP concepts file included definitions for class, object, inheritance, and polymorphism.

This was an initial preparation step. I used safe sample materials first because I still need professor guidance on which real CISC230 materials are approved to include.

## 2. Build an initial retrieval-based system

I completed this objective by building `retrieval.py`.

The retrieval system:

- Loads text files from the course-materials folder
- Splits the files into paragraph chunks
- Cleans and compares words from the student question and course chunks
- Scores chunks using keyword overlap
- Returns the most relevant course context

I tested the retrieval system in Terminal with:

python -c "from retrieval import retrieve_context; print(retrieve_context('What is inheritance?'))"

The system correctly returned the inheritance chunk from `oop_concepts.txt`.

This retrieval method is simple, but it is useful for understanding how grounding works. It also gives me a baseline before trying more advanced methods such as TF-IDF or embedding retrieval.

## 3. Connect course materials to the tutor

I completed this objective by updating the Streamlit app.

The app now includes:

- A checkbox called “Use CISC230 course materials”
- A “Retrieved Course Context” display section
- A course-aware prompt
- A connection between the retrieved material and the model response

When retrieval is turned on, the app retrieves relevant course context and inserts it into the model prompt before generating the tutor response.

The current system flow is:

Student question  
→ retrieve relevant CISC230 material  
→ include retrieved context in the prompt  
→ send prompt to selected model  
→ generate tutor response

This means the course materials are now directly connected to the tutor.

## 4. Compare responses with and without retrieval support

I completed this objective by testing the same questions with retrieval off and retrieval on.

I tested:

- What is inheritance?
- What is polymorphism?

For inheritance, retrieval off produced a correct but generic explanation. Retrieval on produced a more course-aligned explanation that used vocabulary from the retrieved course material, such as superclass, subclass, shared behavior, and override.

For polymorphism, retrieval on found the correct course context about objects of different classes working through a shared type. However, this test also revealed a limitation: the model initially generated an unsupported example and implied it came from the course materials. This led me to improve the prompt.

I saved comparison notes in:

week-02-course-aware-tutor/03-comparison-study/inheritance-comparison.md

This comparison showed that retrieval can improve course alignment, but it also showed that retrieval does not automatically guarantee perfect educational behavior.

---

# Research Objectives

## 1. Investigate how retrieval affects educational quality

Retrieval affected educational quality by making the tutor’s responses more course-aligned and less generic.

Without retrieval, the tutor could explain programming concepts, but the response did not necessarily match CISC230. With retrieval, the tutor could use course vocabulary and connect its response to the available course material.

This improved educational quality in several ways:

- The response used familiar course terminology.
- The tutor was less likely to rely only on general knowledge.
- The answer was more connected to what students are likely learning.
- The tutor could support learning within the course context.

However, I also found that retrieval improves educational quality only when the retrieved content is relevant and safe. If the retrieval system finds incomplete, wrong, or unsafe material, the tutor response may still be problematic.

Therefore, retrieval is helpful, but it needs careful document selection, strong prompting, and evaluation.

## 2. Analyze situations where retrieval helps and where it fails

Retrieval helped most when the student question directly matched information in the course materials.

It helped with:

- “What is inheritance?”
- “What is polymorphism?”

In these cases, the retrieval system found relevant chunks from `oop_concepts.txt`, and the tutor used the retrieved ideas in its response.

Retrieval helped by:

- Improving course alignment
- Providing relevant vocabulary
- Reducing the need for the model to guess
- Making the response more connected to the course

Retrieval failed or was limited when the model went beyond the retrieved context.

The polymorphism test showed this clearly. The retrieved content was correct, but the model initially generated an example that was not actually in the course materials and implied it came from the course. This showed that retrieval does not fully prevent hallucination.

This failure led to an improvement. I changed the course-aware prompt so the tutor should not claim something comes from course materials unless it appears in the retrieved context.

My finding is that retrieval helps most when the question and documents match clearly, but it can fail when the model adds unsupported details or when the retrieved context is too limited.

## 3. Begin thinking about how tutoring policies should evolve when course materials are available

This objective became very important during Week 2.

In Week 1, the tutor only had a general academic-integrity rule: do not provide complete homework solutions.

In Week 2, once course materials became available, I realized the policy needs to become more specific.

The tutor now needs policies about:

- Which documents are safe to retrieve
- Whether homework descriptions should be included
- Whether starter code should be included
- Whether rubrics should be included
- Whether solutions and answer keys should be excluded
- When small code examples are acceptable
- How to respond to assignment-specific questions
- How to refuse complete solution requests

Course materials make the tutor more powerful, but also riskier. If the tutor has access to the wrong materials, it may reveal answers. Therefore, tutoring policies should evolve from a general “be helpful” rule to a more detailed policy based on question type and document type.

A possible policy structure is:

Concept questions:
Explain the concept, give a small example, and ask a follow-up question.

Debugging questions:
Ask what the student tried, help interpret errors, and suggest the next step.

Assignment clarification:
Summarize requirements and explain expectations without solving the assignment.

Complete solution requests:
Refuse to provide full code or full answers, then offer hints or a plan.

Restricted materials:
Do not retrieve or reveal solutions, answer keys, or previous student submissions.

This reflection connects directly to academic integrity. The tutor should support learning, not replace student work.

---

# Prototype Work Completed

This week, I completed the following prototype work:

- Created a Week 2 project folder
- Added a course-materials folder
- Added sample course policy and OOP concept files
- Built `retrieval.py`
- Updated `app.py` to support retrieval
- Added a retrieval checkbox
- Displayed retrieved context in the app
- Strengthened the course-aware prompt
- Created `model_client.py`
- Added a model-backend dropdown
- Added Ollama llama3.2 as the working local backend
- Attempted to add OpenAI API as a non-Ollama backend

---

# Model and Backend Reflection

The current working model setup is:

- Streamlit as the web interface
- Ollama as the local model runner
- llama3.2 as the local model

I also added code for an OpenAI API backend so the system could eventually compare a local model with a non-Ollama cloud model. The API key was recognized, but the request failed because my OpenAI API account had insufficient quota.

This was not a coding failure. It showed a practical research issue: model comparison depends on access, billing, credits, or institutional support.

This is something I should discuss with my professor. I need to ask whether the project has a shared API key, whether I should use a department-supported account, or whether I should compare multiple local models first.

---

# Main Findings

1. Retrieval improves course alignment.
2. Retrieval makes the tutor less generic.
3. Retrieval helps the tutor use course vocabulary.
4. Retrieval does not fully prevent hallucination.
5. Prompting still matters after retrieval is added.
6. Course-material selection affects academic integrity.
7. The tutor needs different policies for concept questions, debugging questions, assignment questions, and full-solution requests.
8. Model comparison requires access to different models or APIs.
9. A course-aware tutor is not just a chatbot with documents attached; it needs educational design.

---

# Current Limitations

- The retrieval system is still simple and keyword-based.
- The course materials are sample materials, not full real CISC230 materials yet.
- The tutor may still give too much code in some responses.
- The OpenAI API backend is blocked by insufficient quota.
- More testing is needed for academic-integrity boundary questions.
- More real course documents are needed after professor approval.
- The system does not yet label documents as safe, caution, or restricted.

---

# Questions for Professor

1. Which real CISC230 materials should I include in the retrieval system?
2. Which materials should I avoid completely?
3. Should homework descriptions be included?
4. Should rubrics and starter code be included?
5. Should answer keys and previous solutions be excluded?
6. Should the tutor provide small code examples for general concept questions?
7. How should the tutor respond to assignment-specific questions?
8. Should the tutor show retrieved context to students or keep it hidden?
9. Should Week 3 focus on better retrieval, better tutoring behavior, or model comparison?
10. Is there a project API key or department-supported model access for testing non-Ollama models?

---

# Overall Reflection

Week 2 helped me understand that retrieval can make an AI tutor more course-aware, but retrieval alone is not enough. It improved the tutor’s course alignment, especially for concept questions like inheritance and polymorphism. However, I also observed that the model can still hallucinate or add unsupported examples.

The most important thing I learned is that a course-aware AI tutor needs both technical grounding and educational policy. The technical system retrieves course materials, but the educational design decides how the tutor should use those materials. A useful tutor must support learning, respect academic integrity, and avoid pretending to know more than the retrieved course context actually provides.

My main takeaway is:

Retrieval improves course alignment, but it does not automatically make the tutor educationally safe. The tutor still needs careful document selection, strong prompts, academic-integrity rules, and systematic evaluation.

---

# Guiding Questions Reflection

## About Learning

### Why might students trust an answer simply because it sounds confident?

Students might trust an AI answer because the response is written fluently and confidently. Even when the answer is wrong or unsupported, the tone can make it seem reliable. This is risky in education because students may not yet have enough knowledge to recognize mistakes.

In this project, I saw how easily a model can sound confident. During the polymorphism test, the tutor retrieved correct course context but initially generated an unsupported example and implied it came from the course materials. The response sounded believable, but it was not fully grounded in the retrieved material.

This matters because an AI tutor should not only sound helpful. It should be accurate, transparent, and aligned with the course.

### What happens when an AI tutor gives advice that contradicts course expectations?

When an AI tutor gives advice that contradicts course expectations, it can confuse students and possibly lead them in the wrong direction. A student might use a concept, programming language, style, or solution strategy that does not match what the instructor expects.

For example, if CISC230 expects Java and the tutor gives a C++ example, the explanation may still relate to object-oriented programming, but it is not fully course-aligned. This could confuse students or make the tutor less useful for the actual class.

This is why course grounding is important. The tutor should not only answer correctly in a general sense; it should answer in a way that matches the course’s language, level, and expectations.

### How can course materials improve learning support?

Course materials can improve learning support by giving the tutor access to the same context students are using. This can include lecture vocabulary, assignment expectations, course policies, examples, and rubrics.

In my prototype, course materials improved the tutor’s response to the inheritance question. Without retrieval, the tutor gave a generic explanation. With retrieval, it used course-related terms such as superclass, subclass, shared behavior, and override.

This made the response more educationally useful because it connected the explanation to the course context instead of giving a general programming answer.

---

## About Retrieval

### What information should the tutor have access to?

The tutor should have access to materials that help students learn without giving away complete answers.

Useful information may include:

- Syllabus policies
- Lecture notes
- Concept explanations
- Lab instructions
- Homework descriptions
- Rubrics
- Starter code
- General examples

The tutor should especially have access to materials that explain concepts, clarify expectations, and support step-by-step learning.

### Which documents are useful?

Useful documents are documents that help the tutor understand the course without exposing solutions.

For this prototype, I used:

- `course_policies.txt`
- `oop_concepts.txt`

These were useful because they helped the tutor understand both tutoring expectations and object-oriented programming concepts.

In the future, useful real CISC230 documents may include lecture slides, lab instructions, homework descriptions, rubrics, and syllabus policies. These documents can help the tutor answer questions in a course-aware way.

### Which documents might create problems?

Documents that contain complete answers can create problems.

Risky documents include:

- Homework solutions
- Answer keys
- Completed lab solutions
- Previous student submissions
- Test or quiz answers
- Instructor-only solution notes

These documents might make the tutor more accurate, but they also increase the risk of academic-integrity violations. If the tutor retrieves solution material, it may accidentally reveal answers to students.

### Can retrieval accidentally expose assignment solutions?

Yes. Retrieval can accidentally expose assignment solutions if unsafe documents are included in the course-material database.

This is one of the biggest risks of a course-aware tutor. Retrieval makes the tutor more powerful, but it also means document selection becomes very important.

Because of this, the project should use document safety rules. For example:

Safe documents:
Lecture notes, syllabus policies, concept explanations, public assignment descriptions.

Caution documents:
Starter code, rubrics, detailed lab instructions.

Restricted documents:
Solutions, answer keys, previous student submissions, completed assignments.

This is something I need to discuss with my professor before adding real CISC230 materials.

---

## About Research

### Does retrieval improve educational quality?

Based on my initial testing, retrieval does improve educational quality in some cases.

For the inheritance question, retrieval made the tutor more course-aligned. The response used vocabulary from the retrieved course material, including superclass, subclass, shared behavior, and override.

This improved educational quality because the tutor’s response became more connected to what students are likely learning in CISC230.

However, retrieval does not automatically guarantee quality. The retrieved material must be relevant, safe, and correctly used by the model.

### Does retrieval reduce hallucinations?

Retrieval can reduce hallucinations by giving the model relevant context before it answers. Instead of relying only on its general training, the model can use course materials.

However, my testing showed that retrieval does not completely eliminate hallucinations. During the polymorphism test, the tutor retrieved correct context but initially added an unsupported example and implied it came from the course materials.

This means retrieval helps, but it must be combined with stronger prompting and careful evaluation. After observing this issue, I improved the prompt so the tutor would not claim something came from the course unless it appeared in the retrieved context.

### How can we measure whether retrieval is helping?

We can measure whether retrieval is helping by comparing tutor responses with retrieval off and retrieval on.

Possible evaluation criteria include:

- Correctness
- Course alignment
- Use of course vocabulary
- Educational usefulness
- Level of detail
- Hallucination risk
- Academic-integrity behavior
- Whether the response helps the student think instead of giving away the answer

In my prototype, I started measuring retrieval by comparing responses to the same questions:

- What is inheritance?
- What is polymorphism?

This comparison showed that retrieval improved course alignment, but also revealed that retrieval does not fully prevent hallucination.

In future work, I could create a simple rubric and score each response based on course alignment, accuracy, scaffolding, and academic-integrity safety.

