
from retrieval import find_matching_scenario


def test_pending_question():
    assert find_matching_scenario(
        "My payment is still pending"
    ) == "Payment is pending"


def test_merchant_not_credited():
    assert find_matching_scenario(
        "My account was debited but the shop did not receive money"
    ) == "Money debited, receiver not credited"


def test_duplicate_payment():
    assert find_matching_scenario(
        "I accidentally paid twice"
    ) == "Possible duplicate payment"


def test_suspected_fraud():
    assert find_matching_scenario(
        "I see an unauthorized transaction"
    ) == "Suspected fraud"


def test_unknown_question():
    assert find_matching_scenario(
        "How do I change my phone wallpaper?"
    ) is None

def test_charged_twice_matches_duplicate_payment():
    assert find_matching_scenario("I was charged twice") == "Possible duplicate payment"


def test_paid_twice_matches_duplicate_payment():
    assert find_matching_scenario("I paid twice for the same order") == "Possible duplicate payment"


def test_stole_money_matches_fraud():
    assert find_matching_scenario("Someone stole money from my account") == "Suspected fraud"


def test_without_permission_matches_fraud():
    assert find_matching_scenario("Someone used my account without my permission") == "Suspected fraud"
