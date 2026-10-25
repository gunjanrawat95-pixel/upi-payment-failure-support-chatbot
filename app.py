
import streamlit as st

st.set_page_config(
    page_title="UPI Resolution Navigator",
    page_icon="💳",
    layout="centered"
)

st.title("💳 UPI Resolution Navigator")

st.write("Get guidance for common UPI payment problems.")

st.info(
    "This app provides general guidance. "
    "It cannot check your actual bank or UPI transaction status."
)

problem = st.selectbox(
    "What happened to your payment?",
    [
        "Payment is pending",
        "Payment failed",
        "Money debited, receiver not credited",
        "Possible duplicate payment",
        "Suspected fraud"
    ]
)


guidance = {
    "Payment is pending": {
        "title": "Your payment is still pending",
        "steps": [
            "Open your UPI app and check the transaction status.",
            "Check your bank account statement to confirm whether money was debited.",
            "Avoid making the same payment again until you clarify the status.",
            "If it remains unresolved, raise a complaint in your UPI app or contact your bank using its official support channel."
        ]
    },
    "Payment failed": {
        "title": "Your payment failed",
        "steps": [
            "Open the transaction details and confirm that the status is Failed.",
            "Check your bank statement to see whether any money was debited.",
            "If no money was debited, confirm the recipient and payment details before trying again.",
            "If money was debited, keep the transaction reference and raise a complaint through your UPI app or bank's official support channel.",
            "Do not assume a refund has happened until you verify your account."
        ]
    }
}

if problem in guidance:
    st.subheader(guidance[problem]["title"])

    for step in guidance[problem]["steps"]:
        st.write("•", step)

else:
    st.info(
        "Guidance for this situation is coming next. "
        "Choose Payment is pending to try the first completed scenario."
    )
