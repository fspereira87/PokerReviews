import os
import streamlit as st
from main import PokerReviewCrew
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

# Secure API Key
if "OPENAI_API_KEY" not in os.environ:
    if "OPENAI_API_KEY" in st.secrets:
        os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
    else:
        os.environ["OPENAI_API_KEY"] =st.error("OPENAI_API_KEY not found.")
        st.stop()

st.set_page_config(
    page_title="Poker Review AI Crew",
    layout="wide"
)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("🤖 Poker Review Agent Team")

    st.markdown("""
**🔎 Operator Intelligence Researcher**  
Collects verified poker operator data.

**📊 SERP Intelligence Analyst**  
Analyzes keyword opportunities.

**🧱 Review Architect**  
Designs structured review format.

**✍️ Review Writer**  
Generates full review content.

**🚀 SEO Optimizer**  
Optimizes ranking performance.

**⚖️ Compliance Reviewer**  
Ensures regulatory safety.

**🧑‍⚖️ Editorial Supervisor**  
Prepares publication-ready output.
""")

# ---------------- MAIN ----------------
st.title("♠️ Poker Operator Review Automation")

st.markdown(
    "Generate structured, SEO-optimized poker operator reviews "
    "with built-in compliance validation."
)

operator_input = st.text_input(
    "Operator Name or URL:",
    placeholder="e.g. GGPoker or https://ggpoker.com"
)

if st.button("Generate Review"):

    if not operator_input:
        st.error("Please enter an operator name or URL.")
    else:
        st.subheader("🚀 Running Poker Review Crew...")

        log_area = st.empty()
        logs = []

        def stream_log(log_line):
            logs.append(log_line)
            log_area.markdown("```\n" + "\n".join(logs) + "\n```")

        poker_crew = PokerReviewCrew(
            operator_input,
            log_callback=stream_log
        )

        with st.spinner("Agents are working..."):
            result = poker_crew.run()

        # ---------------- STRUCTURED HANDLING ----------------

        if isinstance(result, dict):
            review_content = result.get("final_review", "")
            meta_data = result.get("meta", {})
            compliance_flags = result.get("compliance_flags", [])
            editor_summary = result.get("editor_summary", "")
        else:
            # Fallback if raw text returned
            review_content = result
            meta_data = {}
            compliance_flags = []
            editor_summary = ""

        # ---------------- TABS ----------------

        tab1, tab2, tab3, tab4 = st.tabs(
            ["📄 Review", "🚀 SEO Metadata", "⚖️ Compliance", "📜 Logs"]
        )

        # ---- TAB 1: REVIEW ----
        with tab1:
            if review_content:
                st.markdown(review_content)

                st.download_button(
                    label="⬇️ Download Markdown",
                    data=str(review_content),
                    file_name=f"{operator_input}_review.md",
                    mime="text/markdown"
                )

                html_content = f"<html><body>{review_content}</body></html>"

                st.download_button(
                    label="⬇️ Download HTML",
                    data=html_content.encode("utf-8"),
                    file_name=f"{operator_input}_review.html",
                    mime="text/html"
                )
            else:
                st.warning("No review content returned.")


        # ---- TAB 2: SEO METADATA ----
        with tab2:
            if meta_data:
                st.json(meta_data)

                st.download_button(
                    label="⬇️ Download SEO Metadata (JSON)",
                    data=json.dumps(meta_data, indent=2),
                    file_name=f"{operator_input}_seo_metadata.json",
                    mime="application/json"
                )
            else:
                st.info("No structured SEO metadata returned.")


        # ---- TAB 3: COMPLIANCE ----
        with tab3:
            if compliance_flags:
                st.warning("⚠️ Compliance Flags Found:")
                for flag in compliance_flags:
                    st.write(f"- {flag}")

                st.download_button(
                    label="⬇️ Download Compliance Report",
                    data=json.dumps(compliance_flags, indent=2),
                    file_name=f"{operator_input}_compliance.json",
                    mime="application/json"
                )
            else:
                st.success("✅ No compliance issues detected.")

            if editor_summary:
                st.subheader("🧑‍⚖️ Editorial Summary")
                st.write(editor_summary)


        # ---- TAB 4: LOGS ----
        with tab4:
            if logs:
                log_text = "\n".join(logs)
                st.markdown(f"```\n{log_text}\n```")

                st.download_button(
                    label="⬇️ Download Logs",
                    data=log_text,
                    file_name=f"{operator_input}_logs.txt",
                    mime="text/plain"
                )
            else:
                st.info("No logs available.")

        st.success("✅ Review generation completed. Manual verification required before publication.")
