# Week 2 Deliverables Checklist

## 1. Course Material Inventory

Status: Completed initial version.

Files:
- week-02-course-aware-tutor/01-course-materials/course_policies.txt
- week-02-course-aware-tutor/01-course-materials/oop_concepts.txt

Need to add:
- course-material-inventory.md

Summary:
I selected safe sample course materials first: course policies and object-oriented programming concepts. These materials support learning without exposing assignment solutions. The next step is to ask the professor which real CISC230 materials are safe to include.

## 2. Retrieval Reflection

Status: Completed in Week 2 reflection.

Summary:
I used a simple keyword-overlap retrieval approach. The system loads text files, splits them into chunks, compares words from the student question with words from each chunk, and returns the most relevant course context.

What worked:
- It successfully retrieved inheritance and polymorphism context.
- It was easy to understand and explain.
- It helped show the difference between generic and course-aware tutoring.

Challenges:
- It depends on exact word overlap.
- It does not deeply understand meaning.
- It can retrieve limited context.
- Retrieval does not fully prevent hallucinations.

What surprised me:
Even when retrieval found the correct context, the model could still add unsupported details. This showed that retrieval must be combined with strong prompting.

## 3. Comparison Study

Status: Completed initial examples.

Files:
- week-02-course-aware-tutor/03-comparison-study/inheritance-comparison.md

Need to add:
- polymorphism-comparison.md

Summary:
I compared tutor responses with retrieval off and retrieval on. Retrieval improved course alignment by helping the tutor use course vocabulary such as superclass, subclass, shared behavior, override, and shared type.

## 4. Literature Notes

Status: Completed/drafted.

Files:
- week-02-course-aware-tutor/04-literature-notes/reading-01-rag.md
- week-02-course-aware-tutor/04-literature-notes/reading-02-intelligent-tutoring-systems.md
- week-02-course-aware-tutor/04-literature-notes/reading-03-hallucinations.md

Summary:
The readings helped connect the technical prototype to research ideas about retrieval, intelligent tutoring systems, and hallucination risks.

## 5. Weekly Reflection

Status: Completed.

Files:
- project-notes/05-weekly-reflections/week-02-reflection.md

Need to copy to:
- week-02-course-aware-tutor/05-reflection/week-02-reflection.md

Summary:
The Week 2 reflection answers the educational objectives, technical objectives, research objectives, guiding questions, suggested activities, findings, limitations, and questions for the professor.
