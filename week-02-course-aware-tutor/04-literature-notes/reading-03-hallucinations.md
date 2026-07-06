# Reading 3: Why Language Models Hallucinate

## Citation

Adam Tauman Kalai, Ofir Nachum, Santosh S. Vempala, and Edwin Zhang  
Why Language Models Hallucinate

## Why I Chose This Paper

I chose this paper for Reading 3 because it directly discusses hallucinations in language models. This connects to Week 2 because one of the main questions is whether retrieval can reduce hallucinations in educational AI systems.

This paper is useful for our project because our tutor must not give confident but unsupported answers to students.

## Main Idea

The paper argues that language models hallucinate because they are often trained and evaluated in ways that reward guessing instead of admitting uncertainty.

A hallucination is when a model produces a plausible-sounding but incorrect or unsupported statement. The paper explains that hallucinations are not mysterious. They can arise from statistical errors during training and can persist because evaluation systems often reward confident answers.

## Focus Question 1: Why are hallucinations especially dangerous in educational settings?

Hallucinations are especially dangerous in education because students may trust an answer simply because it sounds confident. If the tutor gives a wrong explanation, wrong assignment advice, or unsupported example, the student may learn the wrong thing.

This is especially risky for beginner programming students because they may not yet have enough knowledge to detect mistakes.

In an educational setting, hallucinations can cause several problems:

- Students may misunderstand a concept.
- Students may follow advice that contradicts the course.
- Students may use the wrong programming language or style.
- Students may think an invented example came from the instructor.
- Students may become overconfident in incorrect knowledge.
- Students may complete work incorrectly.

## Connection to Our Project

We saw this problem in our own Week 2 prototype.

During the polymorphism test, retrieval found the correct course context. However, the model initially generated a C++ example and implied that the example came from course materials. That was not true because the retrieved context did not include that code example.

This was an educational hallucination risk. The response sounded helpful, but it went beyond the retrieved material.

Because of this, we improved the prompt by adding a rule:

Do not claim that an example, phrase, or requirement comes from the course materials unless it appears in the retrieved course context.

After this change, the tutor gave a Java example and did not falsely claim it came from course materials.

## Focus Question 2: How can retrieval reduce these risks?

Retrieval can reduce hallucination risk by giving the model external evidence before it generates an answer. Instead of relying only on internal model memory, the tutor can use course materials as grounding.

For our project, retrieval can reduce hallucination risk by helping the tutor:

- Use actual course vocabulary
- Refer to selected CISC230 materials
- Avoid unsupported guessing
- Stay aligned with the course
- Give responses that can be checked against retrieved context

Retrieval also makes the system more inspectable because we can see what context was retrieved before the model answered.

## Important Limitation

Retrieval reduces risk, but it does not eliminate hallucinations.

Our own prototype showed this clearly. Even when the retrieved context was correct, the model still added unsupported details. This means retrieval must be combined with:

- Strong prompting
- Careful document selection
- Response evaluation
- Academic-integrity rules
- Possibly source citations or visible retrieved context

## Implications for Our AI Tutor Project

This paper suggests that our tutor should be allowed to express uncertainty. It should not always guess.

For example, if the retrieved course context is limited, the tutor should say something like:

The available course context is limited, but I can give a general explanation.

This is better than pretending that the answer definitely came from the course materials.

The tutor should also distinguish between:

- Information found in retrieved course materials
- General programming knowledge
- Uncertain or missing information

## Connection to Academic Integrity

Hallucinations and academic integrity are connected. If a tutor invents assignment requirements or gives unsupported code, students may mistakenly rely on it. If retrieval includes unsafe documents, the tutor may also reveal solution material.

Therefore, reducing hallucinations is not only about correctness. It is also about responsible educational support.

## Overall Reflection

This reading helped me understand why hallucinations matter so much in educational AI. A confident answer is not always a reliable answer.

For our project, retrieval is important because it gives the tutor course context. However, retrieval is not enough by itself. The tutor also needs to be honest about uncertainty, avoid unsupported claims, and follow clear tutoring policies.

My main takeaway is that an educational AI tutor should be grounded, cautious, and transparent. It should help students learn without pretending to know more than the course materials actually provide.
