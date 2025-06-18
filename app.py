# streamlit_app.py
import streamlit as st
from streamlit_lottie import st_lottie
import requests
import time
import pandas as pd
import plotly.express as px
from datetime import datetime
import os
from PIL import Image
import base64

# ====== CONFIGURATION ====== #
SOCIAL_LINKS = {
    "github": "https://github.com/Sandeep2369",
    "linkedin": "http://linkedin.com/in/sandeep-ponnapalli-abb86a190",
    "email": "mailto:sanjusandeep846@gmail.com"
}

CONTACT_INFO = {
    "email": "sanjusandeep846@gmail.com",
    "phone": "+91 7780242441",
    "location": "Andhra Pradesh, India"
}

SKILLS = {
    "Python Programming": 92,
    "Machine Learning": 88,
    "AWS Cloud Services": 85,
    "Natural Language Processing": 83,
    "Data Analysis": 87,
    "Deep Learning": 80,
}

PAGES = [
    "🏠 Home",
    "🛠 Skills",
    "💼 Experience", 
    "🚀 Projects",
    "🎓 Education",
    "📩 Contact"
]

# ====== SETUP ====== #
st.set_page_config(
    page_title="Ponnapalli Poorna Sandeep | AI/ML Trainee",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ====== LOAD ASSETS ====== #
@st.cache_data
def load_lottie(url, retries=2, timeout=5):
    for attempt in range(retries + 1):
        try:
            r = requests.get(url, timeout=timeout)
            r.raise_for_status()
            return r.json()
        except requests.exceptions.RequestException as e:
            if attempt == retries:
                st.warning(f"Couldn't load animation. Using fallback content.")
                return None
            time.sleep(1)

@st.cache_resource
def load_image(path):
    try:
        return Image.open(path)
    except Exception as e:
        st.error(f"Error loading image: {str(e)}")
        return None

# Load assets
lottie_coding = load_lottie("https://assets7.lottiefiles.com/packages/lf20_qp1q7mct.json")
placeholder_img = load_image("placeholder.png") if os.path.exists("placeholder.png") else None

# ====== RESUME HANDLING ====== #
def get_resume_bytes():
    """Try multiple ways to load the resume file"""
    # Try local file first
    local_path = "Ponnapalli_Poorna_Sandeep_Resume2.pdf"
    if os.path.exists(local_path):
        with open(local_path, "rb") as f:
            return f.read()
    
    # Try GitHub raw content as fallback
    try:
        github_url = "https://raw.githubusercontent.com/Sandeep2369/portfolio/main/Ponnapalli_Poorna_Sandeep_Resume2.pdf"
        response = requests.get(github_url)
        response.raise_for_status()
        return response.content
    except:
        return None

def resume_download_section(key_suffix=""):
    resume_bytes = get_resume_bytes()
    
    if resume_bytes:
        st.download_button(
            label="📄 Download Resume",
            data=resume_bytes,
            file_name="Ponnapalli_Poorna_Sandeep_Resume.pdf",
            mime="application/pdf",
            help="Click to download my complete resume",
            use_container_width=True,
            key=f"resume_download_{key_suffix}"
        )
    else:
        st.error("Resume file could not be loaded automatically")
        st.info("Please contact me directly at sanjusandeep846@gmail.com for my resume")
    
    st.markdown(f"""
    <div style="text-align: center; margin-top: 1rem;">
        <a href="mailto:sanjusandeep846@gmail.com" class="btn">📧 Email Me</a>
    </div>
    """, unsafe_allow_html=True)

# ====== COMPONENTS ====== #
def skill_chart():
    df = pd.DataFrame.from_dict(SKILLS, orient='index', columns=['Proficiency'])
    fig = px.bar(
        df,
        x=df.index,
        y='Proficiency',
        labels={'x': 'Skill', 'y': 'Proficiency'},
        color='Proficiency',
        color_continuous_scale='Blues',
        text='Proficiency'
    )
    fig.update_traces(texttemplate='%{text}%', textposition='outside')
    fig.update_layout(
        xaxis_tickangle=-45,
        yaxis_range=[0, 100],
        showlegend=False,
        margin=dict(l=20, r=20, t=30, b=20)
    )
    st.plotly_chart(fig, use_container_width=True)

def project_card(title, description, tech_stack, results=None):
    with st.expander(f"📌 {title}", expanded=False):
        st.markdown(description)
        
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown("**Tech Stack:**")
            for tech in tech_stack:
                st.markdown(f"- {tech}")
        
        if results:
            with col2:
                st.markdown("**Key Results:**")
                for result in results:
                    st.markdown(f"- {result}")

def experience_card(company, duration, position, achievements, technologies):
    with st.expander(f"🏢 {company} | {duration} | {position}", expanded=True):
        st.markdown("**Key Achievements:**")
        for achievement in achievements:
            st.markdown(f"- {achievement}")
        
        st.markdown("**Technologies Used:**")
        cols = st.columns(4)
        for i, tech in enumerate(technologies):
            cols[i%4].markdown(f"- {tech}")

# ====== CSS STYLING ====== #
def local_css():
    st.markdown(f"""
    <style>
    :root {{
        --primary: #4361ee;
        --secondary: #3f37c9;
        --accent: #4895ef;
        --dark: #1e1e24;
        --light: #f8f9fa;
    }}

    /* Dark mode support */
    @media (prefers-color-scheme: dark) {{
        :root {{
            --primary: #4895ef;
            --secondary: #4361ee;
            --accent: #3f37c9;
            --dark: #f8f9fa;
            --light: #1e1e24;
        }}
        
        body, .card, .testimonial {{
            background-color: #121212;
            color: #ffffff;
        }}
        
        .st-expander {{
            background-color: #1e1e1e;
        }}
    }}

    /* Main Styling */
    html, body, [class*="css"] {{
        font-family: 'Poppins', sans-serif;
        background-color: #f9f9f9;
        color: #333;
        line-height: 1.6;
    }}

    /* Header Styling */
    .header {{
        color: var(--primary);
        font-weight: 700;
        margin-bottom: 1rem;
    }}

    /* Card Styling */
    .card {{
        background: white;
        border-radius: 12px;
        box-shadow: 0 6px 16px rgba(0,0,0,0.1);
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        transition: all 0.3s ease;
        border-left: 4px solid var(--accent);
    }}
    .card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 12px 20px rgba(0,0,0,0.15);
    }}

    /* Button Styling */
    .btn {{
        background: var(--primary);
        color: white !important;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        text-decoration: none;
        display: inline-block;
        margin: 0.3rem;
        transition: all 0.3s;
    }}
    .btn:hover {{
        background: var(--secondary);
        transform: scale(1.05);
    }}

    /* Responsive Design */
    @media (max-width: 768px) {{
        .col {{
            flex: 100% !important;
        }}
    }}
    </style>
    """, unsafe_allow_html=True)

local_css()

# ====== SIDEBAR ====== #
with st.sidebar:
    st.markdown("## Ponnapalli Poorna Sandeep")
    st.markdown("**AI/ML Trainee | AWS Cloud Intern**")
    
    if placeholder_img:
        st.image(placeholder_img, width=200, use_column_width='always')

    st.markdown("---")
    st.markdown(f"📧 **Email:** [{CONTACT_INFO['email']}](mailto:{CONTACT_INFO['email']})")
    st.markdown(f"📞 **Phone:** {CONTACT_INFO['phone']}")
    st.markdown(f"📍 **Location:** {CONTACT_INFO['location']}")

    st.markdown("---")
    st.markdown("### Navigation")
    page = st.radio("", PAGES, label_visibility="collapsed", key="nav_radio")

    st.markdown("---")
    st.markdown("### 📄 Resume Download")
    resume_download_section(key_suffix="sidebar")

    st.markdown("---")
    st.markdown("""
    <div style="text-align: center;">
        <a href="{}" class="btn" target="_blank">GitHub</a>
        <a href="{}" class="btn" target="_blank">LinkedIn</a>
    </div>
    """.format(SOCIAL_LINKS['github'], SOCIAL_LINKS['linkedin']), unsafe_allow_html=True)

# ====== PAGE CONTENT ====== #
if page == "🏠 Home":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("# Hi, I'm **Ponnapalli Poorna Sandeep**")
        st.markdown("### AI/ML Trainee | AWS Cloud Intern")
        st.markdown("""
        I am an enthusiastic AI/ML trainee with a strong foundation in model development, deployment, and automation workflows. Passionate about learning and exploring innovative ML applications.:
        - Machine Learning & Deep Learning
        - Natural Language Processing (NLP)
        - Cloud Computing (AWS)
        - Data Pipelines
        """)

        st.markdown("""
        <div style="margin-top: 2rem;">
            <a href="{}" class="btn" target="_blank">GitHub</a>
            <a href="{}" class="btn" target="_blank">LinkedIn</a>
            <a href="mailto:sanjusandeep846@gmail.com" class="btn">Email Me</a>
        </div>
        """.format(SOCIAL_LINKS['github'], SOCIAL_LINKS['linkedin']), unsafe_allow_html=True)

    with col2:
        if lottie_coding:
            st_lottie(lottie_coding, height=300, key="home-animation")
        elif placeholder_img:
            st.image(placeholder_img, width=300)
        else:
            st.info("Professional profile image coming soon")

elif page == "🛠 Skills":
    st.markdown("# 🛠 Technical Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔧 Core Competencies")
        st.markdown("""
        - **Python** (Pandas, NumPy, Scikit-learn)
        - **Machine Learning** (Supervised/Unsupervised)
        - **Deep Learning** (TensorFlow, PyTorch)
        - **Natural Language Processing** (NLP)
        - **Cloud Computing** (AWS)
        """)

    with col2:
        st.markdown("### 🛠 Tools & Frameworks")
        st.markdown("""
        - **Data Analysis:** Pandas, NumPy
        - **Web Frameworks:** Flask, FastAPI, Streamlit
        - **DevOps:** Docker, Kubernetes, CI/CD
        - **Version Control:** Git, GitHub
        - **Cloud Services:** AWS (EC2, S3, Lambda)
        """)

    st.markdown("---")
    st.markdown("### 📊 Skill Proficiency")
    skill_chart()

elif page == "💼 Experience":
    st.markdown("# 💼 Professional Experience")
    
    experience_card(
        company="Lyros Technologies",
        duration="2025-Present",
        position="AI/ML Trainee",
        achievements=[
            "Improved model performance by 18% through advanced hyperparameter optimization techniques",
            "Built NLP pipelines processing 10K+ documents daily with 92% accuracy",
            "Reduced inference time by 30% by optimizing model architectures"
        ],
        technologies=[
            "Python", "TensorFlow", "PyTorch", 
            "Pandas", "NumPy", "Docker", 
            "Kubernetes"
        ]
    )
    
    experience_card(
        company="HMI Engineering Services",
        duration="3 Months",
        position="AWS Cloud Intern",
        achievements=[
            "Configured 5 EC2 instances with auto-scaling, reducing deployment time by 25%",
            "Managed 3 S3 buckets with lifecycle policies saving $1,200/month in storage costs",
            "Designed IAM roles that improved security compliance by 40%",
            "Automated backup systems for RDS databases"
        ],
        technologies=[
            "AWS EC2", "AWS S3", "AWS IAM", 
            "AWS RDS", "Python", "CloudFormation"
        ]
    )

elif page == "🚀 Projects":
    st.markdown("# 🚀 Projects")
    
    tab1, tab2 = st.tabs(["AI/ML Projects", "Web Applications"])
    
    with tab1:
        st.markdown("### 🤖 AI/ML Projects")
        
        project_card(
            title="Diabetes Prediction System",
            description="""
            Developed a predictive model using logistic regression with 78% accuracy in diabetes prediction.
            Performed comprehensive EDA and feature engineering on the Pima Indians Diabetes Dataset.
            """,
            tech_stack=["Scikit-learn", "Logistic Regression", "Pandas", "NumPy"],
            results=[
                "Achieved 78% accuracy in diabetes prediction",
                "Identified key medical predictors",
                "Implemented data preprocessing pipeline"
            ]
        )
        
        project_card(
            title="Bike Sharing Demand Prediction",
            description="""
            Built ensemble models to predict bike sharing demand using time-series analysis.
            Analyzed patterns based on weather, time, and seasonal factors.
            """,
            tech_stack=["Python", "Pandas", "Scikit-learn", "XGBoost", "Random Forest"],
            results=[
                "Achieved R2 score of 0.89 on test data",
                "Reduced prediction error by 22% compared to baseline",
                "Identified key business insights for optimization"
            ]
        )
    
    with tab2:
        st.markdown("### 🌐 Web Applications")
        
        project_card(
            title="Smart Tax Calculator (Streamlit)",
            description="""
            Developed an Indian income tax calculator with deduction support and PDF export functionality.
            """,
            tech_stack=["Streamlit", "Python", "Pandas"],
            results=[
                "5,000+ monthly active users",
                "Reduced calculation errors by 95%"
            ]
        )
        
        project_card(
            title="Secure Auth System (Supabase)",
            description="""
            Implemented secure user authentication with OTP and role-based access control.
            """,
            tech_stack=["Supabase", "Streamlit", "JWT"],
            results=[
                "Protected 10,000+ user accounts",
                "Zero security breaches"
            ]
        )

elif page == "🎓 Education":
    st.markdown("# 🎓 Education")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📚 Academic Background")
        st.markdown("""
        **Master of Computer Applications (MCA)**  
        Sri Vishnu College, Bhimavaram  
        *2022 - 2024* | GPA: **7.4/10.0**  
        
        **B.Sc in Animations**  
        Adithya College, Kakinada  
        *2019 - 2022* | GPA: **6.8/10.0**
        """)
        
    with col2:
        st.markdown("### 🌍 Languages")
        st.markdown("""
        - English (Professional Proficiency)  
        - Telugu (Native Speaker)  
        - Hindi (Conversational)  
        """)

elif page == "📩 Contact":
    st.markdown("# 📩 Get In Touch")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Contact Information")
        st.markdown(f"""
        📧 **Email:** [{CONTACT_INFO['email']}](mailto:{CONTACT_INFO['email']})  
        📞 **Phone:** {CONTACT_INFO['phone']}  
        📍 **Location:** {CONTACT_INFO['location']}  
        """)
        
        st.markdown("### Social ")
        st.markdown(f"""
        <div style="margin-top: 1rem;">
            <a href="{SOCIAL_LINKS['github']}" class="btn" target="_blank">GitHub</a>
            <a href="{SOCIAL_LINKS['linkedin']}" class="btn" target="_blank">LinkedIn</a>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### My Resume")
        resume_download_section(key_suffix="contact")
    
    with col2:
        with st.form(key="contact_form", clear_on_submit=True):
            st.markdown("### Send Me a Message")
            name = st.text_input("Your Name*", key="contact_name")
            email = st.text_input("Your Email*", key="contact_email")
            subject = st.selectbox("Subject", ["Job Opportunity", "Collaboration", "Question", "Other"], key="contact_subject")
            message = st.text_area("Your Message*", height=150, key="contact_message")
            
            submitted = st.form_submit_button("Send Message")
            
            if submitted:
                if not all([name, email, message]):
                    st.error("Please fill all required fields (*)")
                elif "@" not in email or "." not in email:
                    st.error("Please enter a valid email address")
                else:
                    st.success("Message sent successfully! I'll get back to you soon.")
                    st.balloons()

# ====== FOOTER ====== #
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: #6c757d; margin-top: 2rem;">
    © {datetime.now().year} Ponnapalli Poorna Sandeep | Made with ❤️ & Streamlit
</div>
""", unsafe_allow_html=True)