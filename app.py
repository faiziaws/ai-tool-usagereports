import streamlit as st
import pandas as pd

# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(
    page_title="AI Tool Usage Reports – India",
    layout="wide"
)

# ==================================================
# SESSION STATE INITIALIZATION
# ==================================================
if "users" not in st.session_state:
    st.session_state.users = {}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ==================================================
# AUTHENTICATION (REGISTER + LOGIN)
# ==================================================
if not st.session_state.logged_in:

    st.title("🔐 User Authentication")

    tab1, tab2 = st.tabs(["📝 Register", "🔑 Login"])

    # ---------- REGISTER ----------
    with tab1:
        st.subheader("New User Registration")

        reg_username = st.text_input("Create Username")
        reg_password = st.text_input("Create Password", type="password")

        if st.button("Register"):
            if reg_username and reg_password:
                if reg_username in st.session_state.users:
                    st.error("User already exists. Please login.")
                else:
                    st.session_state.users[reg_username] = reg_password
                    st.success("Registration successful! Please login.")
            else:
                st.warning("Please fill all fields.")

    # ---------- LOGIN ----------
    with tab2:
        st.subheader("Existing User Login")

        login_username = st.text_input("Username")
        login_password = st.text_input("Password", type="password")

        if st.button("Login"):
            if (
                login_username in st.session_state.users and
                st.session_state.users[login_username] == login_password
            ):
                st.session_state.logged_in = True
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid username or password.")

    st.stop()

# ==================================================
# MAIN DASHBOARD
# ==================================================
st.title("AI Tool Usage Reports – India")
st.subheader("Location-wise AI Tool Usage by Users")

st.markdown(
    """
    This dashboard analyzes **state and city-wise AI tool usage in India**.
    All insights are calculated using **actual usage counts**.
    """
)

# ==================================================
# DATA
# ==================================================
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

# ==================================================
# FILTER (STATE)
# ==================================================
st.markdown("### 🔍 Filter Options")

states = ["All States"] + sorted(df["State"].unique().tolist())
selected_state = st.selectbox("Select State", states)

filtered_df = df.copy()
if selected_state != "All States":
    filtered_df = df[df["State"] == selected_state]

# ==================================================
# DISPLAY DATA
# ==================================================
st.dataframe(filtered_df, use_container_width=True)

# ==================================================
# SUMMARY INSIGHTS (CORRECT LOGIC)
# ==================================================
st.markdown("### 📊 Summary Insights")

col1, col2, col3, col4 = st.columns(4)

# Total Records
col1.metric("Total Records", len(filtered_df))

# Total AI Tools
col2.metric("AI Tools Used", filtered_df["AI Tool"].nunique())

# ---------- Top City by Total Usage ----------
top_city_df = (
    filtered_df.groupby("City", as_index=False)["Usage Count"]
    .sum()
    .sort_values(by="Usage Count", ascending=False)
)

top_city = top_city_df.iloc[0]["City"]
top_city_usage = top_city_df.iloc[0]["Usage Count"]
col3.metric("Top City", f"{top_city} ({top_city_usage})")

# ---------- Top State by Total Usage ----------
top_state_df = (
    filtered_df.groupby("State", as_index=False)["Usage Count"]
    .sum()
    .sort_values(by="Usage Count", ascending=False)
)

top_state = top_state_df.iloc[0]["State"]
top_state_usage = top_state_df.iloc[0]["Usage Count"]
col4.metric("Top State", f"{top_state} ({top_state_usage})")

# ==================================================
# MOST USED AI TOOL
# ==================================================
st.markdown("### 🤖 Most Used AI Tool (Overall)")

top_tool_df = (
    filtered_df.groupby("AI Tool", as_index=False)["Usage Count"]
    .sum()
    .sort_values(by="Usage Count", ascending=False)
)

top_tool = top_tool_df.iloc[0]["AI Tool"]
top_tool_usage = top_tool_df.iloc[0]["Usage Count"]

st.info(f"**{top_tool}** is the most used AI tool with **{top_tool_usage}** total usages.")

# ==================================================
# BAR CHART – STATE-WISE USAGE
# ==================================================
st.markdown("### 📈 State-wise AI Tool Usage")

state_usage_df = (
    filtered_df.groupby("State", as_index=False)["Usage Count"]
    .sum()
    .sort_values(by="Usage Count", ascending=False)
)

st.bar_chart(state_usage_df.set_index("State"))

# ==================================================
# LOGOUT
# ==================================================
if st.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()

# ==================================================
# FOOTER
# ==================================================
st.success("Logical Endpoint: /aitool-usagereports")

st.markdown(
    """
    **Project Name:** Location-wise AI Tools Used by Users in India  
    **Features:** Register, Login, Filters, Analytics, Charts  
    **Technology:** DBMS Concepts, AI, Streamlit Cloud  
    **Course:** BCA – DBMS Mini Project
    """
)
