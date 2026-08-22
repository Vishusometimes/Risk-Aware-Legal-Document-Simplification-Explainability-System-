import streamlit as st
import pandas as pd
import re
import unicodedata
import sys
import os

# Fix path
sys.path.append(os.path.abspath("src"))

# PDF reader
from PyPDF2 import PdfReader

# Optional cleaner
try:
    import ftfy
except:
    ftfy = None

# Pipeline
from src.pipeline import process_clause


# =========================
# TEXT CLEANING
# =========================
def clean_text(text):
    if not text:
        return ""

    if ftfy:
        text = ftfy.fix_text(text)

    text = unicodedata.normalize("NFKC", text)

    # Fix weird chars
    text = text.replace("ﬁ", "fi").replace("ﬂ", "fl")
    text = text.replace("�", "")

    # Fix spacing
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    text = re.sub(r'([a-zA-Z])([0-9])', r'\1 \2', text)
    text = re.sub(r'([0-9])([a-zA-Z])', r'\1 \2', text)

    text = re.sub(r'\s+', ' ', text)

    # Ensure full sentence
    if text and text[-1] not in ".!?":
        text += "."

    return text.strip()


# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Legal Risk Analyzer", layout="wide")

st.title("📄 RRisk-Aware Legal Document Simplification and Explainability system")


# =========================
# SIDEBAR
# =========================
with st.sidebar:
    st.header("⚙️ Settings")

    input_type = st.radio("Input Type", ["Text", "PDF"])

    risk_filter = st.multiselect(
        "Filter by Risk",
        ["Very High", "High", "Medium", "Low", "Very Low"],
        default=["Very High", "High", "Medium", "Low", "Very Low"]
    )

    clause_filter = st.multiselect(
        "Filter by Clause Type",
        [
            "Legal Liability",
            "User Obligation",
            "Data & Privacy",
            "Financial Terms",
            "Intellectual Property",
            "General Information"
        ]
    )


# =========================
# INPUT
# =========================
raw_text = ""

if input_type == "Text":
    raw_text = st.text_area("Enter Legal Text", height=200)

else:
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

    if uploaded_file:
        st.info("📤 Uploading and extracting text...")

        reader = PdfReader(uploaded_file)

        for page in reader.pages:
            raw_text += page.extract_text() or ""

        raw_text = clean_text(raw_text)

        st.success("✅ PDF uploaded and processed successfully!")

        st.text_area("🔎 Preview (first 1000 chars)", raw_text[:1000], height=150)


# =========================
# TABS
# =========================
tab1, tab2, tab3 = st.tabs(["🔍 Analyze", "📊 Evaluation", "📈 Analytics"])


# =========================
# 🔍 ANALYZE TAB
# =========================
with tab1:

    if st.button("🚀 Analyze Document"):

        if not raw_text:
            st.warning("Please provide input text")
        else:
            clauses = [c.strip() for c in raw_text.split(".") if len(c.strip()) > 40]

            results = []
            progress = st.progress(0)

            for i, clause in enumerate(clauses):
                result = process_clause(clause)
                results.append(result)
                progress.progress((i + 1) / len(clauses))

            st.session_state["results"] = results

            st.success("Analysis completed!")

    # DISPLAY RESULTS
    if "results" in st.session_state:

        results = st.session_state["results"]

        # Apply filters
        filtered = []
        for r in results:
            if r["risk"] not in risk_filter:
                continue
            if clause_filter and r["type"] not in clause_filter:
                continue
            filtered.append(r)

        if not filtered:
            st.warning("⚠️ No clauses found for selected filters")
        else:
            for r in filtered:

                st.markdown("### 📌 Clause")

                st.markdown("**Original:**")
                st.write(clean_text(r.get("original", "")))

                st.markdown("**Risk:**")
                st.write(r.get("risk", "N/A"))

                st.markdown("**Explanation:**")
                st.write(clean_text(r.get("explanation", "")))

                st.markdown("**Confidence (BERT):**")
                st.write(r.get("confidence", 0))

                st.markdown("**RPS:**")
                st.write(r.get("rps", 0))

                st.markdown("**Type of Clause:**")
                st.write(r.get("type", "N/A"))

                if r.get("type") != "General Information" and r.get("reasons"):
                    st.markdown("**Why this risk:**")
                    for reason in r["reasons"]:
                        st.write(f"- {reason}")

                st.markdown("---")


# =========================
# 📊 EVALUATION TAB
# =========================
with tab2:

    if "results" not in st.session_state:
        st.info("Run analysis first")
    else:
        df = pd.DataFrame(st.session_state["results"])

        st.subheader("📊 Summary Metrics")

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Clauses", len(df))
        col2.metric("High Risk Clauses", sum(df["risk"].isin(["High", "Very High"])))
        col3.metric("Avg RPS", round(df["rps"].mean(), 2))

        st.markdown("---")

        st.markdown("### 📋 Table")

        # FULL SCROLL TABLE
        st.dataframe(df, use_container_width=True)


# =========================
# 📈 ANALYTICS TAB
# =========================
with tab3:

    if "results" in st.session_state:
        df = pd.DataFrame(st.session_state["results"])

        st.subheader("📊 Risk Distribution")
        st.bar_chart(df["risk"].value_counts())

        st.subheader("📈 Clause Types")
        st.bar_chart(df["type"].value_counts())