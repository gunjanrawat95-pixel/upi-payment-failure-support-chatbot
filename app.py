
import streamlit as st

from guidance import get_guidance

st.set_page_config(
    page_title="UPI Resolution Navigator",
    page_icon="💳",
    layout="centered"
)


st.title("💳 UPI Resolution Navigator")

st.markdown(
    """
    Find clear next steps for common UPI payment problems.

    Select what happened below to get guidance tailored to your situation.
    """
)

st.caption(
    "Prototype • General guidance only • No access to live bank transactions"
)

st.divider()

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
    },
    
    "Possible duplicate payment": {
        "title": "You may have paid more than once",
        "steps": [
            "Open your UPI app and review the transaction history.",
            "Compare the transaction reference numbers, amounts, and timestamps.",
            "Check your bank statement to confirm whether money was debited more than once.",
            "If two separate successful debits appear, save both transaction references and raise a complaint through your UPI app or bank's official support channel.",
            "Do not assume a duplicate payment will be refunded automatically; follow up through official support."
        ]
    }
}



if problem == "Suspected fraud":
    st.error(
        "Act promptly if you suspect an unauthorized UPI transaction."
    )

    st.subheader("Steps to take now")

    steps = [
        "Contact your bank immediately using its official app, website, or phone number. Report the unauthorized transaction and ask what protective steps are available.",
        "If safe to do so, secure your account and UPI app. Never share your UPI PIN, OTP, or banking password with anyone.",
        "For suspected financial cyber fraud in India, call 1930 promptly and report it at https://cybercrime.gov.in/.",
        "Save transaction IDs, timestamps, messages, screenshots, and your bank complaint reference.",
        "Do not pay anyone who promises to recover your money for an upfront fee."
    ]

    for step in steps:
        st.write("•", step)


elif problem == "Money debited, receiver not credited":
    result = get_guidance(problem)

    recipient_type = st.radio(
        "Who were you paying?",
        ["A merchant or shop", "Another person"]
    )

    st.subheader(result["title"])

    for step in result["recipients"][recipient_type]:
        st.write("•", step)


    
elif get_guidance(problem):
    result = get_guidance(problem)

    st.subheader(result["title"])

    for step in result["steps"]:
        st.write("•", step)


else:
    st.info(
        "Guidance for this situation is coming next. "
        "Choose a supported payment problem to see its steps."
    )
