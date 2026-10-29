
from guidance import GUIDANCE


def find_matching_scenario(question):
    question = question.lower()

    keywords = {
        "Payment is pending": ["pending", "processing", "waiting"],
        "Payment failed": ["failed", "failure", "unsuccessful"],
        "Money debited, receiver not credited": [
            "debited", "charged", "receiver", "merchant", "shop"
        ],
        "Possible duplicate payment": [
            "duplicate", "twice", "two payments", "paid twice"
        ],
        "Suspected fraud": [
            "fraud", "scam", "unauthorized", "unknown transaction"
        ],
    }

    for scenario, words in keywords.items():
        if any(word in question for word in words):
            return scenario

    return None
