import PyPDF2
import docx2txt
from keybert import KeyBERT

# Initialize the model
kw_model = KeyBERT()

# Predefined global skill set
common_skills = [
    'python', 'c++', 'java', 'tensorflow', 'pytorch', 'machine learning',
    'deep learning', 'nlp', 'pandas', 'numpy', 'scikit-learn', 'matplotlib',
    'data analysis', 'sql', 'aws', 'azure', 'gcp', 'git', 'linux',
    'data structures', 'algorithms', 'html', 'css', 'javascript'
]

# Extract text from PDF or DOCX
def extract_text(file_path):
    if file_path.endswith('.pdf'):
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = ''
            for page in reader.pages:
                text += page.extract_text()
        return text

    elif file_path.endswith('.docx'):
        return docx2txt.process(file_path)

    return ''

# Extract keywords using predefined skill list
def extract_skills_using_list(text, skill_list):
    found_skills = []
    for skill in skill_list:
        if skill.lower() in text.lower():
            found_skills.append(skill)
    return found_skills

# Match and score
def calculate_match_score(jd_keywords, resume_keywords):
    matched = set(jd_keywords) & set(resume_keywords)
    score = (len(matched) / len(jd_keywords)) * 100 if jd_keywords else 0
    return score, matched

# Identify missing skills
def get_missing_skills(jd_keywords, resume_keywords):
    return list(set(jd_keywords) - set(resume_keywords))

# Generate suggestions for improvement
def generate_suggestions(missing_skills):
    return [
        f"Consider gaining experience or certification in '{skill}' to align better with the job description."
        for skill in missing_skills
    ]

# Main function to process resume and JD
def process_resume_and_jd(resume_path, jd_text):
    resume_text = extract_text(resume_path)

    resume_skills = extract_skills_using_list(resume_text, common_skills)
    jd_skills = extract_skills_using_list(jd_text, common_skills)

    score, matched = calculate_match_score(jd_skills, resume_skills)
    missing_skills = get_missing_skills(jd_skills, resume_skills)
    suggestions = generate_suggestions(missing_skills)

    return {
        "resume_keywords": resume_skills,
        "jd_keywords": jd_skills,
        "match_score": score,
        "matched_keywords": matched,
        "missing_skills": missing_skills,
        "suggestions": suggestions
    }