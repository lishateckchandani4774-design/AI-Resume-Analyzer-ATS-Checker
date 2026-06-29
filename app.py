import plotly.express as px
import streamlit as st
import pdfplumber
import pandas as pd

import plotly.express as px
import streamlit as st
import pdfplumber
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄"
)

st.markdown("""
<div style='text-align:center;
padding:20px;
border-radius:15px;
background:linear-gradient(90deg,#1e3c72,#2a5298);
color:white;'>

<h1>📄 AI Resume Analyzer & ATS Checker</h1>
<p>Smart Resume Screening and Career Recommendation System</p>

</div>
""", unsafe_allow_html=True)
st.title("📄 AI Resume Analyzer")

st.sidebar.markdown("""
# 🎯 AI Resume Analyzer

### Features

✅ ATS Score

✅ Resume Strength Level

✅ Career Recommendations

✅ Skill Gap Analysis

✅ Certifications

✅ Download Report

---

Developed By

Lisha
""")
uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

skills_database = [
    "Python",
    "SQL",
    "Machine Learning",
    "Deep Learning",
    "NLP",
    "AWS",
    "Docker",
    "Java",
    "Power BI",
    "Excel",
    "Linux"
]

if uploaded_file:

    resume_text = ""

    with pdfplumber.open(uploaded_file) as pdf:

        for page in pdf.pages:
            resume_text += page.extract_text()

    st.subheader("Resume Text Extracted")

    st.text_area(
        "Resume Content",
        resume_text,
        height=250
    )

    found_skills = []

    for skill in skills_database:

        if skill.lower() in resume_text.lower():
            found_skills.append(skill)

    # -------------------------
    # ATS SCORE
    # -------------------------

    total_skills = len(skills_database)

    found_count = len(found_skills)

    ats_score = int(
        (found_count / total_skills) * 100
    )

    # -------------------------
    # DASHBOARD
    # -------------------------
    st.divider()
    st.subheader("📊 Resume Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "ATS Score",
            f"{ats_score}/100"
        )

    with col2:
        st.metric(
            "Skills Found",
            found_count
        )

    with col3:
        st.metric(
            "Missing Skills",
            total_skills - found_count
        )

    st.progress(ats_score)
    st.markdown(f"""
    <div style='
    padding:20px;
    border-radius:15px;
    border:2px solid #4CAF50;
    background-color:#1E293B;
    '>

    <h2>ATS Score: {ats_score}/100</h2>

    </div>
    """, unsafe_allow_html=True)

    # -------------------------
    # RESUME LEVEL
    # -------------------------
    st.divider()
    if ats_score >= 80:
        level = "Industry Ready 🚀"

    elif ats_score >= 60:
        level = "Advanced ⭐"

    elif ats_score >= 40:
        level = "Intermediate 📘"

    else:
        level = "Beginner 🌱"

    st.subheader("🏅 Resume Strength Level")

    st.success(level)

    # -------------------------
    # DETECTED SKILLS
    # -------------------------
    st.divider()
    st.subheader("✅ Detected Skills")

    for skill in found_skills:
        st.success(skill)

    # -------------------------
    # MISSING SKILLS
    # -------------------------

    missing_skills = []

    for skill in skills_database:

        if skill not in found_skills:
            missing_skills.append(skill)

    st.subheader("❌ Missing Skills")

    for skill in missing_skills:
        st.error(skill)

    # -------------------------
    # SUGGESTIONS
    # -------------------------
    st.divider()
    st.subheader("💡 Resume Suggestions")

    if ats_score < 50:

        st.warning(
            "Add more technical skills to improve ATS score."
        )

    if len(found_skills) < 5:

        st.warning(
            "Add projects and certifications."
        )

    if "Python" not in found_skills:

        st.warning(
            "Python is highly recommended."
        )

    if "SQL" not in found_skills:

        st.warning(
            "SQL is highly demanded in industry."
        )

    # -------------------------
    # CAREER RECOMMENDATIONS
    # -------------------------
    st.divider()
    st.subheader("🎯 Recommended Careers")

    career_matches = []

    if "Python" in found_skills:
        career_matches.append("Data Scientist")

    if "Machine Learning" in found_skills:
        career_matches.append("Machine Learning Engineer")

    if "Deep Learning" in found_skills:
        career_matches.append("AI Engineer")

    if "SQL" in found_skills:
        career_matches.append("Data Analyst")

    if "AWS" in found_skills:
        career_matches.append("Cloud Engineer")

    if "Java" in found_skills:
        career_matches.append("Software Developer")

    if len(career_matches) == 0:
        st.warning("Add more technical skills for career recommendations.")

    else:
        for career in career_matches:
            st.success(career)

    # -------------------------
    # PROJECT RECOMMENDATIONS
    # -------------------------
    st.divider()
    st.subheader("💻 Recommended Projects")

    projects = []

    if "Python" in found_skills:
        projects.append(
            "Python Automation System"
        )

    if "Machine Learning" in found_skills:
        projects.append(
            "Machine Learning Prediction System"
        )

    if "Deep Learning" in found_skills:
        projects.append(
            "Image Classification Project"
        )

    if "SQL" in found_skills:
        projects.append(
            "Sales Analytics Dashboard"
        )

    if "AWS" in found_skills:
        projects.append(
            "Cloud Deployment Project"
        )

    for project in projects:
        st.write(f"🚀 {project}")

    # -------------------------
    # CERTIFICATIONS
    # -------------------------
    st.divider()
    with st.expander("🏆 Recommended Certifications"):
        certifications = []

        if "Python" in found_skills:
            certifications.append("Python for Everybody")

        if "Machine Learning" in found_skills:
            certifications.append("Machine Learning Specialization")

        if "AWS" in found_skills:
            certifications.append("AWS Cloud Practitioner")

        if "SQL" in found_skills:
            certifications.append("Google Data Analytics")

        if "Deep Learning" in found_skills:
            certifications.append("TensorFlow Developer Certificate")

        for cert in certifications:
            st.write(f"🏅 {cert}")

    # -------------------------
    # GITHUB TIPS
    # -------------------------
    st.divider()
    with st.expander("🐙 GitHub Portfolio Tips"):
        github_tips = [
            "Upload at least 5 projects",
            "Write professional README files",
            "Use meaningful repository names",
            "Add project screenshots",
            "Keep code well documented"
        ]

        for tip in github_tips:
            st.write(f"✅ {tip}")

    # -------------------------
    # ATS CHART
    # -------------------------
    st.divider()
    st.subheader("📈 ATS Skills Overview")

    chart_data = {
        "Category": [
            "Found Skills",
            "Missing Skills"
        ],

        "Count": [
            len(found_skills),
            len(missing_skills)
        ]
    }

    chart_df = pd.DataFrame(chart_data)

    fig = px.bar(
        chart_df,
        x="Category",
        y="Count",
        title="Resume Skill Analysis"
    )

    pie_fig = px.pie(
        chart_df,
        values="Count",
        names="Category",
        title="Resume Skill Distribution"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:
        st.plotly_chart(
            pie_fig,
            use_container_width=True
        )

    # -------------------------
    # HR SUMMARY
    # -------------------------
    st.divider()
    st.subheader("📋 Candidate Summary")

    best_career = (
        career_matches[0]
        if len(career_matches) > 0
        else "Not Determined"
    )

    if ats_score >= 70:
        employability = "High"

    elif ats_score >= 50:
        employability = "Moderate"

    else:
        employability = "Needs Improvement"

    st.info(
        f"""
    ATS Score: {ats_score}/100

    Resume Level: {level}

    Recommended Career: {best_career}

    Employability: {employability}
    """
    )
    # ============================================
    # JOB DESCRIPTION MATCHER
    # ============================================

    st.markdown("---")
    st.header("🎯 Resume vs Job Description Matcher")

    job_description = st.text_area(
        "Paste the Job Description",
        height=220,
        placeholder="""
    Example:

    We are looking for a Python Developer with experience in SQL,
    Machine Learning, TensorFlow, Docker, AWS and Git.
    """
    )
    if job_description.strip() != "":

     from sklearn.feature_extraction.text import TfidfVectorizer
     from sklearn.metrics.pairwise import cosine_similarity

    documents = [
        resume_text.lower(),
        job_description.lower()
    ]

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        vectors[0],
        vectors[1]
    )[0][0]

    match_score = similarity * 100

    st.subheader("📊 Resume Match Score")

    st.progress(min(int(match_score), 100))
    # =====================================
    # SKILL MATCH ANALYSIS
    # =====================================

    resume_words = set(resume_text.lower().split())
    jd_words = set(job_description.lower().split())

    common_words = sorted(resume_words.intersection(jd_words))
    missing_words = sorted(jd_words - resume_words)

    # Remove very small words
    missing_words = [
        word for word in missing_words
        if len(word) > 3
    ]

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("✅ Matching Keywords")

        if common_words:

            for word in common_words[:20]:
                st.success(word)

        else:
            st.info("No matching keywords found.")

    with col2:

        st.subheader("❌ Missing Keywords")

        if missing_words:

            for word in missing_words[:20]:
                st.error(word)

        else:
            st.success("Excellent! No important keywords are missing.")

            st.markdown("---")

        st.subheader("💡 ATS Suggestions")

        if match_score >= 80:

            st.success("""
        Excellent resume match!

        Your resume aligns very well with the job description.
        Only minor improvements are needed.
        """)

        elif match_score >= 60:

            st.warning("""
        Good match.

        Consider adding more relevant technical skills,
        projects, and keywords from the job description.
        """)

        else:

            st.error("""
        Low ATS Match.

        Improve your resume by adding
        • Required Skills
        • Relevant Projects
        • Certifications
        • Keywords from the Job Description
        """)
    # -------------------------
    # DOWNLOAD REPORT
        # -------------------------
        report = f"""
    ==============================
    AI RESUME ANALYZER REPORT
    ==============================

    ATS SCORE
    -------------------
    {ats_score:.1f}%

    JOB DESCRIPTION MATCH
    -------------------
    {match_score:.1f}%

    CAREER MATCH
    -------------------
    {career_matches[0]}

    SKILLS FOUND
    -------------------
    {", ".join(found_skills)}

    MISSING SKILLS
    -------------------
    {", ".join(missing_skills)}

    TOP ATS SUGGESTIONS
    -------------------
    • Add missing keywords
    • Add relevant projects
    • Mention certifications
    • Quantify achievements
    • Tailor resume to the job description

    Generated using
    AI Resume Analyzer & ATS Checker
    """

    st.markdown("""
    ---
    <center>

    AI Resume Analyzer

    Built with Python • Streamlit • NLP

    © 2026

    </center>
    """, unsafe_allow_html=True)