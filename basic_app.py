import streamlit as st

# Import icons (e.g., from Font Awesome)
st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
""", unsafe_allow_html=True)

# Centered main title with icon above
st.markdown("""
    <div style="text-align: center;">
        <i class="fas fa-laptop-code" style="font-size: 50px; color: #4CAF50;"></i>
        <h1>My Portfolio</h1>
    </div>
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

# Create clickable icons
st.markdown("""
    <style>
        .icon-bar {
            display: flex;
            justify-content: space-evenly;
            margin-bottom: 20px;
        }
        .icon-bar a {
            text-align: center;
            text-decoration: none;
            color: black;
        }
        .icon-bar a:hover {
            color: #4CAF50; /* Change color on hover */
        }
        .icon-bar i {
            font-size: 30px;
        }
    </style>
    <div class="icon-bar">
""", unsafe_allow_html=True)

# Generate clickable icons with links
for page, (icon, label) in page_icons.items():
    st.markdown(f"""
        <a href="?page={page}" title="{label}">
            <i class="{icon}"></i>
            <p>{label}</p>
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
    st.markdown(f"""
        <div style="text-align: center;">
            <img src="{htp}" alt="logo" width="500">
            <p style="font-size: 24px; color: black; font-weight: bold; text-align: center;">Roelan Amerila</p>
            <p style="font-size: 16px; color: black; text-align: justify;">
                I'm a 4th-year college student studying at Cebu Institute of Technology - University. My course is Information Technology.
                <br><br>
                I have a passion for technology and programming, and I enjoy working on projects that involve software development and data analysis. 
                Throughout my studies, I have developed skills in various programming languages such as Python, Java, and JavaScript. I am particularly interested in 
                web development and machine learning. 
            </p>
        </div>
    """, unsafe_allow_html=True)

elif selected_page == "Portfolio":
    st.title("Portfolio")

elif selected_page == "Contacts":
    st.title("Contacts")
