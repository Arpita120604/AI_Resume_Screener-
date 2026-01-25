import streamlit as st
from resume_parser import extract_text_from_pdf
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="AI Resume Screener")

st.title("AI Resume Screener")
st.write("App is running successfully ✅")

# 1️⃣ Job Description Input
job_description = st.text_area(
    "Enter Job Description",
    height=200,
    placeholder="Paste the job description here..."
)

# 2️⃣ Resume Upload
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file and job_description:
    resume_text = extract_text_from_pdf(uploaded_file)

    # 3️⃣ TF-IDF Matching
    documents = [resume_text, job_description]
    tfidf = TfidfVectorizer(stop_words='english')
    vectors = tfidf.fit_transform(documents)
    similarity_score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

    st.success("Resume analyzed successfully!")

    st.subheader("Match Result")
    st.write(f"**Resume Match Score:** {round(similarity_score*100, 2)}%")

elif uploaded_file and not job_description:
    st.warning("⚠️ Please enter the job description.")


if uploaded_file and job_description:
    resume_text = extract_text_from_pdf(uploaded_file)

    # --- AI MATCHING ---
    resume_embedding = model.encode(resume_text)
    jd_embedding = model.encode(job_description)

    similarity = cosine_similarity(
        [resume_embedding],
        [jd_embedding]
    )[0][0]

    score = round(similarity * 100, 2)

    # --- SHOW RESULT ---
    st.success("Resume analyzed successfully!")
    st.subheader("Result")
    st.metric("Resume Match Score", f"{score}%")


import streamlit as st
from resume_parser import extract_text_from_pdf
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="AI Resume Screener")

st.title("AI Resume Screener")

# Job Description input
job_description = st.text_area(
    "Enter Job Description",
    height=200,
    placeholder="Paste job description here..."
)

# Resume upload
uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

# Load AI model (cached)
@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()

# Show result
if uploaded_file and job_description:

    resume_text = extract_text_from_pdf(uploaded_file)

    resume_embedding = model.encode(resume_text)
    jd_embedding = model.encode(job_description)

    similarity = cosine_similarity(
        [resume_embedding],
        [jd_embedding]
    )[0][0]

    score = round(similarity * 100, 2)

    st.success("Resume analyzed successfully!")
    st.subheader("Result")
    st.metric("Resume Match Score", f"{score}%")

elif uploaded_file and not job_description:
    st.warning("Please enter the job description.")


