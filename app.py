import streamlit as st
import pandas as pd

st.title("AI Tool Usage Reports – India")
st.subheader("Location-wise AI Tool Usage")

data = {
    "State": ["Delhi", "Maharashtra","Jharkhand","Bihar","Orisa",],
    "City": ["New Delhi", "Mumbai","Ranchi","Jamshedpur","Dhanbad","Bhuwaneshwar","cuttak","Patna",],
    "AI Tool": ["ChatGPT", "Copilot","Gemini","purplexcity"],
    "Usage Count": [13,11,9,7,5, 3,2,]
}

df = pd.DataFrame(data)
st.dataframe(df)

st.success("URL: /aitool-usagereports")

