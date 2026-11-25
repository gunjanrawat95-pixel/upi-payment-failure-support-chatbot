
import streamlit as st
from google import genai
from groq import Groq


SYSTEM_PROMPT = """
You are a careful UPI payment support assistant.

Use the retrieved guidance as your factual source.
Do not invent transaction statuses, refunds or resolution timelines.
Never ask for a UPI PIN, OTP or password.
Do not claim to have checked a live bank transaction.
If the guidance does not answer something, say so.
Give clear, practical steps in simple language.
"""


def build_prompt(question, context):
    return f"""
{SYSTEM_PROMPT}

Retrieved UPI guidance:
{context}

User's question:
{question}

Give one natural, conversational answer.
"""


def ask_gemini(question, context):
    client = genai.Client(
        api_key=st.secrets["GEMINI_API_KEY"]
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=build_prompt(question, context)
    )

    if not response.text:
        raise RuntimeError("Gemini returned an empty response.")

    return response.text


def ask_groq(question, context):
    client = Groq(
        api_key=st.secrets["GROQ_API_KEY"]
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": (
                    f"Retrieved UPI guidance:\n{context}\n\n"
                    f"User question:\n{question}"
                )
            }
        ],
        temperature=0.2,
        max_tokens=700
    )

    answer = response.choices[0].message.content

    if not answer:
        raise RuntimeError("Groq returned an empty response.")

    return answer


def generate_answer(provider, question, context):
    providers = {
        "Gemini": ask_gemini,
        "Groq": ask_groq
    }

    if provider not in providers:
        raise ValueError("Please select a valid AI provider.")

    try:
        return providers[provider](question, context)
    except Exception as error:
        raise RuntimeError(
            f"{provider} could not generate an answer: "
            f"{type(error).__name__}: {error}"
        ) from error
