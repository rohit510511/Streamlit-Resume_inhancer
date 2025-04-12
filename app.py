# app.py

import streamlit as st
import os
from logic import process_resume_and_jd

# Set page config
st.set_page_config(page_title="Resume Enhancer", page_icon="📄", layout="wide")
st.title("📄 Resume Enhancer")
st.markdown("Upload your resume and job description to get keyword match insights.")

# Sidebar
with st.sidebar:
    st.header("About")
    st.markdown("Enhance your resume with keyword analysis and score estimation.")

# File uploader
uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])

# JD input
jd_text = st.text_area("Paste the Job Description here")

if uploaded_file and jd_text:
    # Save file temporarily
    temp_dir = "temp"
    os.makedirs(temp_dir, exist_ok=True)
    file_path = os.path.join(temp_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Process resume and JD
    resume_keywords, jd_keywords, score, matched = process_resume_and_jd(uploaded_file, jd_text)

    # Output
    st.subheader("🔍 Extracted Keywords")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Resume Keywords:**")
        st.write(resume_keywords)
    with col2:
        st.markdown("**JD Keywords:**")
        st.write(jd_keywords)

    # Display match score and matched keywords
    st.success(f"🎯 Match Score: {score:.2f}%")
    st.markdown("✅ **Matched Keywords:**")
    st.write(matched)
