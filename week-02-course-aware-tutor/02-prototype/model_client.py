import os
import requests
from openai import OpenAI


def generate_with_ollama(prompt, model_name="llama3.2"):
    """
    Generate a tutor response using a local Ollama model.
    Ollama is the backend/model runner.
    llama3.2 is the model.
    """
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model_name,
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    response.raise_for_status()
    return response.json().get("response", "")


def generate_with_openai(prompt, model_name="gpt-4o-mini"):
    """
    Generate a tutor response using the OpenAI API.
    This is a non-Ollama backend for model comparison.
    """
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError(
            "OPENAI_API_KEY is not set. In Terminal, run: "
            "export OPENAI_API_KEY='your_api_key_here'"
        )

    client = OpenAI()

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content


def generate_response(prompt, backend):
    """
    Route the prompt to the selected model backend.
    """
    if backend == "Ollama - llama3.2":
        return generate_with_ollama(prompt, model_name="llama3.2")

    if backend == "OpenAI API - gpt-4o-mini":
        return generate_with_openai(prompt, model_name="gpt-4o-mini")

    raise ValueError(f"Unknown backend: {backend}")
