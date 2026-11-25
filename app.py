
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
    "Get practical guidance for common UPI payment problems."
)

st.info(
    "This tool provides general information. "
    "It cannot check your bank transaction or guarantee a refund."
)

provider = st.selectbox(
    "Choose your AI model",
    ["Gemini", "Groq"]
)

problem = st.selectbox(
    "Select your payment problem",
    [
        "Select a problem",
        "Payment pending",
        "Payment failed",
        "Money debited but receiver not credited",
        "Possible duplicate payment",
        "Suspected fraud"
    ]
)

question = st.text_input(
    "Describe your problem",
    placeholder="Example: I paid a shopkeeper but they did not receive the money."
)

if st.button("Get support", type="primary"):

    if problem == "Select a problem" and not question.strip():
        st.warning("Please select a problem or enter your question.")

    else:
        try:
            search_question = question.strip()

            if not search_question:
                search_question = problem

            with st.spinner("Finding relevant UPI guidance..."):

                results = semantic_search(
                    search_question,
                    top_k=1
                )

                if not results:
                    st.warning("No matching guidance found. Please try another description.")
                    st.stop()

                best_match = results[0]

                if isinstance(best_match, tuple):
                    best_match = best_match[0]

                if isinstance(best_match, dict):
                    context = best_match.get("content", "")
                else:
                    context = str(best_match)

                scenario_guidance = ""

                if problem != "Select a problem":
                    scenario_guidance = get_guidance(problem)

                if scenario_guidance:
                    context += (
                        "\n\nAdditional scenario guidance:\n"
                        + str(scenario_guidance)
                    )

            st.subheader("Relevant knowledge")

            if isinstance(best_match, dict):
                st.write(
                    best_match.get("title", "Relevant UPI guidance")
                )

            if problem == "Suspected fraud":
                st.error(
                    "If you suspect UPI fraud, contact your bank "
                    "immediately. In India, call 1930 and report at "
                    "https://cybercrime.gov.in/."
                )

            with st.spinner(f"Generating answer using {provider}..."):

                answer = generate_answer(
                    provider,
                    search_question,
                    context
                )

            st.subheader("Your UPI support answer")
            st.write(answer)

            sources = (
                best_match.get("sources", [])
                if isinstance(best_match, dict)
                else []
            )

            if sources:
                with st.expander("📚 Reference sources"):
                    for source in sources:
                        st.markdown(
                            f"- [Official reference]({source})"
                        )

        except Exception as error:
            st.error(str(error))
            st.info(
                "Check your API key, model availability, "
                "free-tier quota and deployment logs."
            )
