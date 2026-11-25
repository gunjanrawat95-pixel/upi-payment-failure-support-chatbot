
import streamlit as st

from guidance import get_guidance
from semantic_search import semantic_search
from llm_providers import ask_gemini


st.set_page_config(
    page_title="UPI Resolution Navigator",
    page_icon="💳",
    layout="centered"
)

st.title("💳 UPI Resolution Navigator")

st.markdown(
    """
    Find clear next steps for common UPI payment problems.

    Describe your payment issue and get guidance from the UPI Support Assistant.
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

st.divider()

st.subheader("Describe your payment problem")

question = st.text_input(
    "What happened?",
    placeholder="e.g. My account was charged but the shop didn't receive the money"
)

best_match = None
result = None
recipient_type = None

# Retrieve relevant guidance for typed questions
if question.strip():

    results = semantic_search(question, top_k=1)

    if results:
        best_match = results[0]
        problem = best_match["category"]

        st.caption(
            f"Identified issue: {best_match['title']}"
        )

        result = get_guidance(problem)

    else:
        problem = None

        st.warning(
            "I couldn't confidently find matching UPI guidance. "
            "Please describe the issue differently or select a scenario."
        )

else:
    result = get_guidance(problem)


if problem is None:
    st.stop()


if result is None:
    st.info("Guidance for this situation is coming next.")
    st.stop()


# Collect recipient type for merchant-related problems
if problem == "Money debited, receiver not credited":

    recipient_type = st.radio(
        "Who were you paying?",
        ["A merchant or shop", "Another person"]
    )


# Display urgent fraud guidance independently of Gemini
if problem == "Suspected fraud":

    st.error(result["title"])

    for index, step in enumerate(result["steps"], start=1):
        st.write(f"**{index}.** {step}")

    st.markdown(
        "[Report suspected cybercrime at the official Indian portal](https://cybercrime.gov.in/)"
    )

    st.markdown("**Cyber financial fraud helpline: 1930**")


# Generate one integrated conversational answer
elif question.strip() and best_match is not None:

    st.divider()

    st.subheader("🤖 UPI Support Assistant")

    context = best_match["content"]

    if problem == "Money debited, receiver not credited":

        context += "\n\nAdditional recipient-specific guidance:\n"

        context += "\n".join(
            result["recipients"][recipient_type]
        )

    else:

        context += "\n\nAdditional troubleshooting guidance:\n"

        context += "\n".join(result["steps"])

    try:

        with st.spinner("Preparing your guidance..."):

            answer = ask_gemini(
                question,
                context
            )

        st.write(answer)

        st.caption(
            "AI-generated using retrieved UPI guidance. "
            "Please verify important actions with your bank or UPI app."
        )

        # Display reference links from the retrieved record
        sources = best_match.get("sources", [])

        if sources:

            with st.expander("📚 Reference sources"):

                for source in sources:
                    st.markdown(
                        f"- [Official reference]({source})"
                    )

    except Exception as error:

        st.warning(
            "The AI assistant is temporarily unavailable. "
            "Here are the available troubleshooting steps instead."
        )

        st.caption(
            f"Technical detail: {type(error).__name__}: {error}"
        )

        if problem == "Money debited, receiver not credited":

            fallback_steps = result["recipients"][recipient_type]

        else:

            fallback_steps = result["steps"]

        for index, step in enumerate(fallback_steps, start=1):
            st.write(f"**{index}.** {step}")


# Display original guidance when user selects a dropdown option
else:

    if problem == "Money debited, receiver not credited":

        st.subheader(result["title"])

        for index, step in enumerate(
            result["recipients"][recipient_type], start=1
        ):
            st.write(f"**{index}.** {step}")

    else:

        st.subheader(result["title"])

        for index, step in enumerate(result["steps"], start=1):
            st.write(f"**{index}.** {step}")
