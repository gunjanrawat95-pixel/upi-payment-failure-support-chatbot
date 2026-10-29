
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
    
    
    "Money debited, receiver not credited": {
        "title": "Money was debited, but the receiver has not received it",
        "recipients": {
            "A merchant or shop": [
                "Check the transaction status in your UPI app.",
                "Ask the merchant to verify the payment in their account or payment system.",
                "Keep the transaction reference number and payment receipt.",
                "Avoid paying again until you clarify the original transaction.",
                "If unresolved, contact your bank or UPI app through its official support channel.",
            ],
            "Another person": [
                "Check the transaction status and confirm the UPI ID or phone number you paid.",
                "Ask the recipient to check their bank account, not only their notifications.",
                "Keep the transaction reference number and payment receipt.",
                "Avoid sending the payment again until you clarify the original transaction.",
                "If unresolved, contact your bank or UPI app through its official support channel.",
            ],
        },
    },
    
    "Suspected fraud": {
        "title": "Act promptly if you suspect an unauthorized UPI transaction",
        "steps": [
            "Contact your bank immediately using its official app, website, or phone number.",
            "Never share your UPI PIN, OTP, or banking password.",
            "For suspected financial cyber fraud in India, call 1930 promptly and report it at https://cybercrime.gov.in/.",
            "Save transaction IDs, timestamps, messages, screenshots, and your bank complaint reference.",
            "Do not pay anyone who promises to recover your money for an upfront fee."
        ],
    },
}


def get_guidance(problem):
    return GUIDANCE.get(problem)
