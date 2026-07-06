# Week 1 Reflection: Foundations of Educational AI Tutors

## Week 1 Focus

During Week 1, I focused on understanding how educational AI tutors are different from general-purpose chatbots. The main idea was that an AI tutor should support learning instead of simply giving students answers.

This week helped me think about tutoring as an educational process, not just a technical chatbot task.

## Educational Objective 1: Explain why one-on-one tutoring is effective

One-on-one tutoring is effective because it can respond to the student’s current understanding. A tutor can slow down, ask questions, give hints, and adjust explanations based on what the student says.

In this project, I tried to apply this idea by designing the tutor to guide students instead of directly completing their work. The Week 1 prototype included a system prompt telling the tutor to ask guiding questions, give hints, and encourage the student to explain what they tried.

## Educational Objective 2: Describe educational scaffolding

Educational scaffolding means giving students enough support to move forward without doing the entire task for them. The support can be gradually reduced as the student gains understanding.

For our AI tutor, scaffolding means the model should not immediately provide complete code or full homework solutions. Instead, it should break problems into smaller steps, explain concepts, and ask students questions that help them think.

## Educational Objective 3: Discuss benefits and risks of AI in programming education

AI can benefit programming education by giving students immediate help, explaining concepts in different ways, and helping them debug errors step by step.

However, AI also creates risks. Students may rely on it too much, receive incorrect explanations, or use it to complete assignments without understanding. In programming courses, this is especially important because a model can easily generate complete code.

This showed me that our tutor needs clear rules about academic integrity and learning support.

## Educational Objective 4: Explain the difference between helping students learn and helping students complete work

Helping students learn means supporting their reasoning process. It involves hints, questions, explanations, and debugging guidance.

Helping students complete work means giving them the final answer or complete code without requiring understanding.

In the Week 1 prototype, I tried to make this distinction clear in the system prompt. The tutor was instructed to avoid complete homework solutions and instead help students break problems into smaller steps.

## Technical Progress

This week, I built a simple Streamlit prototype connected to a local Ollama model.

The prototype included:

- Streamlit interface
- Text box for student questions
- Button to ask the tutor
- Ollama local model connection
- llama3.2 model
- System prompt focused on educational tutoring behavior

## Prototype Architecture

Student question
→ Streamlit interface
→ Ollama local model
→ Tutor response

## Main Finding

The Week 1 prototype could answer programming questions, but it was still generic. It did not know anything about a specific course, instructor, assignment, or learning objective.

This limitation led directly into Week 2, where the goal became making the tutor course-aware.

## Limitations

- The tutor was not connected to course materials.
- The tutor could give generic programming explanations.
- The tutor might introduce concepts outside the course.
- The tutor depended heavily on the prompt.
- There was no retrieval system yet.

## Questions Moving Forward

1. How can we make the tutor aware of a specific course?
2. What course materials should the tutor use?
3. How do we prevent the tutor from giving complete assignment solutions?
4. How do we measure whether the tutor is actually supporting learning?

## Overall Reflection

Week 1 helped me understand that building an educational AI tutor is not only a technical problem. It is also a learning-design problem. A good tutor should support student thinking, provide appropriate scaffolding, and respect academic integrity. The first prototype was a starting point, but it needed course grounding to become more useful for a real class.
