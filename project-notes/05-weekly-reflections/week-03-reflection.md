# Week 3 Reflection: Designing Tutoring Behavior

## Week 3 Focus

During Week 3, I focused on improving the AI tutor’s tutoring behavior. In Week 1, I built a simple educational tutor prototype. In Week 2, I made the tutor course-aware by adding retrieval from CISC 230 materials. In Week 3, the goal was to move beyond simply answering questions and begin designing the tutor to respond differently depending on the type of student question.

The main focus was shifting from:

Student question → retrieved course material → AI answer

to:

Student question → detected tutoring scenario → retrieved course material → tutoring strategy → course-grounded tutor response

This week helped me understand that an educational tutor needs more than correct information. It also needs to guide students, ask useful questions, support debugging, protect academic integrity, and encourage independent thinking.

---

# Educational Objectives

## 1. Explain the characteristics of effective tutoring conversations

Effective tutoring conversations are clear, supportive, interactive, and responsive to the student’s current understanding. A tutor should not simply give information. It should help the student think through the concept or problem.

In this project, effective tutoring means:

* Using language that matches the course.
* Giving focused explanations.
* Asking check-for-understanding questions.
* Giving hints instead of complete answers when appropriate.
* Helping students reason through errors.
* Avoiding random examples that are not connected to the course.

During Week 3, I noticed that even when the tutor retrieved the correct CISC 230 material, the model could still behave like a general chatbot. For example, when I asked about inheritance, the tutor retrieved the correct Chapter 9 slides but still added outside examples such as houses, vehicles, and cars. This showed me that tutoring quality depends not only on retrieval but also on how strongly the tutor is instructed to use the retrieved materials.

## 2. Describe how different types of student questions require different tutoring strategies

Different student questions require different tutoring strategies because students need different kinds of support depending on what they are trying to do.

For concept-learning questions, such as “What is inheritance?”, the tutor should explain the concept clearly using CISC 230 terminology and ask a short check-for-understanding question.

For debugging questions, such as “Why am I getting a NullPointerException?”, the tutor should not immediately give fixed code. Instead, it should help the student inspect the error message, line number, object reference, variable state, or method call involved.

For assignment clarification questions, the tutor should help the student understand the goal, requirements, and concepts involved without completing the assignment.

For reflection questions, the tutor should help the student evaluate their own reasoning by asking why they think an approach makes sense.

To support this, I added scenario detection to the prototype. The tutor can now detect concept learning, debugging, assignment clarification, reflection, and general tutoring scenarios.

## 3. Understand common misconceptions encountered by novice Java programmers

Beginning Java students often struggle with the difference between classes and objects, how constructors work, when to use the `new` keyword, and how object references behave. They may also confuse superclass and subclass relationships, misunderstand inheritance, or assume that method overriding and method overloading are the same.

Some common misconceptions include:

* Thinking a class and an object are the same thing.
* Thinking a constructor is a regular method.
* Forgetting that constructors do not have a return type.
* Confusing superclass and subclass roles.
* Thinking inheritance means copying code manually.
* Thinking a subclass can always access all superclass variables directly.
* Confusing overloading with overriding.
* Misunderstanding polymorphic references and casting.
* Reading an error message without checking the line number or object involved.

The professor’s lecture materials helped identify these topics because the converted lecture files include chapters on writing classes, object-oriented design, inheritance, polymorphism, arrays, exceptions, and related Java concepts.

## 4. Reflect on what makes an AI tutor educationally helpful rather than simply informative

An informative response gives an answer. An educationally helpful response supports learning.

A response may be technically correct but still not educationally helpful if it is too long, too advanced, disconnected from the course, or gives away too much. A helpful tutor should guide the student toward understanding rather than replacing the student’s thinking.

In Week 3, I saw this clearly when the tutor answered the inheritance question. The retrieved materials were correct, but the generated response added extra analogies and outside examples. That made the response less course-grounded. It was informative, but not ideal as a CISC 230 tutor.

This taught me that an educational tutor needs strong rules about response behavior. It should use course materials, stay concise, ask students to explain ideas in their own words, and avoid creating dependency.

---

# Technical Objectives

## 1. Improve the tutor's response quality

I improved the tutor’s response quality by making the system more course-grounded and more structured.

The main improvement was changing retrieval from whole-file retrieval to smaller chunk-based retrieval. Before this change, if a lecture file contained the word “inheritance” one time, the tutor retrieved almost the entire lecture file. This made the retrieved context messy and hard to use.

