
from guidance import get_guidance, GUIDANCE


def test_all_five_payment_scenarios_exist():
    expected_scenarios = [
        "Payment is pending",
        "Payment failed",
        "Money debited, receiver not credited",
        "Possible duplicate payment",
        "Suspected fraud",
    ]

    for scenario in expected_scenarios:
        assert get_guidance(scenario) is not None


def test_pending_payment_has_steps():
    result = get_guidance("Payment is pending")

    assert result["title"] == "Your payment is still pending"
    assert len(result["steps"]) > 0


def test_merchant_and_person_guidance_are_different():
    result = get_guidance("Money debited, receiver not credited")

    assert "A merchant or shop" in result["recipients"]
    assert "Another person" in result["recipients"]

    merchant_steps = result["recipients"]["A merchant or shop"]
    person_steps = result["recipients"]["Another person"]

    assert merchant_steps != person_steps


def test_unknown_scenario_returns_none():
    assert get_guidance("Unknown payment problem") is None
