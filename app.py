
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

from retrieval import find_matching_scenario

st.divider()

st.subheader("Or describe your payment problem")

question = st.text_input(
    "What happened?",
    placeholder="e.g. My account was charged but the shop didn't receive the money"
)

if question:
    matched_problem = find_matching_scenario(question)

    if matched_problem:
        st.success(f"Matched scenario: {matched_problem}")
        problem = matched_problem
    else:
        st.warning(
            "I couldn't confidently match that question. "
            "Please select a scenario from the dropdown above."
        )

if problem == "Money debited, receiver not credited":
    result = get_guidance(problem)

    recipient_type = st.radio(
        "Who were you paying?",
        ["A merchant or shop", "Another person"]
    )

    st.subheader(result["title"])

    for index, step in enumerate(
        result["recipients"][recipient_type], start=1
    ):
        with st.expander(f"Step {index}: {step}"):
            st.write(step)

else:
    result = get_guidance(problem)

    if result is None:
        st.info("Guidance for this situation is coming next.")
    else:
        if problem == "Suspected fraud":
            st.error(result["title"])
        else:
            st.subheader(result["title"])

       
        for index, step in enumerate(result["steps"], start=1):
            with st.expander(f"Step {index}: {step}"):
                st.write(step)

        if problem == "Suspected fraud":
            st.markdown(
                "[Report suspected cybercrime at the official Indian portal](https://cybercrime.gov.in/)"
            )
            st.markdown("**Cyber financial fraud helpline: 1930**")
