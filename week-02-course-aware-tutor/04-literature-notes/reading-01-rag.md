# Reading 1: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

## Citation

Patrick Lewis et al.  
Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

## Main Idea

The paper introduces Retrieval-Augmented Generation, or RAG. RAG combines two kinds of memory:

1. Parametric memory: knowledge stored inside a pre-trained language model.
2. Non-parametric memory: external documents that can be retrieved and used during generation.

Instead of relying only on what the language model already “knows,” RAG retrieves relevant documents first and then generates an answer using those documents as context.

## Focus Question 1: What problem is retrieval solving?

Retrieval solves the problem that language models cannot always access, update, or explain their knowledge reliably.

The paper explains that large pre-trained language models can store factual knowledge in their parameters, but their ability to precisely access and manipulate that knowledge is limited. They may also hallucinate, and it can be difficult to know where their answers came from.

Retrieval helps by giving the model access to explicit external documents. This means the model does not have to rely only on internal memory. It can use retrieved evidence when generating an answer.

## Connection to Our Project

This directly connects to our course-aware AI tutor. In Week 1, our tutor relied only on the language model. It could answer programming questions, but the answers were generic and not grounded in CISC230.

In Week 2, we added retrieval from course-material files. This helps solve a similar problem: the model should not rely only on general programming knowledge. It should use CISC230 course context before answering.

Our prototype changed from:

Student question → AI model

to:

Student question → retrieved CISC230 material → AI model

This is a simplified version of the RAG idea.

## Focus Question 2: Why not simply rely on the language model?

We should not rely only on the language model because the model may give confident but unsupported answers. It may also use outdated, irrelevant, or overly general knowledge.

The paper points out several limitations of parametric-only models:

- They cannot easily update their memory.
- They cannot straightforwardly show where an answer came from.
- They may hallucinate.
- They may perform worse on knowledge-intensive tasks.

For an educational tutor, these problems are serious. A student may trust the answer because it sounds confident, even if it does not match the course.

## Connection to Our Project

This happened in our Week 2 testing. When retrieval was off, the tutor could still answer “What is inheritance?” but the answer was generic. It was not clearly connected to CISC230.

When retrieval was on, the tutor used course-related language such as superclass, subclass, shared behavior, and override.

This showed that relying only on the model is not enough for a course-aware tutor. The tutor needs access to course materials so it can align with what students are actually learning.

## Focus Question 3: How does retrieval improve reliability?

Retrieval improves reliability by giving the model relevant evidence before it generates an answer. The model can condition its response on retrieved documents instead of relying only on internal memory.

The paper reports that RAG models generated more factual, specific, and diverse responses than a parametric-only BART baseline. The paper also notes that RAG can reduce hallucination and make the model’s knowledge easier to inspect because retrieved documents can be viewed.

Another important reliability benefit is that the external knowledge source can be updated. The paper discusses replacing the document index to update the model’s knowledge without retraining the whole model.

## Connection to Our Project

In our tutor, retrieval improves reliability by giving the model course context before it answers. The tutor can use information from selected course materials instead of guessing.

For example, when the student asked “What is inheritance?”, the system retrieved this course context:

Inheritance allows one class to reuse fields and methods from another class.  
The superclass contains shared behavior, and the subclass can add or override behavior.

The tutor then used that context in its response. This made the answer more course-aligned and easier to evaluate.

However, our testing also showed that retrieval does not completely remove hallucination. During the polymorphism test, the tutor retrieved correct context but initially generated an unsupported example and implied it came from course materials. This showed that retrieval improves reliability, but it must be combined with strong prompting and careful evaluation.

## Implications for Our AI Tutor Project

This paper supports the direction of our Week 2 prototype. It suggests that a course-aware tutor should not rely only on the model’s internal knowledge. Instead, it should retrieve relevant course materials and use them to guide its response.

For our project, RAG has several implications:

1. Course materials can act as the tutor’s non-parametric memory.
2. Retrieval can improve course alignment.
3. Retrieved context can make responses easier to inspect.
4. Updating course materials may be easier than retraining the model.
5. Retrieval may reduce hallucinations, but it does not eliminate them.
6. Document selection is important because unsafe documents could expose assignment solutions.

## Important Limitation

The paper also reminds us that external knowledge sources are not automatically perfect. If the retrieved documents contain bias, incorrect information, or unsafe material, the generated response may still be problematic.

For our project, this means we need to carefully choose which CISC230 documents the tutor can access. Lecture notes and concept explanations may support learning, but solutions and answer keys could create academic-integrity risks.

## Overall Reflection

This reading helped me understand why retrieval matters for educational AI. A language model alone may produce fluent and confident answers, but that does not mean the answers are grounded in the course.

Retrieval gives the tutor access to course-specific information, making it more reliable and course-aware. However, retrieval is not a complete solution. The tutor still needs careful prompts, safe document selection, and academic-integrity policies.

My main takeaway is that RAG is useful because it combines the flexibility of language generation with the grounding of external documents. For our project, this means CISC230 materials can help transform the tutor from a generic chatbot into a course-aware learning assistant.
