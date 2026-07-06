# Week 2 Reflection: Building a Course-Aware AI Tutor

## Week 2 Focus

During Week 2, I focused on making the AI tutor course-aware. In Week 1, the tutor could answer general programming questions, but it did not know anything about a specific course. Week 2 addressed this problem by adding retrieval from selected CISC230 course materials.

The goal was to move from:

Student question
→ AI model

to:

Student question
→ course materials
→ AI model

This changed the tutor from a generic chatbot into the beginning of a course-aware learning assistant.

## Educational Objective 1: Explain why educational grounding is important

Educational grounding is important because a tutor should give support that matches the course context. A general language model may give an answer that is technically correct but not appropriate for the class.

For example, it might:

- Use a different programming language
- Introduce advanced concepts too early
- Give advice that conflicts with the instructor’s expectations
- Ignore assignment-specific instructions
- Provide too much code

In my prototype, educational grounding means retrieving relevant CISC230 material before the model answers. This helps the tutor use course vocabulary and stay closer to what students are actually learning.

When I tested the question “What is inheritance?” without retrieval, the tutor gave a correct but generic answer. With retrieval, the tutor used course-related terms such as superclass, subclass, shared behavior, and override. This showed that grounding can improve course alignment.

## Educational Objective 2: Discuss the risks of hallucinations in educational systems

Hallucinations are especially dangerous in educational systems because students may trust an answer if it sounds confident. If the tutor gives incorrect or unsupported information, students may learn the wrong concept or follow the wrong assignment instructions.

I observed this during the polymorphism test. The retrieval system found the correct course context, but the model initially generated a C++ example and implied that it came from the course materials. This was a problem because the retrieved context did not include that example.

This showed me that retrieval helps, but it does not completely prevent hallucinations. The model still needs strong instructions about how to use retrieved material.

To improve this, I updated the course-aware prompt to say that the tutor should not claim an example, phrase, or requirement comes from the course materials unless it appears in the retrieved context. After this improvement, the tutor gave a Java example and did not falsely claim it came from the course material.

## Educational Objective 3: Describe how course context influences learning support

Course context influences learning support because students need help that fits their current course, not just general explanations.

For example, if a student asks about inheritance, a generic tutor might explain the concept using unrelated examples or advanced ideas. A course-aware tutor can focus on the specific vocabulary and level of detail used in the course.

In my prototype, course context influenced the tutor by giving it retrieved material before answering. This changed the response in several ways:

- The tutor used course vocabulary.
- The response became more aligned with CISC230.
- The tutor had less need to guess.
- The answer was more connected to what students are likely learning.

This suggests that course context can make AI tutoring more educationally useful.

## Educational Objective 4: Reflect on the relationship between tutoring and academic integrity

Tutoring and academic integrity are closely related because a tutor should help students learn without replacing their work.

A good tutor can:

- Explain concepts
- Ask guiding questions
- Give hints
- Help debug step by step
- Suggest a plan

But it should not:

- Write complete homework solutions
- Provide full assignment code
- Reveal answer keys
- Complete the work for the student

Retrieval makes this issue more complex. If the tutor retrieves lecture notes or assignment descriptions, it can provide useful support. But if it retrieves complete solutions or answer keys, it could leak answers. This means course-aware tutoring requires careful document selection.

In this project, I started addressing academic integrity by including course policy text and by strengthening the system prompt. The tutor is instructed to refuse complete solution requests and offer conceptual help instead.

## Technical Work Completed

This week, I created a Week 2 project structure:

- week-02-course-aware-tutor/01-course-materials
- week-02-course-aware-tutor/02-prototype
- week-02-course-aware-tutor/03-comparison-study
- week-02-course-aware-tutor/04-literature-notes
- week-02-course-aware-tutor/05-reflection

I added sample course material files:

- course_policies.txt
- oop_concepts.txt

I built retrieval.py, which:

- Reads course-material text files
- Splits them into chunks
- Scores chunks using keyword overlap
- Returns relevant course context

I updated app.py to include:

- Retrieval checkbox
- Retrieved course context display
- Course-aware prompt
- Comparison between retrieval and no retrieval

I added model_client.py to separate model logic from the Streamlit interface.

## Model and Backend Work

The current working model setup is:

- Streamlit as the web interface
- Ollama as the local model runner
- llama3.2 as the main local model

I also added an OpenAI API backend as a non-Ollama model comparison option. The code was added successfully, and the API key was recognized. However, testing was blocked because my OpenAI API account had insufficient quota.

This was still useful because it showed a real practical issue: model comparison depends not only on code, but also on access, billing, and institutional resources.

## Comparison Study: Inheritance

Question:

What is inheritance?

Without retrieval:
The tutor gave a correct but generic explanation.

With retrieval:
The tutor retrieved course context and used terms such as superclass, subclass, shared behavior, and override.

Finding:
Retrieval improved course alignment.

## Comparison Study: Polymorphism

Question:

What is polymorphism?

With retrieval:
The tutor retrieved the correct course context about objects of different classes working through a shared type.

Finding:
The tutor used the retrieved idea correctly, but the test also revealed that retrieval does not fully prevent hallucination. Prompt improvements were needed.

## Main Findings

1. Retrieval improves course alignment.
2. Retrieval does not fully prevent hallucinations.
3. Prompt design still matters after retrieval is added.
4. Course-material selection affects both usefulness and academic integrity.
5. Model comparison requires access to different models or APIs.
6. A course-aware tutor must balance helpfulness with student responsibility.

## Current Limitations

- Retrieval is currently keyword-based and simple.
- The system only uses sample course materials so far.
- Real CISC230 materials still need to be selected.
- The tutor may still give too much code for some questions.
- The OpenAI API backend is blocked by quota.
- More academic-integrity testing is needed.

## Questions for Professor

1. Which real CISC230 materials should I include?
2. Which materials should I avoid?
3. Should the tutor provide small code examples for general concept questions?
4. How should the tutor respond to assignment-specific questions?
5. Should the next step be better retrieval, better tutoring behavior, or model comparison?
6. Is there a project API key or department-supported model access?
7. Should retrieved course context be visible to students or hidden?

## Overall Reflection

Week 2 showed me that course grounding can transform a generic AI chatbot into a more course-aware tutor. Retrieval helped the tutor use course vocabulary and answer in a way that better matched CISC230.

However, I also learned that retrieval is not enough by itself. The model can still hallucinate, provide too much detail, or use retrieved context in unsafe ways. Because of this, the tutor needs strong prompts, careful course-material selection, academic-integrity safeguards, and systematic evaluation.

My main takeaway is that a course-aware AI tutor is not simply a chatbot with documents attached. It is a learning system that must be designed around course context, student understanding, and responsible support.
