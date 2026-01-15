import streamlit as st

st.set_page_config(page_title="AI Resume Screener")

st.title("AI Resume Screener")
st.write("App is running successfully ✅")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file:
    st.success("File uploaded successfully!")
