
import streamlit as st
from google import genai


def ask_gemini(question, context):
    """Generate an answer using Gemini and retrieved UPI guidance."""

    client = genai.Client(
        api_key=st.secrets["GEMINI_API_KEY"]
    )

    prompt = f"""
    You are a helpful UPI payment support assistant.

    Use the following verified guidance to answer the user's question.
    Do not invent transaction statuses, refunds, or resolution timelines.
    Never ask for a UPI PIN, OTP, or password.

    Guidance:
    {context}

    User question:
    {question}

    Give a clear, simple, step-by-step answer.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
