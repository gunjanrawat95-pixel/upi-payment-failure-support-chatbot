
import time
import streamlit as st
from google import genai


def ask_gemini(question, context):
    """Generate a grounded UPI support answer with retries and fallback."""

    client = genai.Client(
        api_key=st.secrets["GEMINI_API_KEY"]
    )

    prompt = f"""
You are a careful UPI payment support assistant.

Answer the user's question using the retrieved guidance below.

Rules:
- Use the supplied guidance as your factual source.
- Do not invent transaction statuses, refunds or resolution timelines.
- Never ask for a UPI PIN, OTP or password.
- If the guidance does not answer something, say so.
- Give clear, practical steps in simple language.
- Do not claim to have checked a live bank transaction.

Retrieved UPI guidance:
{context}

User's question:
{question}

Write one natural, conversational answer.
"""

    models = [
        "gemini-3.8-flash",
        "gemini-3.7-flash"
    ]

    delays = [2, 5, 10]

    errors = []

    for model in models:

        for attempt, delay in enumerate(delays):

            try:
                response = client.models.generate_content(
                    model=model,
                    contents=prompt
                )

                if response.text:
                    return response.text

                errors.append(
                    f"{model}: empty response"
                )

            except Exception as error:

                errors.append(
                    f"{model}, attempt {attempt + 1}: "
                    f"{type(error).__name__}: {error}"
                )

                # Retry only temporary server errors
                if "503" in str(error) or "UNAVAILABLE" in str(error):
                    if attempt < len(delays) - 1:
                        time.sleep(delay)
                        continue

                # Try the fallback model for other errors
                break

    raise RuntimeError(
        "Gemini models could not generate an answer. "
        + " | ".join(errors)
    )
