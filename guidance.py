
GUIDANCE = {
    "Payment is pending": {
        "title": "Your payment is still pending",
        "steps": [
            "Open your UPI app and check the transaction status.",
            "Check your bank account statement to confirm whether money was debited.",
            "Avoid making the same payment again until you clarify the status.",
            "If unresolved, contact your UPI app or bank through its official support channel.",
        ],
    },
    "Payment failed": {
        "title": "Your payment failed",
        "steps": [
            "Confirm the transaction status in your UPI app.",
            "Check your bank statement to see whether money was debited.",
            "If money was debited, keep the transaction reference and contact official support.",
            "Do not assume a refund has occurred until you verify your account.",
        ],
    },
    
    "Possible duplicate payment": {
        "title": "You may have paid more than once",
        "steps": [
            "Open your UPI app and review the transaction history.",
            "Compare transaction reference numbers, amounts, and timestamps.",
            "Check your bank statement to confirm whether money was debited more than once.",
            "If two separate successful debits appear, save both transaction references and contact your UPI app or bank through its official support channel.",
            "Do not assume a duplicate payment will be refunded automatically."
        ],
    },
}


def get_guidance(problem):
    return GUIDANCE.get(problem)
