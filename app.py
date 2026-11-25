
import streamlit as st

from guidance import get_guidance
from semantic_search import semantic_search
from llm_providers import generate_answer


st.set_page_config(
    page_title="UPI Resolution Navigator",
    page_icon="💳",
    layout="centered"
)

st.title("💳 UPI Resolution Navigator")

st.write(
    "Your AI-powered assistant for common UPI payment problems."
)

st.info(
    "This tool provides general information. "
    "It cannot check bank transactions or guarantee refunds. "
    "Never share your UPI PIN, OTP or password."
)

# Initialize conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Provider selection
provider = st.selectbox(
    "Choose your AI model",
    ["Gemini", "Groq"]
)

# Clear conversation
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

st.divider()

# Display previous conversation
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# New question
question = st.chat_input(
    "Describe your UPI payment problem..."
)

if question:

    # Display and save user question
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    try:
        with st.chat_message("assistant"):

            with st.spinner("Finding relevant UPI guidance..."):

                # Retrieve relevant knowledge
                results = semantic_search(
                    question,
                    top_k=1
                )

                if not results:
                    answer = (
                        "I couldn't find relevant guidance. "
                        "Please describe your payment problem differently."
                    )

                else:
                    best_match = results[0]

                    if isinstance(best_match, tuple):
                        best_match = best_match[0]

                    if isinstance(best_match, dict):
                        context = best_match.get("content", "")
                        title = best_match.get(
                            "title",
                            "Relevant UPI guidance"
                        )
                    else:
                        context = str(best_match)
                        title = "Relevant UPI guidance"

                    # Add scenario-specific guidance when matched
                    scenario_guidance = ""

                    categories = {
                        "pending": "Payment pending",
                        "failed": "Payment failed",
                        "debited": "Money debited but receiver not credited",
                        "duplicate": "Possible duplicate payment",
                        "fraud": "Suspected fraud"
                    }

                    question_lower = question.lower()

                    if any(
                        word in question_lower
                        for word in ["fraud", "scam", "stolen", "unauthorized", "without permission"]
                    ):
                        scenario_guidance = get_guidance(
                            categories["fraud"]
                        )

                    elif any(
                        word in question_lower
                        for word in ["twice", "double", "duplicate", "charged twice"]
                    ):
                        scenario_guidance = get_guidance(
                            categories["duplicate"]
                        )

                    elif any(
                        word in question_lower
                        for word in ["pending", "processing", "stuck"]
                    ):
                        scenario_guidance = get_guidance(
                            categories["pending"]
                        )

                    elif any(
                        word in question_lower
                        for word in ["failed", "declined"]
                    ):
                        scenario_guidance = get_guidance(
                            categories["failed"]
                        )

                    elif any(
                        word in question_lower
                        for word in ["debited", "deducted", "not received", "not credited"]
                    ):
                        scenario_guidance = get_guidance(
                            categories["debited"]
                        )

                    if scenario_guidance:
                        context += (
                            "\n\nAdditional scenario guidance:\n"
                            + str(scenario_guidance)
                        )

                    # Add fraud emergency information
                    if scenario_guidance == get_guidance(
                        categories["fraud"]
                    ):
                        st.error(
                            "Suspected fraud? Contact your bank immediately. "
                            "In India, call 1930 and report at "
                            "https://cybercrime.gov.in/."
                        )

                    st.caption(f"Knowledge matched: {title}")

                    with st.spinner(
                        f"Generating response using {provider}..."
                    ):
                        answer = generate_answer(
                            provider,
                            question,
                            context
                        )

            st.markdown(answer)

            # Show reference sources
            if results and isinstance(best_match, dict):
                sources = best_match.get("sources", [])

                if sources:
                    with st.expander("📚 Reference sources"):
                        for source in sources:
                            st.markdown(
                                f"- [Official reference]({source})"
                            )

        # Save assistant response
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

    except Exception as error:

        error_message = (
            f"Sorry, I couldn't generate a response. "
            f"Please check the selected provider and try again. "
            f"Error: {type(error).__name__}: {error}"
        )

        with st.chat_message("assistant"):
            st.error(error_message)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": error_message
            }
        )
