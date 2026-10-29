
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
}


def get_guidance(problem):
    return GUIDANCE.get(problem)
