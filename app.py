import streamlit as st
import os

# Set page config
st.set_page_config(
    page_title="Resume Enhancer",
    page_icon="📄",
    layout="wide"
)

# Main title
st.title("📄 Resume Enhancer")
st.markdown("Upload your resume and get AI-powered suggestions to enhance it!")

# File uploader
uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])

if uploaded_file is not None:
    # Display file details
    file_details = {
        "Filename": uploaded_file.name,
        "File type": uploaded_file.type,
        "File size": f"{uploaded_file.size / 1024:.2f} KB"
    }
    st.write(file_details)

    # Save the file temporarily
    with open(os.path.join("temp", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("File uploaded successfully!")

# Add a sidebar
with st.sidebar:
    st.header("About")
    st.markdown("""
    This app helps you enhance your resume with AI-powered suggestions.
    Upload your resume and get personalized recommendations to make it stand out!
    """)
