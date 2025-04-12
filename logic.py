import PyPDF2
import docx2txt
from keybert import KeyBERT

kw_model = KeyBERT()


def extract_text(uploaded_file):
    if uploaded_file.name.endswith('.pdf'):
        reader = PyPDF2.PdfReader(uploaded_file)
        text= ''
        for page in reader.pages:
            text+=page.extract_text()
        return text
    
    elif uploaded_file.name.endswith('.docx'):
        return docx2txt.process(uploaded_file)
    
    return ''

def extract_keywords(text, top_n=10):
    keywords = kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 2),
        stop_words='english',
        top_n=top_n
    )
    return [kw[0] for kw in keywords]

def calculate_match_score(jd_keywords, resume_keywords):
    matched = set(jd_keywords) & set(resume_keywords)
    score = (len(matched) / len(jd_keywords)) * 100 if jd_keywords else 0
    return score, matched

def process_resume_and_jd(uploaded_file, jd_text):
    resume_text = extract_text(uploaded_file)

    resume_keywords = extract_keywords(resume_text)
    jd_keywords = extract_keywords(jd_text)

    score, matched = calculate_match_score(jd_keywords, resume_keywords)

    return resume_keywords, jd_keywords, score, matched


sample_text = """
We are looking for a software engineer with expertise in Python, machine learning, and cloud platforms like AWS.
The candidate should also be comfortable with data structures, algorithms, and system design.
"""

# Call the function
result = extract_keywords(sample_text, top_n=20)

# Print the result
print("Extracted Keywords:", result)




