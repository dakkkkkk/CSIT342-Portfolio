import streamlit as st

# Function to apply dark mode CSS
def apply_dark_mode():
    st.markdown("""
        <style>
            .main {
                background-color: #121212;
                color: #e0e0e0;
            }
            .header {
                background-color: #1f1f1f;
                color: #e0e0e0;
                padding: 20px;
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
                text-align: center;
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
            .main {
                background-color: #f4f4f4;
                color: #000000;
            }
            .header {
                background-color: #2c3e50;
                color: white;
                padding: 20px;
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
                text-align: center;
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
        pursuing a degree in Informat
