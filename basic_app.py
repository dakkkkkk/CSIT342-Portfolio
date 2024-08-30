import streamlit as st

# Import icons (e.g., from Font Awesome)
st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
""", unsafe_allow_html=True)

# Define pages
pages = ["Home", "About Me", "Portfolio", "Contacts"]

# Create a dictionary mapping pages to icons and their labels
page_icons = {
    "Home": ("fas fa-home", "Home"),
    "About Me": ("fas fa-user", "About Me"),
    "Portfolio": ("fas fa-briefcase", "Portfolio"),
    "Contacts": ("fas fa-envelope", "Contacts")
}

# Navbar with clickable icons
st.markdown("""
    <style>
        .navbar {
            display: flex;
            justify-content: center;
            background-color: #333;
            padding: 10px 0;
            position: sticky;
            top: 0;
            z-index: 1000;
        }
        .navbar a {
            color: white;
            padding: 14px 20px;
            text-decoration: none;
            font-size: 17px;
            text-align: center;
            transition: background-color 0.3s;
        }
        .navbar a:hover {
            background-color: #575757;
        }
        .navbar i {
            margin-right: 8px;
        }
    </style>
    <div class="navbar">
""", unsafe_allow_html=True)

# Generate clickable icons with links in the navbar
for page, (icon, label) in page_icons.items():
    st.markdown(f"""
        <a href="?page={page}">
            <i class="{icon}"></i>{label}
        </a>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Get selected page from URL parameters
params = st.experimental_get_query_params()
selected_page = params.get("page", ["Home"])[0]

# Page content
if selected_page == "Home":
    st.title("Welcome to My Portfolio")

    st.markdown("""
        <p style="font-size: 18px; text-align: justify; color: black;">
        Hello and welcome to my portfolio! My name is Roelan Amerila, and I am a dedicated and passionate 4th-year student 
        pursuing a degree in Information Technology at Cebu Institute of Technology - University. 
        <br><br>
        Throughout my academic journey, I have cultivated a strong foundation in programming, software development, and data analysis. 
        My interests lie particularly in web development and machine learning, where I have had the opportunity to work on various projects 
        that have honed my skills in these areas. 
        <br><br>
        This portfolio showcases my academic projects, skills, and experiences that I have gained over the years. I am constantly learning and 
        am eager to take on new challenges in the tech world. Feel free to explore and learn more about my journey!
        </p>
    """, unsafe_allow_html=True)

elif selected_page == "About Me":
    st.title("About Me")

    htp = "https://github.com/dakkkkkk/CSIT342-Portfolio/blob/main/Untitled.png?raw=true"
    # Centered image with name and justified paragraphs
    st.markdown("""
        <div style="text-align: center;">
            <img src="{htp}" alt="logo" width="500">
            <p style="font-size: 24px; color: black; font-weight: bold; text-align: center;">Roelan Amerila</p>
            <p style="font-size: 16px; color: black; text-align: justify;">
                I'm a 4th-year college student studying at Cebu Institute of Technology - University. My course is Information Technology.
                <br><br>
                I have a passion for technology and programming
