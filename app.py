import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie

# Load Lottie animation from URL
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            st.warning(f"⚠️ Failed to load Lottie animation from URL (status code: {r.status_code})")
            return None
        return r.json()
    except Exception as e:
        st.warning(f"⚠️ Exception occurred while loading Lottie animation: {e}")
        return None

# Page Config
st.set_page_config(page_title="Ponnapalli Poorna Sandeep | Portfolio", page_icon="🧑‍💻", layout="wide")

# ✅ Load Lottie animation
lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_qp1q7mct.json")

# CSS Styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@400;700&display=swap');
html, body, [class*="css"] {
    font-family: 'Roboto Slab', serif;
}
.main-title {
    font-size: 56px;
    font-weight: 700;
    color: #1abc9c;
    margin-bottom: 12px;
}
.section-title {
    font-size: 32px;
    font-weight: 600;
    color: #2980b9;
    margin-top: 30px;
    border-left: 5px solid #2980b9;
    padding-left: 12px;
}
.card {
    background-color: #ffffff;
    border-radius: 15px;
    padding: 25px;
    box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
    margin-bottom: 25px;
    transition: transform 0.3s ease;
    color: #2c3e50;
}
.card h4 {
    color: #2c3e50;
}
.card:hover {
    transform: scale(1.02);
    box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.15);
}
.footer {
    text-align: center;
    color: #7f8c8d;
    font-size: 14px;
    margin-top: 50px;
}
.social-buttons a {
    margin: 0 8px;
    text-decoration: none;
    font-weight: bold;
    color: white;
    background-color: #1abc9c;
    padding: 8px 16px;
    border-radius: 8px;
}
.social-buttons a:hover {
    background-color: #16a085;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
try:
    st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png", width=150)
except:
    st.sidebar.image(Image.new("RGB", (150, 150), color=(220, 220, 220)))

st.sidebar.markdown("## 💼 Ponnapalli Poorna Sandeep")
st.sidebar.markdown("**📧 Email:** sanjusandeep846@gmail.com")
st.sidebar.markdown("**📞 Phone:** +91 7780242441")
st.sidebar.markdown("**📍 Location:** Andhra Pradesh, India")

menu = st.sidebar.radio("Navigate", [
    "Home", "Technical Skills", "Internship", "Work Experience", "Project", "Education & Languages", "Contact"
])

# Download Resume Button
try:
    with open("Ponnapalli Poorna Sandeep_Resume2.docx", "rb") as file:
        st.sidebar.download_button(
            label="📄 Download Resume",
            data=file,
            file_name="Ponnapalli_Poorna_Sandeep_Resume2.docx",
            mime="application/octet-stream"
        )
except FileNotFoundError:
    st.sidebar.warning("⚠️ Resume file not found!")

# Main Sections
if menu == "Home":
    st.markdown('<div class="main-title">👋 Hello, I\'m Ponnapalli Poorna Sandeep</div>', unsafe_allow_html=True)
    st.write("Passionate about AI, ML, and Cloud Technologies. Building scalable, intelligent, and secure systems.")
    if lottie_coding:
        st_lottie(lottie_coding, height=300, key="coding")
    else:
        st.info("⚠️ Could not load animation at this time.")
    st.markdown("""
        <div class="social-buttons">
            <a href="https://github.com/dashboard" target="_blank">GitHub</a>
            <a href="http://linkedin.com/in/sandeep-ponnapalli-abb86a190" target="_blank">LinkedIn</a>
        </div>
    """, unsafe_allow_html=True)

elif menu == "Technical Skills":
    st.markdown('<div class="section-title">🛠️ Technical Skills</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card">
        <h4>💻 Technical</h4>
        <ul>
            <li>Python</li>
            <li>Machine Learning</li>
            <li>Artificial Intelligence</li>
            <li>Natural Language Processing (NLP)</li>
            <li>Neural Networks</li>
        </ul>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="card">
        <h4>🔧 Functional</h4>
        <ul>
            <li>Team Building</li>
            <li>Project Management</li>
            <li>Communication</li>
            <li>Quick Learner</li>
        </ul>
        </div>""", unsafe_allow_html=True)

elif menu == "Internship":
    st.markdown('<div class="section-title">📚 AWS Internship</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
    <b>Organization:</b> HMI Engineering Services, Vizag<br>
    <b>Duration:</b> Feb 2024 – Apr 2024<br><br>
    <ul>
        <li>Configured EC2 for deployment.</li>
        <li>Managed secure S3 buckets.</li>
        <li>Designed IAM policies.</li>
        <li>Used AWS: EC2, S3, IAM, VPC, CloudWatch.</li>
    </ul>
    </div>""", unsafe_allow_html=True)

elif menu == "Work Experience":
    st.markdown('<div class="section-title">💼 Work Experience</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
    <b>Role:</b> Software Engineer<br>
    <b>Company:</b> Lyros Technologies Pvt. Ltd<br>
    <b>Domain:</b> AI/ML<br>
    <b>Duration:</b> Jan 2025 – Present<br><br>
    <ul>
        <li>Worked on data preprocessing and deployment.</li>
        <li>Collaborated on scalable ML solutions.</li>
        <li>Optimized models and automation pipelines.</li>
    </ul>
    </div>""", unsafe_allow_html=True)

elif menu == "Project":
    st.markdown('<div class="section-title">📁 Project</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
    <h4>Privacy Protection and Intrusion Avoidance for Cloudlet-Based Medical Data Sharing</h4>
    <ul>
        <li>Improved healthcare using wearable & cloudlet tech.</li>
        <li>Built trust models and intrusion detection systems.</li>
    </ul>
    </div>""", unsafe_allow_html=True)

elif menu == "Education & Languages":
    st.markdown('<div class="section-title">🎓 Education</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">MCA, Sri Vishnu College, Bhimavaram</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🌐 Languages</div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><ul><li>English</li><li>Telugu</li><li>Hindi</li></ul></div>', unsafe_allow_html=True)

elif menu == "Contact":
    st.markdown('<div class="section-title">📞 Contact Me</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
    <b>📧 Email:</b> sanjusandeep846@gmail.com<br>
    <b>📞 Phone:</b> +91 7780242441<br>
    <b>📍 Location:</b> Andhra Pradesh, India<br>
    </div>""", unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">© 2025 Ponnapalli Poorna Sandeep • Built with ❤️ using Streamlit</div>', unsafe_allow_html=True)
