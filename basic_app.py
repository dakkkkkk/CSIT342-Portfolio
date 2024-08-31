import streamlit as st

# Function to apply dark mode CSS
def apply_dark_mode():
    st.markdown("""
        <style>
            body {
                background-color: #121212;
                color: #e0e0e0;
                font-family: 'Arial', sans-serif;
            }
            .header {
                background-image: url('https://example.com/your-banner.jpg');
                background-size: cover;
                color: #ffffff;
                padding: 40px:
                text-align: center;
                border-radius: 10px;
            }
            .content {
                padding: 20px;
            }
            .contacts {
                background-color: #1e1e1e;
                border-radius: 10px;
                padding: 20px;
                text-align: justify;
            }
            .contacts a {
                text-decoration: none;
                color: #e0e0e0;
            }
            .contacts a:hover {
                text-decoration: underline;
            }
            .contact-icon {
                font-size: 30px;
                margin-right: 10px;
            }
        </style>
    """, unsafe_allow_html=True)

# Function to apply light mode CSS
def apply_light_mode():
    st.markdown("""
        <style>
            body {
                background-color: #f4f4f4;
                color: #000000;
                font-family: 'Arial', sans-serif;
            }
            .header {
                background-image: url('https://example.com/your-banner.jpg');
                background-size: cover;
                color: white;
                padding: 40px;
                text-align: center;
                border-radius: 10px;
            }
            .content {
                padding: 20px;
            }
            .contacts {
                background-color: #ecf0f1;
                border-radius: 10px;
                padding: 20px;
                text-align: justify;
            }
            .contacts a {
                text-decoration: none;
                color: #2c3e50;
            }
            .contacts a:hover {
                text-decoration: underline;
            }
            .contact-icon {
                font-size: 30px;
                margin-right: 10px;
            }
        </style>
    """, unsafe_allow_html=True)

# Initialize session state for theme if not already present
if 'theme' not in st.session_state:
    st.session_state.theme = 'Light Mode'

# Sidebar theme selection
st.sidebar.title("Settings")
theme = st.sidebar.selectbox("Select Theme", ["Light Mode", "Dark Mode"], index=["Light Mode", "Dark Mode"].index(st.session_state.theme))

# Update theme in session state
if theme != st.session_state.theme:
    st.session_state.theme = theme

# Apply the selected theme
if st.session_state.theme == "Dark Mode":
    apply_dark_mode()
else:
    apply_light_mode()

# Centered main title
st.markdown("<div class='header'><h1>My Portfolio</h1></div>", unsafe_allow_html=True)

# Navigation
pages = ["Home", "About Me", "Portfolio", "Contacts"]
selected_page = st.selectbox("", pages)

# Page content
if selected_page == "Home":
    st.markdown("<div class='content'>", unsafe_allow_html=True)
    st.title("Welcome to My Portfolio")
    st.markdown("""
        <p style="font-size: 18px; text-align: justify;">
        Hello and welcome to my portfolio! My name is Roelan Amerila, and I am a dedicated and passionate 4th-year student 
        pursuing a degree in Information Technology at Cebu Institute of Technology - University. 
        </p>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

elif selected_page == "About Me":
    st.markdown("<div class='content'>", unsafe_allow_html=True)
    st.title("About Me")
    
    htp = "https://github.com/dakkkkkk/CSIT342-Portfolio/blob/main/Untitled.png?raw=true"
    st.markdown(f"""
        <div style="text-align: center;">
            <img src="{htp}" alt="logo" width="500" style="border-radius: 10px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
            <p style="font-size: 24px; font-weight: bold;">Roelan Amerila</p>
            <p style="font-size: 16px; text-align: justify;">
                I'm a 4th-year college student studying at Cebu Institute of Technology - University. My course is Information Technology.
                <br><br>
                I have a passion for technology and programming, and I enjoy working on projects that involve software development and data analysis. 
                Throughout my studies, I have developed skills in various programming languages such as Python, Java, and JavaScript. I am particularly interested in 
                web development and machine learning. 
            </p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

elif selected_page == "Portfolio":
    st.markdown("<div class='content'>", unsafe_allow_html=True)
    st.title("Portfolio")
    
    htp = "https://github.com/dakkkkkk/CSIT342-Portfolio/blob/main/Untitled.png?raw=true"
    st.markdown(f"""
        <div style="text-align: center;">
            <img src="{htp}" alt="Your Picture" width="300" style="border-radius: 50%; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <h2>Education</h2>
        <p style="font-size: 18px; text-align: justify;">
        <b>Gradeschool:</b> University of San Jose Recoletos
        <br>
        <b>High School:</b> Holy Rosary School of Pardo
        <br>
        <b>Senior High School:</b> Cebu Institute of Technology - University
        <br>
        <b>College:</b> Cebu Institute of Technology - University, Information Technology
        </p>
        
        <h2>Skills</h2>
        <ul style="font-size: 18px; text-align: justify;">
            <li>Programming Languages: Python, Java, JavaScript</li>
            <li>Web Development: HTML, CSS, JavaScript, React</li>
            <li>Database Management: MySQL, PostgreSQL</li>
            <b>Tools & Technologies:</b> Git, Streamlit
        </ul>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

elif selected_page == "Contacts":
    st.markdown("<div class='contacts'>", unsafe_allow_html=True)
    st.title("Contacts")
    
    # Add justified contact details with icons
    st.markdown(f"""
        <div style="text-align: justify;">
            <p style="font-size: 18px;">You can reach me through the following platforms:</p>
            <p style="font-size: 16px;">
                <a href="mailto:roelanamerila@gmail.com" target="_blank">
                    <i class="fas fa-envelope contact-icon"></i>
                    Gmail: roelanamerila@gmail.com
                </a>
            </p>
            <p style="font-size: 16px;">
                <a href="https://github.com/dakkkkkk" target="_blank">
                    <i class="fab fa-github contact-icon"></i>
                    GitHub: dakkkkkk
                </a>
            </p>
            <p style="font-size: 16px;">
                <a href="https://facebook.com/yourprofile" target="_blank">
                    <i class="fab fa-facebook contact-icon"></i>
                    Facebook: yourprofile
                </a>
            </p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
