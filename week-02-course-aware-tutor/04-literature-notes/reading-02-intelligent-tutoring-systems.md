# Reading 2: A Comprehensive Review of AI-Based Intelligent Tutoring Systems

## Citation

Meriem Zerkouk, Miloud Mihoubi, and Belkacem Chikhaoui  
A Comprehensive Review of AI-Based Intelligent Tutoring Systems: Applications and Challenges

## Why I Chose This Paper

I chose this paper for Reading 2 because it focuses on AI-based intelligent tutoring systems. This connects directly to our project because we are building an AI tutor that should support learning, provide feedback, and adapt to course context.

The paper is useful because it discusses how intelligent tutoring systems work in real educational settings and what challenges remain in designing and evaluating them.

## Main Idea

The paper reviews AI-based Intelligent Tutoring Systems, or ITS, and explains how they can support personalized learning, adaptive instruction, real-time feedback, student modeling, and natural language interaction.

A key idea is that ITS are not just answer systems. They are educational systems designed to provide individualized instruction and feedback. They try to mimic some parts of human tutoring by adapting to student needs.

## Focus Question 1: How can retrieval improve educational support?

Retrieval can improve educational support by giving the tutor access to relevant learning materials before it responds. In an intelligent tutoring system, this can help the tutor provide feedback that is more accurate, personalized, and connected to the learning domain.

For our project, retrieval gives the AI tutor access to CISC230 course materials. This helps the tutor answer using course vocabulary and course expectations instead of relying only on general model knowledge.

Retrieval can support education by helping the tutor:

- Use course-specific vocabulary
- Explain concepts at the right level
- Connect answers to lecture or lab material
- Clarify assignment expectations
- Provide hints based on relevant course content
- Reduce unsupported guessing

This connects to the paper’s discussion of ITS features such as personalized learning, adaptive learning, real-time feedback, learner modeling, and natural language interaction.

## Connection to Our Project

In our Week 2 prototype, retrieval improved the tutor’s answer to the inheritance question. Without retrieval, the answer was correct but generic. With retrieval, the tutor used terms from the course material, such as superclass, subclass, shared behavior, and override.

This is similar to the idea of a Domain Model in ITS. The course materials act like a small domain knowledge base that the tutor can use to guide its response.

Our prototype is not a full ITS yet because it does not have a real student model or adaptive learning path. However, retrieval is an important step toward making the tutor more course-aware.

## Focus Question 2: What educational challenges remain unsolved?

Several educational challenges remain unsolved.

First, personalization is still difficult. A strong tutor should know what the student already understands, what misconceptions they have, and what level of help they need. Our current prototype does not yet track student progress or build a student model.

Second, evaluation is difficult. It is not enough to know whether the AI gives a correct answer. We also need to know whether the response helps students learn. This means we need evaluation criteria such as course alignment, scaffolding, correctness, academic-integrity safety, and educational usefulness.

Third, academic integrity remains a challenge. A tutor can help students learn, but it can also help them avoid learning if it gives full solutions. This is especially important in programming courses because models can generate complete code.

Fourth, trust and transparency are important. Students and instructors need to understand why the tutor gave a certain response. Showing retrieved course context may help, but it also raises design questions about whether retrieved context should be visible to students.

Fifth, privacy and bias remain concerns. If a future tutor stores student data, it must handle that data responsibly and avoid unfair or biased support.

## Implications for Our AI Tutor Project

This paper suggests that our tutor should eventually include more than retrieval. Future versions may need:

- A stronger course domain model
- A student model
- Better feedback strategies
- Adaptive hints
- More transparent explanations
- Strong academic-integrity rules
- Evaluation based on learning quality, not just answer correctness

## Connection to Week 2 Prototype

Our current prototype has:

- Course material retrieval
- Course-aware prompting
- A simple comparison between retrieval and no retrieval
- Academic-integrity instructions
- Displayed retrieved context

This is an early step toward an ITS-style system. The next step is to decide which real CISC230 materials should become part of the tutor’s domain knowledge.

## Overall Reflection

This reading helped me understand that an AI tutor should not just answer questions. It should support learning through feedback, guidance, personalization, and course alignment.

Retrieval is useful because it helps connect the tutor to course knowledge. However, retrieval alone does not make the system a complete intelligent tutor. The tutor still needs better student modeling, evaluation, scaffolding, and academic-integrity safeguards.

For our project, this means Week 2 is a foundation. We are building the course-aware part first, but future work should focus on making the tutor more educationally intelligent.
