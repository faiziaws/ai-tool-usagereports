import streamlit as st
import pandas as pd

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="AI Tool Usage Reports – India",
    layout="wide"
)

# --------------------------------------------------
# SESSION STATE INITIALIZATION
# --------------------------------------------------
if "users" not in st.session_state:
    st.session_state.users = {}   # stores registered users

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --------------------------------------------------
# AUTH SECTION (REGISTER / LOGIN)
# --------------------------------------------------
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
                    st.success("Registration successful! You can now login.")
            else:
                st.warning("Please fill all fields")

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
                st.error("Invalid username or password")

    st.stop()

# --------------------------------------------------
# MAIN DASHBOARD (AFTER LOGIN)
# --------------------------------------------------
st.title("AI Tool Usage Reports – India")
st.subheader("Location-wise AI Tool Usage by Users")

st.markdown(
    """
    This dashboard presents **state and city-wise AI tool usage in India**.
    It supports **user registration, login, filtering, and analytics**.
    """
)

# --------------------------------------------------
# DATA
# --------------------------------------------------
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

# --------------------------------------------------
# FILTER BY STATE
# --------------------------------------------------
st.markdown("### 🔍 Filter Options")

states = ["All States"] + sorted(df["State"].unique().tolist())
selected_state = st.selectbox("Select State", states)

if selected_state != "All States":
    df = df[df["State"] == selected_state]

# --------------------------------------------------
# DISPLAY DATA
# --------------------------------------------------
st.dataframe(df, use_container_width=True)

# --------------------------------------------------
# SUMMARY METRICS
# --------------------------------------------------
st.markdown("### 📊 Summary Insights")

col1, col2, col3 = st.columns(3)
col1.metric("Total Records", len(df))
col2.metric("AI Tools Used", df["AI Tool"].nunique())
col3.metric("Top City", df["City"].mode()[0])

# --------------------------------------------------
# LOGOUT
# --------------------------------------------------
if st.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.success("Logical Endpoint: /aitool-usagereports")

st.markdown(
    """
    **Project Name:** Location-wise AI Tools Used by Users in India  
    **Features:** User Registration, Login, State Filter, Analytics  
    **Technology:** DBMS Concepts, AI, Streamlit Cloud  
    **Course:** BCA – DBMS Mini Project
    """
)