After the update, lecture files are split into smaller chunks based on slide markers. For example, instead of retrieving all of `chapter-9.txt`, the system can retrieve focused chunks such as:

* `chapter-9.txt :: Slide 2`
* `chapter-9.txt :: Slide 4`
* `chapter-9.txt :: Slide 5`

This made the retrieved context much more readable and relevant.

I also strengthened the tutor prompt so that when course materials are active, the tutor should avoid outside examples and use only the retrieved CISC 230 materials.

## 2. Support multiple tutoring scenarios, including concept learning, debugging, and assignment clarification

I completed this objective by creating `tutor_behavior.py`.

This file includes scenario detection for:

* Concept learning
* Debugging
* Assignment clarification
* Reflection
* General tutoring

Each scenario has a different tutoring strategy. For example, concept-learning responses should explain the idea clearly and ask a check-for-understanding question. Debugging responses should guide students through the error instead of immediately fixing the code. Assignment clarification responses should explain requirements and concepts without completing the assignment.

This helps the tutor behave more like an educational assistant rather than a general question-answering chatbot.

## 3. Organize the system into reusable software components

I continued organizing the prototype into reusable components.

The Week 3 prototype includes:

* `app.py` for the Streamlit interface
* `retrieval.py` for loading, chunking, and retrieving course materials
* `tutor_behavior.py` for scenario detection and tutoring strategies
* `model_client.py` for model calls
* `00-course-materials/` for CISC 230 concepts, policies, and lecture files

This organization makes the system easier to modify. For example, I can improve retrieval without rewriting the Streamlit interface, or adjust tutoring strategies without changing the model client.

## 4. Begin creating a framework for evaluating tutoring quality

I began thinking about an evaluation framework by identifying criteria that make one tutor response better than another.

Possible evaluation criteria include:

* Accuracy
* Course alignment
* Clarity
* Use of appropriate tutoring strategy
* Student engagement
* Academic integrity
* Avoidance of unsupported examples
* Helpfulness for learning
* Support for independent thinking

This will become important in future weeks because the project needs a way to compare tutor responses systematically. A response should not be evaluated only by whether it is correct. It should also be evaluated by whether it supports learning.

---

# Research Objectives

## 1. Compare different tutoring styles

This week, I compared general chatbot-style responses with course-grounded tutoring responses.

When the tutor behaved like a general chatbot, it gave broad explanations, analogies, and examples from outside the retrieved materials. These responses were often understandable, but they were not always aligned with CISC 230.

When the tutor used course-grounded behavior, the response was more connected to the professor’s lecture materials. For example, the inheritance response retrieved Chapter 9 slides about superclass, subclass, parent class, child class, and the is-a relationship.

This comparison showed me that course-grounded tutoring is better for this project because the goal is not just to explain Java in general. The goal is to support students in a specific object-oriented programming course.

## 2. Identify strengths and weaknesses of the current tutor

The current tutor has several strengths:

* It retrieves CISC 230 materials.
* It can use professor lecture files.
* It displays retrieved context.
* It detects different tutoring scenarios.
* It separates the interface, retrieval, tutoring behavior, and model calls into different files.
* It avoids OpenAI/general mode when course-only mode is used.
* It can support concept-learning questions with course-specific context.

The current tutor also has weaknesses:

* Retrieval is still keyword-based.
* Some irrelevant chunks can still appear.
* The model may still add outside examples unless the prompt is very strict.
* The tutor does not yet fully evaluate its own response quality.
* More testing is needed for debugging and assignment clarification.
* The tutor does not yet have a formal rubric implemented in code.
* Course material safety still needs careful professor guidance.

The biggest weakness I noticed is that retrieval alone does not guarantee a good tutoring response. The system also needs strict prompt rules and evaluation.

## 3. Develop an evaluation framework that can be used throughout the remainder of the project

I started developing an evaluation framework by thinking about how to judge tutor responses.

A possible rubric could score each response from 1 to 4 on the following criteria:

* Correctness: Is the answer accurate?
* Course alignment: Does it use retrieved CISC 230 materials?
* Clarity: Is it understandable for a beginning Java student?
* Tutoring behavior: Does it guide learning instead of only giving an answer?
* Scenario fit: Does it respond appropriately to concept, debugging, or assignment questions?
* Academic integrity: Does it avoid completing student work?
* Independence: Does it encourage the student to think?

