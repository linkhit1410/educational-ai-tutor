# Week 3 Reading Notes: Tutoring Design and Programming Education

## Week 3 Reading Focus

This week's readings shift from technical implementation toward programming education, tutoring strategies, debugging support, and evaluation.

The main question for this week is:

How can an AI tutor support learning instead of simply giving answers?

These readings connect directly to the Week 3 prototype work because the tutor now needs to support different tutoring scenarios, such as concept learning, assignment clarification, debugging, and reflection.

---

## Reading 1: VanLehn (2011)

**Citation:**  
VanLehn, K. (2011). *The Relative Effectiveness of Human Tutoring, Intelligent Tutoring Systems, and Other Tutoring Systems.*

### Why this reading matters

This paper is important because it compares human tutoring, intelligent tutoring systems, and other types of tutoring systems. It helps explain why tutoring can be effective and what features make tutoring useful for learning.

### Focus Question 1: What makes tutoring effective?

Tutoring is effective when it responds to the learner's current understanding. A tutor can give feedback, ask questions, provide hints, and adjust the level of support based on what the student needs.

For my AI tutor project, this means the tutor should not only answer programming questions. It should guide students through the learning process.

### Focus Question 2: What types of feedback improve learning?

Feedback improves learning when it helps students understand what they did wrong and how to think about the next step. Useful feedback should be specific enough to help the student move forward but not so direct that it removes the learning process.

For the CISC 230 tutor, this supports the idea of giving hints, asking guiding questions, and encouraging students to explain their reasoning.

### Connection to project

This reading supports the Week 3 design decision to move beyond simple question-answering. The tutor should behave more like a learning assistant by using feedback strategies, hints, and check-for-understanding questions.

---

## Reading 2: Robins, Rountree, & Rountree (2003)

**Citation:**  
Robins, A., Rountree, J., & Rountree, N. (2003). *Learning and Teaching Programming: A Review and Discussion.*

### Why this reading matters

This paper is a classic review of difficulties students face when learning programming. It is useful for understanding why beginning programmers often struggle even when they have seen the syntax before.

### Focus Question 1: Which misconceptions occur most frequently?

Beginning programming students often struggle with core concepts such as variables, control flow, objects, methods, and program execution. In Java, students may also struggle with classes, objects, constructors, inheritance, and object references.

For CISC 230, this connects closely to topics such as:

- Classes and objects
- Constructors
- Encapsulation
- Inheritance
- Polymorphism
- Method overriding
- Debugging errors

### Focus Question 2: How should tutors respond to misconceptions?

Tutors should respond to misconceptions by helping students reason through the concept instead of only correcting the final answer. A tutor should identify the misunderstanding, explain the relevant concept, and ask the student to apply the idea.

For example, if a student confuses a class with an object, the tutor should explain that a class is a blueprint and an object is an instance created from that class.

### Connection to project

This reading supports the Week 3 focus on novice Java misconceptions. It also supports the need for different tutoring strategies depending on the type of student question.

---

## Reading 3: Lister et al. (2004)

**Citation:**  
Lister, R., et al. (2004). *A Multi-National Study of Reading and Tracing Skills in Novice Programmers.*

### Why this reading matters

This paper focuses on reading and tracing code. It highlights that many novice programmers struggle to understand what code does before they can successfully write new code.

### Focus Question 1: Why do students struggle with code comprehension?

Students may struggle because programming requires them to mentally trace execution, understand variable changes, follow method calls, and predict program behavior.

In Java, this can be especially difficult when objects, references, inheritance, and method calls are involved.

### Focus Question 2: How can tutors support code comprehension?

A tutor can support code comprehension by asking students to trace the code step by step. Instead of giving the answer immediately, the tutor can ask:

- What line runs first?
- What is the value of this variable?
- Which object is being used?
- Which method is called?
- What do you expect the output to be?

### Connection to project

This reading connects strongly to debugging support. When students encounter errors, the tutor should help them inspect the code and reason through what happened. Debugging should become a learning opportunity, not just a correction.

---

## Reading 4: Recent Paper on Conversational AI or Educational Chatbots in Programming Education

**Citation:**  
Recent paper on conversational AI or educational chatbots in programming education, 2023–2025.  
Exact paper title to be added after selecting the paper.

### Why this reading matters

This reading connects the project to current work on AI tutors and educational chatbots. It is especially relevant because modern LLM-based tutors can generate explanations, code, hints, and feedback.

### Focus Question 1: What kinds of conversations help novice programmers?

Helpful conversations for novice programmers include:

- Concept explanations
- Step-by-step debugging guidance
- Hint-based support
- Reflection questions
- Assignment clarification
- Code tracing questions
- Encouragement to explain reasoning

The tutor should not only provide answers. It should help students become better problem solvers.

### Focus Question 2: What limitations do conversational tutors have?

Conversational tutors can have several limitations:

- They may hallucinate.
- They may give unsupported examples.
- They may provide too much code.
- They may conflict with course expectations.
- They may make students dependent.
- They may not know which materials are safe to use.

These limitations connect directly to the Week 3 work on course-grounded mode and academic-integrity rules.

### Connection to project

This reading supports the need for strict tutoring behavior. The tutor should use CISC 230 materials, avoid unsupported examples, protect academic integrity, and encourage independent thinking.

---

## Optional Reading: Anderson, Corbett, Koedinger, & Pelletier (1995)

**Citation:**  
Anderson, Corbett, Koedinger, & Pelletier (1995). *Cognitive Tutors: Lessons Learned.*

### Why this reading may be useful

This reading is useful because cognitive tutors are an important example of educational technology designed around learning processes. It can help explain why feedback, practice, and student modeling matter.

### Connection to project

This optional reading connects to future improvements. The current prototype does not yet model individual student knowledge, but future versions could adapt hints based on the student’s progress.

---

## Optional Reading: Recent Survey on LLMs in Programming Education

**Citation:**  
Recent survey on LLMs in Programming Education, 2024–2025.  
Exact paper title to be added if selected.

### Why this reading may be useful

A recent survey on LLMs in programming education would help place this project in the current research context. It could provide examples of how LLMs are being used for code explanations, debugging support, feedback, and tutoring.

### Connection to project

This would help justify the project’s focus on course grounding, safety, academic integrity, and evaluation.

---

# Overall Reading Reflection

The Week 3 readings helped me understand that an AI tutor needs to be designed around learning, not just answer generation.

VanLehn's work connects to tutoring effectiveness and feedback strategies. Robins, Rountree, and Rountree connect to novice programming difficulties. Lister et al. connect to code reading and tracing skills. The recent conversational AI reading connects to modern LLM-based tutoring systems and their limitations.

Together, these readings support the main design direction for Week 3:

The tutor should give feedback, hints, and guiding questions instead of simply providing answers. It should respond differently to concept questions, debugging questions, assignment clarification questions, and reflection questions. It should also be evaluated using criteria such as correctness, educational quality, course alignment, helpfulness, safety, and encouragement of independent thinking.

The main takeaway is that tutoring behavior must be intentionally designed. A course-aware AI tutor should support student reasoning, protect academic integrity, and help students become more independent programmers.
