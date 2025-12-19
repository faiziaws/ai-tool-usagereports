import streamlit as st
import pandas as pd

st.title("AI Tool Usage Reports – India")
st.subheader("Location-wise AI Tool Usage")

data = {
    "State": ["Delhi", "Maharashtra"],
    "City": ["New Delhi", "Mumbai"],
    "AI Tool": ["ChatGPT", "Copilot"],
    "Usage Count": [5, 3]
}

df = pd.DataFrame(data)
st.dataframe(df)

st.success("URL: /aitool-usagereports")
