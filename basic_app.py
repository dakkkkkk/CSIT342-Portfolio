import streamlit as st

# Centered main title
st.markdown("<h1 style='text-align: center;'>My Portfolio</h1>", unsafe_allow_html=True)

# Navigation
pages = ["Home", "About Me", "Portfolio", "Contacts"]
selected_page = st.selectbox("", pages)

# Page content
if selected_page == "Home":
    st.title("Home")
 
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
