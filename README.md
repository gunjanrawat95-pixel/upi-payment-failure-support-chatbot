# 💳 UPI Resolution Navigator

An AI-powered UPI payment support chatbot that helps users understand and troubleshoot common UPI payment failures using Retrieval-Augmented Generation (RAG).

## 🚀 Project Overview

UPI Resolution Navigator retrieves relevant troubleshooting guidance from a custom knowledge base and generates conversational responses using selectable AI providers.

The application currently supports:
- Groq for AI-generated responses.
- Gemini integration (currently experiencing intermittent model availability issues).

## ✨ Features

- Troubleshooting for pending payments, failed payments, debited-but-not-credited transactions, duplicate payments and suspected fraud.
- Semantic search using Sentence Transformers.
- FAISS-based vector similarity search.
- Retrieval-Augmented Generation (RAG).
- Manual AI provider selection.
- Multi-turn chat interface with conversation history.
- Clear Chat functionality.
- Reference sources for retrieved guidance.
- Safety instructions: never request UPI PINs, OTPs or passwords.

## 🛠️ Tech Stack

- Python
- Streamlit
- Sentence Transformers
- FAISS
- Google Gemini API
- Groq API
- Pytest
- GitHub Actions

## 🏗️ Project Architecture

1. User submits a UPI-related question.
2. Semantic search converts the question into an embedding.
3. FAISS retrieves the most relevant knowledge-base entry.
4. Retrieved guidance is passed to the selected AI provider.
5. The chatbot generates a conversational response.
6. The answer is displayed in the Streamlit chat interface.

## 📂 Project Structure

```text
upi-payment-failure-support-chatbot/
│
├── app.py
├── guidance.py
├── knowledge_base.py
├── retrieval.py
├── search_knowledge.py
├── semantic_search.py
├── llm_providers.py
├── test_app.py
├── test_retrieval.py
├── requirements.txt
│
└── .github/
    └── workflows/
        └── tests.yml
```

## ⚙️ Run Locally

Clone the repository:

```bash
git clone https://github.com/gunjanrawat95-pixel/upi-payment-failure-support-chatbot.git
cd upi-payment-failure-support-chatbot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure API keys using Streamlit Secrets or environment-specific secret management. Never commit API keys to GitHub.

Run the application:

```bash
streamlit run app.py
```

## 🧪 Run Tests

```bash
pytest -v
```

The retrieval test suite has previously passed 13 tests.

GitHub Actions is configured to run automated tests when code is pushed.

## 🔐 Safety and Limitations

- This is an informational prototype, not a bank or payment-provider system.
- It cannot access live transaction statuses.
- It cannot initiate refunds or reverse payments.
- Resolution timelines are not guaranteed.
- Users should never share UPI PINs, OTPs or passwords.
- Free AI API quotas and model availability may change.

## 🎯 Learning Outcomes

This project demonstrates practical experience with:
- Python application development.
- Semantic search and vector databases.
- Retrieval-Augmented Generation.
- LLM API integration.
- Prompt design and response grounding.
- Automated testing and GitHub Actions.
- Building an AI application using Streamlit.

## 👩‍💻 Author

Created as a hands-on AI and Python portfolio project.

**GitHub:** https://github.com/gunjanrawat95-pixel
