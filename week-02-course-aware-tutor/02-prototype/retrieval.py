from pathlib import Path
import re
from collections import Counter

COURSE_MATERIALS_DIR = Path(__file__).parent.parent / "01-course-materials"


def clean_words(text):
    """
    Convert text into lowercase words and remove very common short words.
    """
    words = re.findall(r"\b[a-zA-Z]{3,}\b", text.lower())

    stop_words = {
        "the", "and", "for", "with", "this", "that", "from", "are",
        "you", "your", "can", "should", "when", "what", "why", "how",
        "into", "they", "their", "have", "has", "not"
    }

    return [word for word in words if word not in stop_words]


def load_course_chunks():
    """
    Load course material text files and split them into paragraph-like chunks.
    """
    chunks = []

    for file_path in COURSE_MATERIALS_DIR.glob("*.txt"):
        text = file_path.read_text(encoding="utf-8")

        paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]

        for paragraph in paragraphs:
            chunks.append({
                "source": file_path.name,
                "text": paragraph
            })

    return chunks


def retrieve_context(question, top_k=3):
    """
    Retrieve the most relevant course-material chunks for a student question.
    """
    chunks = load_course_chunks()
    question_words = Counter(clean_words(question))

    scored_chunks = []

    for chunk in chunks:
        chunk_words = Counter(clean_words(chunk["text"]))

        score = 0
        for word in question_words:
            score += min(question_words[word], chunk_words[word])

        if score > 0:
            scored_chunks.append((score, chunk))

    scored_chunks.sort(key=lambda item: item[0], reverse=True)

    top_chunks = scored_chunks[:top_k]

    if not top_chunks:
        return "No directly relevant course context was found."

    context_parts = []

    for score, chunk in top_chunks:
        context_parts.append(
            f"Source: {chunk['source']}\n{chunk['text']}"
        )

    return "\n\n---\n\n".join(context_parts)
