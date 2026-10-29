# UPI Resolution Navigator 💳

A Streamlit web app that helps users navigate common UPI payment problems with clear, scenario-specific troubleshooting guidance.

## 🚀 Live Demo

Add your deployed Streamlit app URL here.

## 🎯 Problem Statement

When a UPI payment is pending, fails, or appears to debit money without crediting the recipient, users may not know what to check or where to seek help. This project organizes general troubleshooting steps by payment scenario.

## ✨ Features

- **Pending payments:** Check transaction status and verify whether money was debited.
- **Failed payments:** Review transaction details and determine whether to contact official support.
- **Money debited, receiver not credited:** Different guidance for merchant and person-to-person payments.
- **Possible duplicate payment:** Compare transaction references and verify multiple debits.
- **Suspected fraud:** Prioritize contacting the bank and reporting suspected cyber financial fraud through official channels.

## 🛠️ Tech Stack

- Python
- Streamlit
- GitHub
- Streamlit Community Cloud

## ⚙️ How It Works

1. The user selects a payment problem.
2. The app displays guidance for the selected scenario.
3. For money debited without the recipient receiving it, the user selects a merchant or person-to-person payment.
4. The app provides general next steps and official-support recommendations.

## ⚠️ Limitations

- This is a prototype that provides general guidance.
- It does not connect to banks or UPI systems.
- It cannot verify transaction status or initiate refunds.
- It does not yet implement an LLM chatbot, retrieval-augmented generation (RAG), or a vector database.
- Users should verify important actions through their bank's official support channels.

## 🔮 Future Improvements

- Add a curated, verified knowledge base for UPI troubleshooting.
- Implement retrieval-augmented generation (RAG) with source-grounded answers.
- Add automated tests for each payment scenario.
- Improve the interface and add helpful links to official resources.

## 👩‍💻 What I Learned

- Writing Python logic for scenario-based guidance.
- Building a web interface using Streamlit.
- Using GitHub to version and document a project.
- Deploying a Python app with Streamlit Community Cloud.
- Designing different user journeys for distinct payment problems.
