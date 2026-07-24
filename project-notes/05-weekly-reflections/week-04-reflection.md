# Week 4 Reflection: Designing Adaptive AI Tutors

## Week 4 Focus

During Week 4, I focused on designing adaptive tutoring behavior. In the earlier weeks, the tutor became educationally focused, course-aware, and able to support different tutoring scenarios. This week, the main question became:

Should every student receive the same type of help?

The answer is no. Students show different levels of effort, intent, and learning needs. An effective tutor should adjust the amount of support it provides based on the situation.

This week helped me understand that adaptive tutoring is not only a technical feature. It is an educational design decision.

---

## What I Learned About Tutoring

I learned that good tutoring requires more than giving correct answers. A tutor needs to decide how much help is appropriate.

For example, a student who says “Can you write my Homework 3?” should not receive the same support as a student who says, “I created a superclass and three subclasses, but I am not sure where this method belongs.”

The second student has shown more effort and more specific thinking, so the tutor can provide more targeted guidance. The first student is asking for the tutor to complete the work, so the tutor should refuse the full solution and redirect the student toward learning support.

This helped me understand adaptive scaffolding. The tutor should provide enough help for the student to move forward, but not so much that it removes the student’s responsibility to think.

---

## What Surprised Me

What surprised me is how difficult it is to decide the right amount of help.

At first, it seems simple to say that the tutor should give hints instead of answers. But in practice, different students need different hints. Some students need a reflection question. Some need a concept explanation. Some need a debugging strategy. Some have already tried several things and need a more targeted technical hint.

This showed me that academic integrity is not only about refusing bad requests. It is also about designing better alternatives. When the tutor refuses to write homework, it should still offer useful learning support.

---

## Educational Challenges That Remain

One challenge is recognizing student effort accurately. A short question may not always mean low effort, and a long question may not always mean high effort. The tutor needs to make careful decisions based on evidence such as code attempts, error messages, reasoning, and specific confusion.

Another challenge is balancing productive struggle with frustration. If the tutor gives too much help too early, the student may not learn. But if the tutor gives too little help, the student may become stuck or discouraged.

A third challenge is making sure adaptive behavior stays course-aligned. The tutor should continue using CISC 230 materials and avoid unsupported examples, even when it adapts its response.

---

## Aspects of the Tutor That Need the Most Improvement

The tutor needs the most improvement in adaptive decision-making.

Right now, the project has a design framework for intent categories, effort levels, and support levels. The next technical step is to integrate that framework into the prototype so the tutor can classify a student request and choose an appropriate response strategy.

The tutor also needs more testing with realistic student questions, especially:

- direct solution requests
- low-effort debugging questions
- high-effort debugging questions
- assignment clarification
- design reflection questions

These tests will help determine whether the adaptive framework improves tutoring quality.

---

## Ideas to Explore Next

Next, I would like to integrate the adaptive decision framework into the tutor code.

The tutor should be able to identify:

1. Student intent
2. Student effort level
3. Academic-integrity risk
4. Recommended support level

Then the tutor should generate a response based on those decisions.

I would also like to compare non-adaptive and adaptive responses to the same student question. This would help show whether adaptive tutoring improves educational quality.

---

## Overall Reflection

Week 4 helped me understand the central research contribution of the project. The goal is not just to build a chatbot that answers CISC 230 questions. The goal is to design a tutor that makes educational decisions.

A strong adaptive tutor should recognize student intent, consider student effort, protect academic integrity, and choose the right level of support. It should encourage productive struggle while still helping students move forward.

My main takeaway is:

Adaptive tutoring means giving the right amount of help at the right time. The tutor should support learning without replacing the student’s thinking.
