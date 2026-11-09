
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
    
def test_charged_twice_matches_duplicate_payment():
    assert find_matching_scenario("I was charged twice") == "Possible duplicate payment"


def test_paid_twice_matches_duplicate_payment():
    assert find_matching_scenario("I paid twice for the same order") == "Possible duplicate payment"


def test_stole_money_matches_fraud():
    assert find_matching_scenario("Someone stole money from my account") == "Suspected fraud"


def test_without_permission_matches_fraud():
    assert find_matching_scenario("Someone used my account without my permission") == "Suspected fraud"