This framework can be used in future weeks to compare tutor outputs and track whether the system is improving.

---

# Prototype Work Completed

This week, I completed the following prototype work:

* Created the Week 3 project folder structure.
* Added professor Object-Oriented Programming lecture materials.
* Converted lecture materials into text files for retrieval.
* Added the lecture files to `00-course-materials/lectures/`.
* Improved retrieval from whole-file retrieval to slide/chunk retrieval.
* Added topic-based boosts so inheritance prefers Chapter 9 and polymorphism prefers Chapter 10.
* Added scenario detection in `tutor_behavior.py`.
* Added tutoring strategies for concept learning, debugging, assignment clarification, reflection, and general tutoring.
* Strengthened course-grounded prompt rules.
* Disabled the unchecked/general chatbot mode in the Streamlit app.
* Set the app to always use CISC 230 course materials.
* Kept Ollama as the local model backend.
* Committed and pushed Week 3 updates to GitHub.

---

# Current Prototype Architecture

Student question
→ Streamlit interface
→ detect tutoring scenario
→ retrieve relevant CISC 230 lecture chunks
→ build course-grounded tutoring prompt
→ local Ollama model
→ tutor response

This architecture is more educationally structured than the earlier versions because the tutor now uses both course context and tutoring behavior logic.

---

# Main Findings

1. A tutor can be correct but still not educationally ideal.
2. Retrieval improves course alignment, but retrieval alone is not enough.
3. Whole-file retrieval creates too much irrelevant context.
4. Chunk-based retrieval makes the retrieved material more focused.
5. The tutor needs different strategies for different student questions.
6. Course-grounded mode should not behave like a general chatbot.
7. Strict prompting is needed to prevent unsupported examples.
8. Debugging support should guide students instead of immediately fixing code.
9. Assignment support should clarify requirements without completing the work.
10. Evaluating tutoring quality requires more than checking correctness.

---

# Current Limitations

* The retrieval system is still simple and keyword-based.
* The system does not yet use embeddings or semantic search.
* Some retrieved chunks may still be too broad or too narrow.
* The tutor may still need stronger control to avoid outside examples.
* Debugging and assignment clarification need more testing.
* The evaluation framework is still a draft and not yet implemented in the app.
* More professor feedback is needed about which materials should be included or excluded.
* The lecture materials should be handled carefully because they may be instructor-provided course materials.

---

# Questions for Professor

1. Should the tutor always use CISC 230 materials, or should there be a comparison mode?
2. Should students see the retrieved course context, or should it be hidden?
3. Are the converted lecture text files acceptable to use in the prototype?
4. Which lecture materials should be included or excluded?
5. Should the tutor provide examples only if they appear in the retrieved materials?
6. How strict should the tutor be about avoiding outside examples?
7. What debugging behavior would be most helpful for CISC 230 students?
8. How should the tutor respond to assignment-specific questions?
9. What criteria should we use to evaluate tutor response quality?
10. Should the next step focus on better retrieval, better evaluation, or more testing?

---

# Overall Reflection

Week 3 helped me understand that a course-aware tutor is still not automatically an effective tutor. In Week 2, I focused on whether the system could retrieve CISC 230 materials. In Week 3, I saw that the tutor also needs to decide how to respond based on the student’s question type.

The most important technical improvement this week was changing retrieval from whole-file retrieval to chunk-based retrieval. This made the retrieved context more focused and easier for the tutor to use.

The most important educational insight was that tutoring quality is different from answer quality. A response can be accurate but still fail as tutoring if it gives too much away, uses unsupported examples, ignores the student’s reasoning, or does not encourage the student to think.

My main takeaway is:

A useful educational AI tutor needs course grounding, tutoring strategies, academic-integrity rules, and an evaluation framework. Retrieval gives the tutor information, but tutoring behavior determines whether the response actually supports learning.

---

# Guiding Questions Reflection

## About Learning

### What makes an explanation easy to understand?

An explanation is easy to understand when it is clear, focused, and appropriate for the student’s current level. For a beginning Java student, the tutor should use familiar course vocabulary and avoid adding unnecessary outside details.

In this project, I saw that explanations became harder to understand when the retrieved context was too large. When the tutor retrieved an entire lecture file, the response had too much unrelated information available. After changing retrieval to smaller slide-based chunks, the retrieved context became more focused.

