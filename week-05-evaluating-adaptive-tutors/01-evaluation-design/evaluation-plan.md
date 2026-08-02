# Week 5 Evaluation Plan

## Project Context

This project investigates whether an adaptive AI tutor can provide stronger educational support than simpler tutoring approaches while maintaining academic integrity.

During the previous stages of the project, three tutoring approaches were developed or examined:

1. A general-purpose language model that answers without course-specific retrieval or adaptive pedagogical rules.
2. A course-aware tutor that retrieves and uses CISC 230 course materials.
3. An adaptive tutor that uses course materials while adjusting its support according to student intent, demonstrated effort, and academic-integrity risk.

The purpose of this evaluation is to compare these approaches systematically rather than relying on isolated examples or personal impressions.

## Evaluation Goal

The main goal is to determine whether the adaptive tutor provides better educational support while reducing inappropriate solution disclosure.

The evaluation will examine whether each tutoring system:

* provides technically correct information,
* supports student understanding,
* aligns with CISC 230 course materials,
* encourages independent reasoning,
* responds appropriately to different levels of student effort,
* maintains academic-integrity boundaries,
* and avoids unnecessary solution leakage.

## Systems Being Compared

### System 1: General-Purpose Language Model

The general-purpose system will respond to student questions without access to CISC 230 course materials and without the adaptive decision framework.

This system represents a conventional AI chatbot.

### System 2: Course-Aware Tutor

The course-aware tutor will retrieve relevant information from CISC 230 course materials and use that information when generating responses.

This system represents the Week 2 and Week 3 course-grounded tutoring approach.

### System 3: Adaptive Tutor

The adaptive tutor will use the same course materials while also classifying student intent, estimating demonstrated effort, assessing academic-integrity risk, and selecting an appropriate level of support.

This system represents the Week 4 adaptive tutoring framework.

## Evaluation Benchmark

All three systems will be tested using the same benchmark questions.

The benchmark will include realistic student interactions from the following categories:

* concept learning,
* debugging support,
* assignment clarification,
* reflection and design reasoning,
* direct solution requests,
* and mixed or ambiguous situations.

Using the same questions for all systems will support a fair comparison.

The benchmark will include both low-effort and high-effort student requests so that the evaluation can examine whether the adaptive tutor responds differently when students demonstrate meaningful work.

## Evaluation Criteria

Each tutoring response will be evaluated using a shared rubric.

The rubric will assess:

* technical correctness,
* educational quality,
* helpfulness,
* course alignment,
* encouragement of independent thinking,
* adaptation to student intent and effort,
* academic-integrity safety,
* and solution leakage.

Each criterion will receive a numerical score with written descriptions of excellent, acceptable, and poor performance.

Solution leakage will also be classified separately as:

* safe,
* borderline,
* or unsafe.

## Evidence Collected

The evaluation will collect both quantitative and qualitative evidence.

### Quantitative Evidence

Quantitative evidence will include:

* rubric scores for each response,
* average scores by tutoring system,
* average scores by benchmark category,
* counts of safe, borderline, and unsafe responses,
* course-alignment scores,
* independent-thinking scores,
* and overall educational-quality scores.

### Qualitative Evidence

Qualitative evidence will include:

* representative response excerpts,
* descriptions of effective tutoring behavior,
* examples of solution leakage,
* examples of course misalignment,
* patterns in how systems respond to student effort,
* and observations about strengths and weaknesses.

Quantitative scores will show broad patterns, while qualitative analysis will help explain why those patterns occurred.

## Evaluation Procedure

The evaluation will follow these steps:

1. Create and validate a balanced benchmark dataset.
2. Submit every benchmark question to each tutoring system.
3. Save the complete response from each system.
4. Remove or standardize system-identifying information when practical.
5. Evaluate every response using the same rubric.
6. Classify solution leakage as safe, borderline, or unsafe.
7. Record both numerical scores and written observations.
8. Calculate summary statistics for each system and benchmark category.
9. Identify recurring strengths, weaknesses, and failure patterns.
10. Present the results using tables, figures, and narrative analysis.

## Reproducibility

To make the evaluation reproducible, the project will preserve:

* the complete benchmark dataset,
* category and effort labels,
* the evaluation rubric,
* system descriptions,
* model and configuration information,
* all generated responses,
* numerical scores,
* evaluator notes,
* analysis scripts,
* and result-generation procedures.

The same benchmark questions and rubric will be applied to all systems.

Any manual judgment, uncertainty, or change to the procedure will be documented.

## Fairness and Experimental Controls

Several controls will be used to improve fairness:

* Every system will receive the same student prompts.
* The benchmark order will remain consistent or be documented.
* Responses will not be edited before scoring.
* All systems will be evaluated using the same rubric.
* Course-aware and adaptive systems will use the same CISC 230 materials.
* Differences in model, prompt, retrieval, and adaptive behavior will be documented.
* Missing responses, system errors, and retrieval failures will be recorded instead of silently removed.

## Anticipated Limitations

This evaluation may have several limitations:

* The benchmark will be smaller than a large-scale educational dataset.
* Some benchmark questions will be researcher-created rather than collected directly from students.
* Human scoring involves judgment and may contain evaluator bias.
* A single evaluator may not measure inter-rater reliability.
* Strong tutoring responses do not directly prove long-term learning gains.
* Model responses may vary across repeated runs.
* Differences between systems may result from both prompting and system architecture.
* The evaluation will focus on CISC 230 and may not generalize to every course.

These limitations will be acknowledged when interpreting the findings.

## Expected Contribution

This evaluation will provide initial evidence about whether adaptive pedagogical guardrails improve tutoring quality.

The most important contribution is not simply showing that the adaptive tutor can answer questions. Instead, the evaluation will examine whether it provides appropriate help, responds to student effort, encourages reasoning, uses course materials responsibly, and avoids completing academic work for students.

