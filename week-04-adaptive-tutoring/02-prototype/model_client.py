import os
import requests


OLLAMA_URL = "http://localhost:11434/api/chat"


def call_ollama(messages, model="llama3.2"):
    """
    Calls the local Ollama model.
    This is used for course-grounded CISC 230 tutoring mode.
    """

    payload = {
        "model": model,
        "messages": messages,
        "stream": False,
        "options": {
            "temperature": 0,
            "seed": 42,
        },
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=120)
    response.raise_for_status()

    data = response.json()
    return data["message"]["content"]


def call_openai(messages, model="gpt-4o-mini"):
    """
    Optional OpenAI call for comparison mode only.
    This should NOT be used when Use CISC 230 Materials is checked.
    """

    from openai import OpenAI

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set.")

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )

    return response.choices[0].message.content


def get_model_response(messages, use_course_materials, selected_backend):
    """
    Decides which model backend to use.

    Important rule:
    If use_course_materials is True, OpenAI is disabled.
    The tutor must use local Ollama with retrieved CISC 230 materials.
    """

    if use_course_materials:
        return call_ollama(messages, model="llama3.2")

    if selected_backend == "OpenAI":
        return call_openai(messages)

    return call_ollama(messages, model="llama3.2")