An easy-to-understand explanation should connect directly to the student’s question, use course terms, and end with a question that checks understanding.

### When should a tutor provide hints instead of answers?

A tutor should provide hints when the student is solving a problem, debugging code, or working on an assignment. If the tutor gives the full answer immediately, the student may complete the task without understanding it.

Hints are useful because they support the student’s reasoning process. For example, in debugging, the tutor can ask the student to check the error message, line number, variable value, or object reference instead of rewriting the code for them.

The goal is to give enough support for the student to move forward while still leaving the thinking to the student.

### What kinds of responses encourage students to think?

Responses encourage students to think when they ask the student to explain, predict, compare, or justify. A tutor can ask questions like:

* What do you think this variable refers to?
* Which class is the superclass?
* What does the error message point to?
* Why do you think this method is being called?
* Can you explain that idea in your own words?

These kinds of responses make the student actively participate instead of passively receiving an answer.

### How can an AI tutor build confidence without creating dependency?

An AI tutor can build confidence by helping students recognize what they already understand and by giving manageable next steps. It can validate partial progress, explain confusing ideas clearly, and encourage students to keep reasoning.

However, it can create dependency if it gives complete answers or code too quickly. To avoid this, the tutor should provide hints, ask guiding questions, and encourage students to explain their reasoning.

A good tutor should make students feel more capable, not more dependent.

---

## About Programming Education

### What mistakes do beginning Java students commonly make?

Beginning Java students commonly make mistakes with syntax, object creation, constructors, method calls, visibility modifiers, inheritance, and object references.

Common mistakes include:

* Confusing classes and objects.
* Forgetting to create objects with `new`.
* Putting a return type on a constructor.
* Confusing instance variables with local variables.
* Making instance variables public and violating encapsulation.
* Confusing superclass and subclass relationships.
* Misunderstanding method overriding.
* Confusing overloading and overriding.
* Misreading compiler or runtime error messages.
* Trying to fix code without understanding the cause of the error.

These mistakes show why the tutor needs to support both conceptual understanding and debugging.

### Which concepts are most difficult for students to understand?

Some of the most difficult Java concepts for beginners are object references, constructors, inheritance, polymorphism, method overriding, casting, and the difference between compile-time and run-time behavior.

These concepts are difficult because they require students to think about relationships between classes and objects, not just individual lines of code. For example, polymorphism requires understanding that a reference variable can point to different types of objects, and the method that runs may depend on the object type at run time.

These topics need careful explanations, course-aligned examples, and guided practice.

### How should the tutor respond differently to conceptual questions and debugging questions?

For conceptual questions, the tutor should explain the concept using retrieved course materials and ask a check-for-understanding question. The response should be concise and focused on understanding.

For debugging questions, the tutor should guide the student through the debugging process. It should ask about the error message, line number, expected output, actual output, and relevant code. The tutor should avoid immediately giving fixed code because debugging is an important learning activity.

Conceptual questions need explanation. Debugging questions need diagnosis and guided reasoning.

---

## About Research

### How do we determine whether one tutoring response is better than another?

One tutoring response is better than another if it better supports student learning. Correctness matters, but it is not the only factor.

A better tutoring response should be accurate, course-aligned, clear, appropriate for the student’s question type, and supportive of independent thinking. It should also avoid giving complete homework solutions or unsupported examples.

During Week 3, I saw that a response could be correct but still weaker if it behaved like a general chatbot. A better response would stay grounded in the retrieved CISC 230 materials and ask the student to explain the concept in their own words.

### What criteria should be used to evaluate educational quality?

Educational quality should be evaluated using multiple criteria, including:

* Correctness
* Clarity
* Course alignment
* Relevance of retrieved materials
* Appropriate tutoring strategy
* Student engagement
* Academic-integrity safety
* Support for independent thinking
* Avoidance of hallucinated or unsupported examples

These criteria can help compare different tutor responses and decide whether the tutor is improving.

### Can educational usefulness be measured?

Educational usefulness can be measured, but it is more complex than measuring correctness. A correct answer may still not be useful if it is too advanced, too long, unrelated to the course, or gives away too much.

Educational usefulness can be measured with a rubric, scenario-based testing, and comparisons between different tutor responses. For example, I can test the same question across different versions of the tutor and score the responses based on course alignment, clarity, scaffolding, and academic-integrity behavior.

This kind of evaluation can help make future improvements more systematic.

