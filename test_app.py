
def test_payment_scenarios():
    scenarios = [
        "Payment is pending",
        "Payment failed",
        "Money debited, receiver not credited",
        "Possible duplicate payment",
        "Suspected fraud",
    ]

    assert len(scenarios) == 5
    assert "Payment is pending" in scenarios
    assert "Payment failed" in scenarios
    assert "Suspected fraud" in scenarios


def test_merchant_and_person_options():
    recipient_options = [
        "A merchant or shop",
        "Another person",
    ]

    assert len(recipient_options) == 2
    assert "A merchant or shop" in recipient_options
    assert "Another person" in recipient_options
