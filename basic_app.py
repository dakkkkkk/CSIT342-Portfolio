import streamlit as st

# Centered main title
st.markdown("<h1 style='text-align: center;'>My Portfolio</h1>", unsafe_allow_html=True)

# Navigation
pages = ["Home", "About Me", "Portfolio", "Contacts"]
selected_page = st.selectbox("", pages)

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
