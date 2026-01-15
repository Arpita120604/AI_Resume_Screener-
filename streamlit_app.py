import streamlit as st

st.set_page_config(page_title="AI Resume Screener")

st.title("AI Resume Screener")
st.write("App is working ✅")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
