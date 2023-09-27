import streamlit as st
import pandas as pd
import plotly.express as px

# Define your resume data
resume_data = {
    "name": "SAMBIT KUMAR NAYAK",
    "email": "sambitnayak.tuserate@gmail.com",
    "phone": "+91-6372289425",
    "linkedin": "https://www.linkedin.com/in/sambit-kumar-nayak-6a836626b/",
    "github": "https://github.com/SambitKNayak",
    "summary": "I am a highly motivated data science & software engineer with a passion for creating elegant solutions to complex problems & handling big data.",
    "education": [
        {
            "degree": "Bachelor of Technology in Computer Science and Engineering",
            "university": "Kalinga Institute of Industrial Technology (KIIT)",
            "year": "2021-25",
        },
    ],
    "experience": [
        {
            "position": "Software Engineer",
            "company": "Tech Solutions Inc.",
            "year": "2022 - Present",
            "description": "Developed web applications and implemented new features.",
        },
        {
            "position": "Data Science Engineer Intern",
            "company": "CSIR-IMMT",
            "months": "May-July",
            "year": "2023",
            "description": "large data analysis[Soc Estimation on scale of 20 Millions]",
        },
    ],
    "skills": ["Python", "Data Analyst", "AI/ML", "Project Manager", "Java", "SQL"],
}

# Define your skills and their grades
skills_data = {
    "Skill": ["Python", "Data Analyst", "AI/ML", "Project Manager", "Java", "SQL"],
    "Grade": [83, 85, 85, 88, 70, 70],
}

# Create a DataFrame for skills
skills_df = pd.DataFrame(skills_data)

# Set page title and icon
st.set_page_config(
    page_title="THE SKN RESUME",
    page_icon="🤖",
    layout="wide",
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #222;
        color: #fff;
        font-family: Arial, sans-serif;
    }
    .container {
        padding: 20px;
        background-color: #333;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-radius: 10px;
        margin: 20px;
    }
    .header {
        text-align: center;
        padding: 20px;
        background-color: #444;
        color: #fff;
        border-radius: 10px 10px 0 0;
    }
    .contact-info {
        background-color: #555;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    .summary {
        padding: 20px;
    }
    .section-title {
        font-size: 24px;
        color: #FF5733;
        margin-bottom: 10px;
    }
    .experience-item {
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.markdown("<h1 class='header'>SAMBIT KUMAR NAYAK RESUME</h1>", unsafe_allow_html=True)

# Contact Information
st.markdown("<div class='container contact-info'>", unsafe_allow_html=True)
st.markdown(f"<p><strong>Name:</strong> {resume_data['name']}</p>", unsafe_allow_html=True)
st.markdown(f"<p><strong>Email:</strong> {resume_data['email']}</p>", unsafe_allow_html=True)
st.markdown(f"<p><strong>Phone:</strong> {resume_data['phone']}</p>", unsafe_allow_html=True)
st.markdown(f"<p><strong>LinkedIn:</strong> <a href='{resume_data['linkedin']}' target='_blank'>{resume_data['linkedin']}</a></p>", unsafe_allow_html=True)
st.markdown(f"<p><strong>GitHub:</strong> <a href='{resume_data['github']}' target='_blank'>{resume_data['github']}</a></p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Summary
st.markdown("<div class='container summary'>", unsafe_allow_html=True)
st.markdown(f"<h2 class='section-title'>Summary</h2>", unsafe_allow_html=True)
st.markdown(f"<p>{resume_data['summary']}</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Education
st.markdown("<div class='container'>", unsafe_allow_html=True)
st.markdown(f"<h2 class='section-title'>Education</h2>", unsafe_allow_html=True)
for edu in resume_data['education']:
    st.markdown(f"<p><strong>{edu['degree']}</strong> - {edu['university']} ({edu['year']})</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Work Experience
st.markdown("<div class='container'>", unsafe_allow_html=True)
st.markdown(f"<h2 class='section-title'>Work Experience</h2>", unsafe_allow_html=True)
for exp in resume_data['experience']:
    st.markdown(f"<div class='experience-item'>", unsafe_allow_html=True)
    st.markdown(f"<p><strong>{exp['position']}</strong> at {exp['company']} ({exp['year']})</p>", unsafe_allow_html=True)
    st.markdown(f"<p>{exp['description']}</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Skills
st.markdown("<div class='container'>", unsafe_allow_html=True)
st.markdown(f"<h2 class='section-title'>Skills</h2>", unsafe_allow_html=True)

# Bar chart for skills
fig = px.bar(
    skills_df, x="Skill", y="Grade",
    text="Grade", labels={"Skill": "Skill", "Grade": "Grade"},
    color_discrete_sequence=["#FF5733", "#FFB733", "#33FF57", "#33B5FF", "#FF33F2"]
)
fig.update_layout(
    xaxis_title=None,
    yaxis_title="Grade",
    showlegend=False,
    plot_bgcolor="rgba(0, 0, 0, 0)",
    paper_bgcolor="rgba(0, 0, 0, 0)",
)
st.plotly_chart(fig)

# Certification
st.markdown("<div class='container'>", unsafe_allow_html=True)
st.markdown("<h2 class='section-title' style='color: #FF5733;'>Certifications</h2>", unsafe_allow_html=True)

certifications = [
    {
        "name": "Certified Python Developer",
    },
    {
        "name": "JavaScript Fundamentals",
    },
    {
        "name": "React Certified Professional",
    },
    {
        "name": "Django for Web Development",
    },
    {
        "name": "SQL Mastery Certification",
    },
    {
        "name": "Certification F",
    },
    {
        "name": "Certification G",
    },
    # Add more certifications as needed
]

# Display certifications with colorful backgrounds
for idx, cert in enumerate(certifications):
    background_color = "#FF5733" if idx % 2 == 0 else "#FFB733"  # Alternate colors
    st.markdown(
        f"<div style='background-color: {background_color}; color: #fff; padding: 10px; border-radius: 5px;'>"
        f"<strong>{cert['name']}</strong>"
        "</div>",
        unsafe_allow_html=True,
    )

st.markdown("</div>", unsafe_allow_html=True)
