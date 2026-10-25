
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


if problem == "Money debited, receiver not credited":
    recipient_type = st.radio(
        "Who were you paying?",
        ["A merchant or shop", "Another person"]
    )

    st.subheader("Money was debited, but the receiver hasn't received it")

    if recipient_type == "A merchant or shop":
        steps = [
            "Check the transaction status in your UPI app.",
            "Ask the merchant to verify the payment in their own account or payment system.",
            "Keep the UPI transaction reference number and payment receipt.",
            "If the payment remains unresolved, raise a complaint through your UPI app or bank's official support channel.",
            "Avoid paying again until you have clarified the original transaction."
        ]
    else:
        steps = [
            "Check the transaction status and UPI ID or phone number you paid.",
            "Ask the recipient to check their bank account, not just their notification.",
            "Keep the transaction reference number and payment receipt.",
            "If the recipient still hasn't received the money, contact your bank or UPI app through its official support channel.",
            "Avoid sending the payment again until you have clarified the original transaction."
        ]

    for step in steps:
        st.write("•", step)

elif problem in guidance:
    st.subheader(guidance[problem]["title"])

    for step in guidance[problem]["steps"]:
        st.write("•", step)

else:
    st.info(
        "Guidance for this situation is coming next. "
        "Choose a supported payment problem to see its steps."
    )
