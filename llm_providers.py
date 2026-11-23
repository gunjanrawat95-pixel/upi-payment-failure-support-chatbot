
import streamlit as st
from google import genai


def ask_gemini(question, context):
    """Generate an answer using Gemini with a fallback model."""

    client = genai.Client(
        api_key=st.secrets["GEMINI_API_KEY"]
    )

    prompt = f"""
    You are a helpful UPI payment support assistant.

    Use the following guidance to answer the user's question.
    Do not invent transaction statuses, refunds, or resolution timelines.
    Never ask for a UPI PIN, OTP, or password.

    Guidance:
    {context}

    User question:
    {question}

    Give a clear, simple, step-by-step answer.
    """

    models = [
        "gemini-3.8-flash",
        "gemini-2.5-flash"
    ]

    last_error = None

    for model in models:
        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt
            )

            if response.text:
                return response.text

        except Exception as error:
            last_error = error

    raise RuntimeError(
        f"All Gemini models failed. Last error: {last_error}"
    )
