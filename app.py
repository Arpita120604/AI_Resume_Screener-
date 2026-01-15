import streamlit as st
from resume_parser import extract_text_from_pdf

st.set_page_config(page_title="AI Resume Screener")

st.title("AI Resume Screener")
st.write("App is running successfully ✅")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)
    st.success("Resume parsed successfully!")

    with st.expander("Show extracted resume text"):
        st.write(resume_text[:3000])  # preview only
