import streamlit as st

# Main title
st.title("My Autobiography and Portfolio")

# Navigation
pages = ["Home", "About Me", "Portfolio", "Autobiography"]
selected_page = st.selectbox("Navigate a page", pages)

# Page content
if selected_page == "Home":
    st.title("Home")
 
elif selected_page == "About Me":
    st.title("About Me")

    htp = "https://github.com/dakkkkkk/CSIT342-Portfolio/blob/main/Untitled.png?raw=true"
    # Centered image with name and detailed description
    st.markdown(f"""
        <div style="text-align: center;">
            <img src="{htp}" alt="logo" width="500">
            <p style="font-size: 24px; color: black; font-weight: bold;">Roelan Amerila</p>
            <p style="font-size: 16px; color: grey;">
                I'm a 4th-year college student studying at Cebu Institute of Technology - University. My course is Information Technology.
                <br><br>
                I have a strong passion for technology and programming, and I enjoy working on projects that involve software development and data analysis. 
                Throughout my studies, I have developed skills in various programming languages such as Python, Java, and JavaScript. I am particularly interested in 
                web development and machine learning. 
                <br><br>
                In addition to my academic pursuits, I am actively involved in extracurricular activities and have participated in several hackathons and coding competitions. 
                These experiences have helped me hone my problem-solving skills and work effectively in a team. I am always eager to learn and take on new challenges, 
                and I look forward to contributing to the tech industry in the future.
            </p>
        </div>
    """, unsafe_allow_html=True)

elif selected_page == "Portfolio":
    st.title("Portfolio")
   
elif selected_page == "Autobiography":
    st.title("Autobiography")
