# UPI Payment-Failure Support Chatbot

An AI-powered customer support chatbot designed to help users understand failed UPI payments using Retrieval-Augmented Generation (RAG).

## Project Overview

Failed digital payments can leave users confused about transaction status, refunds, pending payments, and the next steps to take.

This project aims to build a chatbot that retrieves relevant information from trusted public documentation and uses a Large Language Model (LLM) to generate helpful, grounded answers.

The goal is to make answers more transparent by showing their sources and reducing unsupported AI-generated claims.

## Problem Statement

Users experiencing UPI payment failures often need clear guidance on:
- Pending or failed transactions
- Refund and reversal processes
- Transaction status and complaint procedures
- Where to seek help when a problem remains unresolved

The chatbot will provide informational guidance based on its indexed documents. It will not access bank accounts, process transactions, or guarantee refund timelines.

## Planned Features

- **Retrieval-Augmented Generation (RAG):** Retrieve relevant passages from a curated document collection.
- **Semantic search:** Find relevant information using text embeddings and a vector database.
- **Source citations:** Show which documents support each answer.
- **Hallucination safeguards:** Respond cautiously when the available sources do not support an answer.
- **Human escalation guidance:** Direct users to appropriate official support channels when necessary.
- **Evaluation:** Test answer correctness, retrieval quality, citation accuracy, and unsupported claims.
- **Web interface:** Provide an interactive chatbot using Streamlit.

## Technology Stack

- Python
- Streamlit
- Retrieval-Augmented Generation (RAG)
- Embeddings and vector search
- ChromaDB
- LLM API (Claude or another suitable provider)
- RAG evaluation and testing

## How It Will Work

1. Collect relevant public documentation and FAQs.
2. Clean the documents and split them into searchable passages.
3. Convert passages into vector embeddings.
4. Store the embeddings in a vector database.
5. Retrieve relevant passages when a user asks a question.
6. Generate an answer grounded in the retrieved information.
7. Display the answer, supporting sources, and escalation guidance where appropriate.

## Evaluation Plan

The project will use a test set of questions with reference answers to assess:

- Retrieval relevance
- Answer correctness and faithfulness
- Citation accuracy
- Appropriate handling of questions with insufficient evidence
- Response latency and estimated cost per query

Evaluation results will be reported after running the tests. No performance figures are claimed at this stage.

## Responsible AI and Limitations

- This project is an educational prototype, not an official NPCI or bank service.
- It will not request UPI PINs, OTPs, passwords, or other payment credentials.
- Users should verify important payment information with their bank or official support channels.
- Answers depend on the coverage, accuracy, and freshness of the indexed documents.
- API credentials will be stored outside the source code.

## Project Status

**In progress:** Repository created; implementation, testing, and deployment are planned next.

## Run Locally

Local setup instructions will be added after the initial application and its dependencies are implemented.

## Future Improvements

- Expand the verified documentation collection.
- Add multilingual support.
- Improve retrieval and answer evaluation.
- Add structured feedback and error analysis.
- Deploy a public interactive demo.

## Disclaimer

This is an independent educational project. It is not affiliated with or endorsed by NPCI, any bank, or any payment service provider.
# upi-payment-failure-support-chatbot
An AI-powered UPI payment failure support chatbot using Retrieval-Augmented Generation (RAG), source citations, and answer evaluation.
