import streamlit as st
import re

from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords


# -----------------------------
# Stopwords
# -----------------------------

stop_words = set(stopwords.words("english"))


# -----------------------------
# Text preprocessing
# -----------------------------

def preprocess_text(text):
    text = text.lower()

    text = re.sub(r'[^a-zA-Z\s]', '', text)

    text = re.sub(r'\s+', ' ', text).strip()

    words = text.split()

    words = [word for word in words if word not in stop_words]

    return " ".join(words)


# -----------------------------
# PDF text extraction
# -----------------------------

def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + " "

    return text


# -----------------------------
# Skill extraction
# -----------------------------

skills = [
    "python",
    "java",
    "c++",
    "sql",
    "machine learning",
    "deep learning",
    "natural language processing",
    "nlp",
    "tensorflow",
    "pytorch",
    "scikit learn",
    "pandas",
    "numpy",
    "aws",
    "docker",
    "git",
    "html",
    "css",
    "javascript"
]


def extract_skills(text):
    found_skills = []

    for skill in skills:
        if skill in text:
            found_skills.append(skill)

    return found_skills


# -----------------------------
# Similarity calculation
# -----------------------------

def calculate_similarity(resume_text, job_text):

    documents = [resume_text, job_text]

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        vectors[0],
        vectors[1]
    )

    return similarity[0][0] * 100


# -----------------------------
# Streamlit UI
# -----------------------------

st.title("📄 Resume Matcher")

st.write(
    "Upload your resume and paste a job description "
    "to calculate how well they match."
)


# Resume upload

uploaded_file = st.file_uploader(
    "Upload your resume",
    type=["pdf"]
)


# Job description

job_description = st.text_area(
    "Paste Job Description",
    height=250
)


# Analyze button

if st.button("Analyze Resume"):

    if uploaded_file is None:
        st.error("Please upload a resume.")

    elif not job_description.strip():
        st.error("Please enter a job description.")

    else:

        # Extract resume text
        resume_text = extract_text_from_pdf(uploaded_file)

        # Preprocess both texts
        clean_resume = preprocess_text(resume_text)
        clean_job = preprocess_text(job_description)

        # Calculate similarity
        match_percentage = calculate_similarity(
            clean_resume,
            clean_job
        )

        # Extract skills
        resume_skills = extract_skills(clean_resume)
        job_skills = extract_skills(clean_job)

        matched_skills = []

        for skill in job_skills:
            if skill in resume_skills:
                matched_skills.append(skill)

        missing_skills = []

        for skill in job_skills:
            if skill not in resume_skills:
                missing_skills.append(skill)

        # Calculate skill match
        if len(job_skills) > 0:
            skill_match_percentage = (
                len(matched_skills) / len(job_skills)
            ) * 100
        else:
            skill_match_percentage = 0

        # Overall score
        overall_score = (
            match_percentage +
            skill_match_percentage
        ) / 2


        # -----------------------------
        # Display results
        # -----------------------------

        st.subheader("Results")

        st.metric(
            "Overall Match",
            f"{overall_score:.2f}%"
        )

        st.metric(
            "Text Similarity",
            f"{match_percentage:.2f}%"
        )

        st.metric(
            "Skill Match",
            f"{skill_match_percentage:.2f}%"
        )


        st.subheader("Matched Skills")

        if matched_skills:
            for skill in matched_skills:
                st.success(skill)

        else:
            st.write("No matching skills found.")


        st.subheader("Missing Skills")

        if missing_skills:
            for skill in missing_skills:
                st.error(skill)

        else:
            st.write("No missing skills!")