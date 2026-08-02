from pathlib import Path
import re


COURSE_MATERIALS_DIR = Path(__file__).resolve().parents[1] / "00-course-materials"

STOP_WORDS = {
    "a", "an", "the", "and", "or", "but",
    "is", "are", "was", "were", "be", "been", "being",
    "what", "why", "how", "when", "where", "which", "who",
    "do", "does", "did", "can", "could", "should", "would",
    "i", "you", "we", "they", "he", "she", "it", "am",
    "to", "of", "in", "on", "for", "from", "with", "about",
    "between", "this", "that", "these", "those",
    "me", "my", "your", "our", "their",
    "as", "not", "one", "three", "created",
    "java", "cisc", "course", "materials"
}


TOPIC_FILE_BOOSTS = {
    "inheritance": ["chapter-9", "oop_concepts"],
    "superclass": ["chapter-9", "oop_concepts"],
    "subclass": ["chapter-9", "oop_concepts"],
    "subclasses": ["chapter-9", "oop_concepts"],
    "abstract": ["chapter-9"],
    "polymorphism": ["chapter-10", "polymorphism-case-study", "oop_concepts"],
    "constructor": ["chapter-4", "lecture-01-classes-objects"],
    "constructors": ["chapter-4", "lecture-01-classes-objects"],
    "class": ["chapter-1", "chapter-4", "lecture-01-classes-objects", "oop_concepts"],
    "object": ["chapter-1", "chapter-4", "lecture-01-classes-objects", "oop_concepts"],
    "encapsulation": ["chapter-4"],
    "interface": ["chapter-7", "chapter-10"],
    "interfaces": ["chapter-7", "chapter-10"],
    "arraylist": ["chapter-5"],
    "arrays": ["chapter-8"],
    "array": ["chapter-8"],
    "exception": ["codes"],
    "nullpointerexception": ["codes"],
}


def clean_text(text):
    return re.sub(r"\s+", " ", text).strip()


def tokenize(text):
    words = re.findall(r"\b[a-zA-Z_][a-zA-Z0-9_]*\b", text.lower())
    return {word for word in words if word not in STOP_WORDS}


def split_into_chunks(source, text):
    text = text.replace("\r\n", "\n")

    if "--- Slide" in text:
        pieces = re.split(r"(?=--- Slide \d+ ---)", text)
    else:
        pieces = re.split(r"\n\s*\n", text)

    chunks = []

    for piece in pieces:
        cleaned = clean_text(piece)

        if len(cleaned) < 40:
            continue

        lowered = cleaned.lower()
        skip_phrases = [
            "outline",
            "summary",
            "copyright",
            "end of lecture",
        ]

        # Skip file metadata such as:
        # "Source file: Polymorphism Case Study.pptx"
        if lowered.startswith("source file:"):
            continue

        # Skip chunks that are mostly navigation or non-content slides.
        if any(phrase in lowered for phrase in skip_phrases) and len(cleaned) < 450:
            continue

        slide_match = re.search(r"--- Slide (\d+) ---", piece)

        # Remove the slide marker before checking whether a slide has
        # enough instructional content.
        content_without_slide_marker = re.sub(
            r"--- Slide \d+ ---\s*",
            "",
            cleaned,
        ).strip()

        # Remove common slide footer text before deciding whether a slide
        # contains enough instructional content.
        content_for_quality_check = re.sub(
            r"\b\d{1,2}/\d{1,2}/\d{4}\b\s+"
            r"CISC230 Object Oriented Design and Programming\s+\d+\s*$",
            "",
            content_without_slide_marker,
            flags=re.IGNORECASE,
        ).strip()

        # Skip title slides and short section-heading slides.
        # Footer text should not make a weak slide appear informative.
        if slide_match and len(content_for_quality_check.split()) < 12:
            continue
        if slide_match:
            chunk_source = f"{source} :: Slide {slide_match.group(1)}"
        else:
            chunk_source = source

        chunks.append(
            {
                "source": chunk_source,
                "content": cleaned,
            }
        )

    return chunks


def load_course_chunks():
    chunks = []

    if not COURSE_MATERIALS_DIR.exists():
        return chunks

    for path in sorted(
        COURSE_MATERIALS_DIR.rglob("*.txt"),
        key=lambda item: str(item).lower(),
    ):
        if path.name.lower() == "readme.txt":
            continue

        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
            source = str(path.relative_to(COURSE_MATERIALS_DIR))
            chunks.extend(split_into_chunks(source, text))
        except Exception as e:
            print(f"Could not read {path}: {e}")

    return chunks


def file_boost_for_question(question_tokens, source):
    source_lower = source.lower()
    boost = 0

    for token in question_tokens:
        preferred_sources = TOPIC_FILE_BOOSTS.get(token, [])
        for preferred in preferred_sources:
            if preferred in source_lower:
                boost += 3

    return boost


def retrieve_course_context(question, max_results=4):
    chunks = load_course_chunks()

    if not chunks:
        return []

    question_tokens = tokenize(question)
    scored_chunks = []

    for chunk in chunks:
        chunk_tokens = tokenize(chunk["content"])
        overlap = question_tokens.intersection(chunk_tokens)

        if not overlap:
            continue

        score = len(overlap)
        score += file_boost_for_question(question_tokens, chunk["source"])

        scored_chunks.append(
            {
                "source": chunk["source"],
                "content": chunk["content"],
                "score": score,
                "matched_terms": sorted(overlap),
            }
        )

    scored_chunks.sort(
        key=lambda item: (
            -item["score"],
            item["source"].lower(),
            item["content"].lower(),
        )
    )

    return scored_chunks[:max_results]


def shorten_content(content, max_chars=900):
    if len(content) <= max_chars:
        return content

    return content[:max_chars].rstrip() + "..."


def format_retrieved_context(results):
    if not results:
        return "No directly relevant CISC 230 course material was retrieved."

    formatted_sections = []

    for result in results:
        matched_terms = ", ".join(result.get("matched_terms", []))

        formatted_sections.append(
            f"Source: {result['source']}\n"
            f"Matched terms: {matched_terms}\n"
            f"Content: {shorten_content(result['content'])}"
        )

    return "\n\n---\n\n".join(formatted_sections)
