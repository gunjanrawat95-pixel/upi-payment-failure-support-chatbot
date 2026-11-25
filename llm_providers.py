
import time
import streamlit as st
from google import genai
from openai import OpenAI
from anthropic import Anthropic


def ask_gemini(question, context):
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

    prompt = f"""
You are a careful UPI payment support assistant.

Use only the retrieved guidance below. Do not invent transaction
statuses, refunds or resolution timelines.

Never ask for a UPI PIN, OTP or password.
Do not claim to have checked a live bank transaction.
If the guidance does not answer something, say so.

Retrieved UPI guidance:
{context}

User's question:
{question}

Give one natural, conversational answer.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text


def ask_gpt(question, context):
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    prompt = f"""
You are a careful UPI payment support assistant.

Use only the retrieved guidance below. Do not invent transaction
statuses, refunds or resolution timelines.

Never ask for a UPI PIN, OTP or password.
Do not claim to have checked a live bank transaction.
If the guidance does not answer something, say so.

Retrieved UPI guidance:
{context}

User's question:
{question}

Give one natural, conversational answer.
"""

    response = client.responses.create(
        model="model="gpt-6.1-terra",
        input=prompt
    )
    return response.output_text


def ask_claude(question, context):
    client = Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])

    prompt = f"""
You are a careful UPI payment support assistant.

Use only the retrieved guidance below. Do not invent transaction
statuses, refunds or resolution timelines.

Never ask for a UPI PIN, OTP or password.
Do not claim to have checked a live bank transaction.
If the guidance does not answer something, say so.

Retrieved UPI guidance:
{context}

User's question:
{question}

Give one natural, conversational answer.
"""

    response = client.messages.create(
        model="model="claude-sonnet-5-5",
        max_tokens=500,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.content[0].text
