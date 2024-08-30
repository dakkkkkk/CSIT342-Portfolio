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
    
    # Add contact details with GitHub icon
    st.markdown("""
        <div style="text-align: center;">
            <p style="font-size: 18px; color: black;">You can reach me through the following platforms:</p>
            <p style="font-size: 16px; color: black;">
                <a href="https://github.com/dakkkkkk" target="_blank" style="text-decoration: none; color: black;">
                    <i class="fab fa-github" style="font-size: 30px; margin-right: 10px;"></i>
                    GitHub
                </a>
            </p>
        </div>
    """, unsafe_allow_html=True)

# Adding Font Awesome CDN for icons
st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
""", unsafe_allow_html=True)
