import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="John Joseph Laborada | Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <script>
        window.scrollTo(0, 0);
    </script>
    """,
    unsafe_allow_html=True
)

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
ASSETS_DIR = current_dir / "assets"

PROFILE = {
    "name": "JOHN JOSEPH LABORADA",
    "role": "Aspiring Software Developer | UI/UX Design",
    "location": "Carcar City, Cebu, Philippines",
    "about_short": (
        "I'm a fresh IT graduate who's been building web projects throughout college. I enjoy turning ideas into something real "
        "whether it's a full system, a clean UI, or just a small side project. I'm always learning, always building, "
        "and always looking for the next thing to figure out."
    ),
    "links": {
        "GitHub": "https://github.com/moshiverse",
        "LinkedIn": "https://www.linkedin.com/in/john-joseph-laborada-8b341430a/",
        "Email": "mailto:josephjohn.laborada@gmail.com",
    },
}

ABOUT_ME_TEXT = """
I am John Joseph Laborada, 22 years of age and recently graduated with a degree of Bachelors of Science in Information Technology, where I developed a strong interest 
in software development and solving problems through technology. My journey in tech started with 
curiosity about how applications and systems work, and over time, that curiosity turned into a 
passion for building them myself. Through various school projects and activities, I gained 
experience in programming, web development, and working with classmates as a team to complete 
systems and meet deadlines.
<br><br>
I am always open to learning new tools and technologies that can improve my skills as a 
developer. I enjoy taking on challenges because they help me grow and think more critically. 
Outside of coding, I like playing chess, watching movies and anime, and working on small side 
projects that allow me to practice and explore new ideas in programming.
"""

SKILLS_DATA = {
    "Programming / Web": ["ReactJS", "Spring Boot", "Java", "C", "C++", "Python", "HTML", "CSS", "Tailwind CSS"],
    "UI/UX / Design": ["Figma", "Canva", "Wireframing", "Wordpress"],
    "Databases & Tools": ["MySQL", "Supabase (PostgreSQL)", "Git", "GitHub", "Postman", "Active Pieces"],
    "Soft Skills": ["Problem Solving", "Team Collaboration", "Communication", "Time management", "Adaptability", "Work Ethics", "Flexibility"],
}

PROJECTS = [
    {
        "name": "Online Bus Ticketing System",
        "type": "Bus Ticketing System",
        "desc": "Bus ticketing platform with seat selection, QR-based boarding, online payments, route management, and analytics dashboard.",
        "tags": ["JavaScript", "Java", "Kotlin"],
        "img": "busmate.png",
        "links": {
            "GitHub": "https://github.com/moshiverse/BusMate-OnlineTicketingSystem-IT342-G01-Group6"
        },
    },
    {
        "name": "IEEE Docs Evaluator",
        "type": "Academic Tool",
        "desc": "IEEE Docs Evaluator consolidates four separate AI-driven document evaluator systems into a single integrated application.",
        "tags": ["Java", "Javascript", "Vercel", "OpenAI API"],
        "img": "IEEE-Docs.png",
        "links": {
            "GitHub": "https://github.com/Hello-Kalibutan-Team/IEEE-Docs-Evaluator"
        },
    },
    {
        "name": "InTurn.AI - Chatbot",
        "type": "Intern Tracking Assistant",
        "desc": "An AI-powered internship tracking assistant for university students. Features hours tracking, mentor communication, and automated report generation.",
        "tags": ["Python", "Streamlit", "OpenAI API"],
        "img": "InTurnAI.png",
        "links": {
            "GitHub": "https://github.com/AI-Chatbotssss/AI-Chatbot"
        },
    },
]

EXPERIENCE = [
    {
        "title": "IT Intern – WordPress Developer",
        "company": "Knowles Training Institute, Singapore (Remote)",
        "date": "Jan 2026 – Apr 2026",
        "points": [
            "Developed a responsive booking website using WordPress and Elementor.",
            "Designed UI/UX layouts for desktop and mobile devices.",
            "Implemented email request handling for bookings and inquiries."
        ]
    }
]

EDUCATION = [
    {
        "degree": "BS Information Technology",
        "school": "Cebu Institute of Technology - University",
        "year": "2022 – 2026",
        "sub": "Recently Graduated",
        "desc": "Relevant Coursework: Web Development, Data Management, Applied AI, Analytics, UI/UX Design",
    },
    {
        "degree": "AWS Academy Graduate",
        "school": "Cloud Foundations & Architecting",
        "year": "2025",
        "sub": "Amazon Web Services",
        "desc": "Comprehensive training in cloud security, architecture, and core AWS services.",
    },
    {
        "degree": "TESDA AI Training",
        "school": "StackTrek",
        "year": "2026",
        "sub": "Basic Automation",
        "desc": "Basic training in Configuring Basic AI Driven Workflows",
    },
]

st.markdown(
    """
    <style>
        html, body {
            scroll-behavior: auto !important;
        }
        .stApp {
            background-color: #0A0A0A !important;
        }

        /* Fixed texture overlay — cubes pattern at 20% opacity */
        .stApp::before {
            content: "";
            position: fixed;
            inset: 0;
            background-image: url('https://www.transparenttextures.com/patterns/cubes.png');
            background-repeat: repeat;
            opacity: 0.20;
            pointer-events: none;
            z-index: 0;
        }

        /* Make sure all Streamlit content sits above the texture */
        .stApp > * {
            position: relative;
            z-index: 1;
        }
        
        header[data-testid="stHeader"] {
            z-index: 1001 !important;
            background-color: #0b0c10; 
        }
        
        .navbar {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 1002;
        padding: 26px 50px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        pointer-events: none;
        background: transparent;
        }

        .navbar::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(11, 12, 16, 0.95);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-bottom: 1px solid rgba(168, 85, 247, 0.2);
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        z-index: -1;
        pointer-events: none;
        }
        
        .brand-name,
        .navbar-links,
        .navbar a {
            pointer-events: auto;
        }

        .navbar-links { 
            display: flex; 
            gap: 30px; 
        }
        
        .navbar a {
            color: #b0b0b0; 
            text-decoration: none; 
            font-size: 0.9rem; 
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            transition: all 0.3s ease;
        }
        
        .navbar a:hover { 
            color: #d8b4fe;
            text-shadow: 0 0 8px rgba(168, 85, 247, 0.6);
        }

        .brand-name {
            font-weight: 900; 
            font-size: 1.2rem;
            background: linear-gradient(90deg, #d8b4fe, #a855f7);
            -webkit-background-clip: text; 
            -webkit-text-fill-color: transparent;
            letter-spacing: 1px;
        }
        
        .anchor-offset { 
            position: relative;
            top: -200px;
            height: 0;
            pointer-events: none; 
        }
        
        div[data-testid="stVerticalBlockBorderWrapper"] {
            padding: 24px 28px !important;
        }
        
        .justified-text {
            text-align: justify;
            line-height: 1.7;
            font-size: 1rem;
            color: #d1d5db;
            padding: 6px 2px;
        }

        .skill-pill {
            display: inline-block;
            background: rgba(168, 85, 247, 0.15);
            border: 1px solid rgba(168, 85, 247, 0.3);
            color: #e9d5ff;
            padding: 6px 16px;
            border-radius: 99px;
            font-size: 0.85rem;
            margin: 5px;
            font-weight: 500;
            transition: all 0.2s;
        }
        
        .skill-pill:hover {
            background: rgba(168, 85, 247, 0.3);
            transform: translateY(-2px);
        }
        
        .skill-container {
            background-color: rgba(255,255,255,0.03);
            border-radius: 16px;
            padding: 24px;
            border: 1px solid rgba(255,255,255,0.08);
        }
        
        .section-header {
            font-size: 2rem;
            font-weight: 800;
            margin-bottom: 15px;
            color: #f3f4f6;
            text-shadow: 0 0 20px rgba(168, 85, 247, 0.15);
        }

        .equal-height-container {
            display: flex;
            gap: 20px;
            margin-bottom: 20px;
        }
        
        .info-box {
            background-color: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 12px;
            padding: 30px;
            color: #e5e7eb;
            display: flex;
            flex-direction: column;
        }
        
        .box-wide { flex: 2; }
        .box-narrow { flex: 1; }
        
        @media (max-width: 768px) {
            .navbar-links { display: none; }
            .equal-height-container { flex-direction: column; }
        }

        .project-card {
        height: 650px;
        display: flex;
        flex-direction: column;
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 16px;
        padding: 20px;
        overflow: hidden;
        }

        .project-card img {
            width: 100%;
            border-radius: 10px;
        }

        .project-content {
            flex-grow: 1;
        }

        .project-tags {
            margin-top: auto;
        }

        .project-card {
            transition: all 0.3s ease;
        }

        .project-card:hover {
            transform: translateY(-8px);
            border-color: rgba(168, 85, 247, 0.5);
            box-shadow: 0 15px 35px rgba(168, 85, 247, 0.15);
        }

        .social-grid {
        display:flex;
        gap:16px;
        margin-top:20px;
    }

    .social-card {
        width:70px;
        height:70px;
        display:flex;
        justify-content:center;
        align-items:center;
        background:#090909;
        border:1px solid rgba(255,255,255,.08);
        border-radius:20px;
        text-decoration:none;
        transition:.3s ease;
    }

    .social-card:hover {
        transform:translateY(-6px);
        border-color:rgba(168,85,247,.5);
        box-shadow:0 15px 35px rgba(168,85,247,.15);
    }

    .social-card svg {
        width:30px;
        height:30px;
    }
    
    </style>

    """,
    unsafe_allow_html=True
)

def load_pdf_bytes(pdf_name: str) -> bytes | None:
    pdf_path = ASSETS_DIR / pdf_name
    if pdf_path.exists():
        return pdf_path.read_bytes()
    return None

def load_image(image_name):
    image_path = ASSETS_DIR / image_name
    if image_path.exists():
        return str(image_path)
    return None

st.markdown('<div id="home" class="anchor-offset"></div>', unsafe_allow_html=True)

c1, c2 = st.columns([2.5, 1], gap="medium")

with c1:
    st.markdown("<div style='font-size: 3.5rem; font-weight: 800; line-height: 1.1;'>John Joseph Laborada</div>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='color: #a855f7; margin-bottom: 20px;'>{PROFILE['role']}</h3>", unsafe_allow_html=True)
    st.markdown(f"<div class='justified-text'>{PROFILE['about_short']}</div>", unsafe_allow_html=True)

    st.write("")
    cols = st.columns(4, gap="small")
    with cols[0]:
        st.link_button("GitHub", PROFILE["links"]["GitHub"], use_container_width=True)
    with cols[1]:
        st.link_button("LinkedIn", PROFILE["links"]["LinkedIn"], use_container_width=True)
    with cols[2]:
        st.link_button("Email", PROFILE["links"]["Email"], use_container_width=True)
    with cols[3]:
        Resume_bytes = load_pdf_bytes("Laborada-Resume.pdf")
        if Resume_bytes:
            st.download_button(
                "Resume",
                data=Resume_bytes,
                file_name="Laborada_Resume.pdf",
                mime="application/pdf",
                use_container_width=True
            )
        else:
            st.button("Resume (missing)", disabled=True, use_container_width=True)

    
with c2:
    avatar_path = load_image("avatar.jpg")
    if avatar_path:
        st.markdown(
            """
            <div style="display:flex; justify-content:flex-end; margin-top:40px;">
            """,
            unsafe_allow_html=True
        )
        st.image(avatar_path, width=250)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("Place 'avatar.jpg' in assets folder")


st.markdown("---")

st.markdown('<div id="about" class="anchor-offset"></div>', unsafe_allow_html=True)
st.markdown("<div class='section-header'>About Me</div>", unsafe_allow_html=True)

st.markdown(
    f"""
    <div class="equal-height-container">
        <div class="info-box box-wide">
            <div class="justified-text">{ABOUT_ME_TEXT}</div>
        </div>
        <div class="info-box box-narrow">
            <h3 style="margin-top: 0; color: #a855f7;">Details</h3>
            <p><strong>Location:</strong><br>{PROFILE['location']}</p>
            <div style="flex-grow:1;"></div>
            <p><strong>Status:</strong><br>Available</p>
            <div style="flex-grow:1;"></div>
            <p><strong>Interests:</strong><br>Chess, Anime, Coding, AI</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('<div id="skills" class="anchor-offset"></div>', unsafe_allow_html=True)
st.markdown("<div class='section-header'>Skills & Technologies</div>", unsafe_allow_html=True)

# Tabs (safe)
tabs = st.tabs(list(SKILLS_DATA.keys()))

for i, (category, skills) in enumerate(SKILLS_DATA.items()):
    with tabs[i]:
        pills_html = "".join(
            [f"<span class='skill-pill'>{skill}</span>" for skill in skills]
        )

        st.markdown(
            f"""
            <div class="skill-container">
                <h4 style="margin-bottom: 15px; color: #d8b4fe;">
                    {category}
                </h4>
                <div>{pills_html}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


st.markdown("---")
st.markdown('<div id="experience" class="anchor-offset"></div>', unsafe_allow_html=True)
st.markdown("<div class='section-header'>Experience</div>", unsafe_allow_html=True)

# IMPORTANT: make sure EXPERIENCE is defined only ONCE in your whole project
for exp in EXPERIENCE:
    with st.container(border=True):
        c1, c2 = st.columns([4, 1])

        with c1:
            st.markdown(f"### {exp['title']}")
            st.markdown(f"**{exp['company']}**")

            for point in exp.get("points", []):
                st.markdown(f"• {point}")

        with c2:
            st.markdown(
                f"<h4 style='text-align:right; color:#a855f7'>{exp['date']}</h4>",
                unsafe_allow_html=True
            )


st.markdown("---")
st.markdown('<div id="projects" class="anchor-offset"></div>', unsafe_allow_html=True)
st.markdown("<div class='section-header'>Featured Projects</div>", unsafe_allow_html=True)

if PROJECTS:

    cols_per_row = 3
    p_cols = st.columns(cols_per_row)

    for i, project in enumerate(PROJECTS):
        with p_cols[i % cols_per_row]:

            with st.container(border=True):

                img_path = load_image(project.get("img"))

                if img_path:
                    st.image(img_path, use_container_width=True)

                st.subheader(project.get("name", "Untitled Project"))
                st.caption(project.get("type", ""))

                st.write(project.get("desc", ""))

                tags = project.get("tags", [])
                if tags:
                    st.markdown(" ".join([f"`{t}`" for t in tags]))

                st.write("")

                links = project.get("links", {})
                if links:
                    for label, url in links.items():
                        st.link_button(label, url, use_container_width=True)
else:
    st.info("No projects found.")



st.markdown("---")
st.markdown('<div id="education" class="anchor-offset"></div>', unsafe_allow_html=True)
st.markdown("<div class='section-header'>Education & Certifications</div>", unsafe_allow_html=True)

for edu in EDUCATION:
    with st.container(border=True):

        c_edu1, c_edu2 = st.columns([3, 1])

        with c_edu1:
            st.markdown(f"### {edu.get('degree', '')}")
            st.markdown(f"**{edu.get('school', '')}**")
            st.caption(edu.get("sub", ""))
            st.write(edu.get("desc", ""))

        with c_edu2:
            st.markdown(
                f"<h4 style='text-align:right; color:#a855f7'>{edu.get('year', '')}</h4>",
                unsafe_allow_html=True
            )


st.markdown(
    """
    <div style="text-align: center; margin-top: 50px; padding: 20px; border-top: 1px solid #333; color: #666;">
        <p>© 2026 John Joseph Laborada · Built with Streamlit</p>
    </div>
    """,
    unsafe_allow_html=True
)
