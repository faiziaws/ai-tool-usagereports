import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Tool Usage Reports – India",
    layout="wide"
)

# ---------------- TITLE ----------------
st.title("AI Tool Usage Reports – India")
st.subheader("Location-wise AI Tool Usage by Users")

st.markdown(
    """
    This dashboard presents **location-wise usage of popular AI tools in India**.
    The data helps understand regional adoption trends of AI technologies.
    """
)

# ---------------- DATA (ALL COLUMNS SAME LENGTH) ----------------
data = {
    "State": [
        "Delhi", "Maharashtra", "Jharkhand", "Bihar",
        "Odisha", "Odisha", "Bihar", "Karnataka"
    ],
    "City": [
        "New Delhi", "Mumbai", "Ranchi", "Patna",
        "Bhubaneswar", "Cuttack", "Jamshedpur", "Bengaluru"
    ],
    "AI Tool": [
        "ChatGPT", "Copilot", "Gemini", "ChatGPT",
        "Perplexity", "ChatGPT", "Gemini", "Copilot"
    ],
    "Usage Count": [
        13, 11, 9, 7, 5, 6, 4, 10
    ]
}

df = pd.DataFrame(data)

# ---------------- DISPLAY TABLE ----------------
st.dataframe(df, use_container_width=True)

# ---------------- BASIC INSIGHTS ----------------
st.markdown("### 📊 Summary Insights")

col1, col2, col3 = st.columns(3)

col1.metric("Total Records", len(df))
col2.metric("Total AI Tools", df["AI Tool"].nunique())
col3.metric("Top State", df["State"].mode()[0])

# ---------------- FOOTER ----------------
st.success("Logical Endpoint: /aitool-usagereports")

st.markdown(
    """
    **Project Name:** Location-wise AI Tools Used by Users in India  
    **Technology Used:** DBMS, AI (ChatGPT), Streamlit Cloud  
    **Developed as:** BCA DBMS Mini Project
    """
)
