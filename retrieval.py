
KEYWORDS = {
    "Possible duplicate payment": [
        "charged twice",
        "paid twice",
        "payment twice",
        "duplicate",
        "twice",
        "two payments"
    ],

    "Suspected fraud": [
        "fraud",
        "scam",
        "unauthorized",
        "unknown transaction",
        "strange transaction",
        "money stolen",
        "stole money",
        "someone stole",
        "stolen from my account",
        "not my transaction",
        "without my permission"
    ],

    "Payment is pending": [
        "pending",
        "processing",
        "waiting",
        "stuck",
        "not completed",
        "taking too long"
    ],

    "Payment failed": [
        "failed",
        "failure",
        "unsuccessful",
        "declined",
        "rejected"
    ],

    "Money debited, receiver not credited": [
        "debited",
        "deducted",
        "receiver",
        "merchant",
        "shop",
        "not credited",
        "not received"
    ]
}


def find_matching_scenario(question):
    question = question.lower()

    for scenario, words in KEYWORDS.items():
        for word in words:
            if word in question:
                return scenario

    return None
