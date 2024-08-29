import streamlit as st
from PIL import Image
import pandas as pd

# Set the title of the web app
st.title("My Autobiography and Portfolio")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select a Page", ["Home", "About Me", "Portfolio", "Contact"])

# Home Page
if page == "Home":
    st.header("Welcome to My Portfolio")
    st.write("""
    Hi, I'm [Your Name], a [Your Profession]. 
    This is a brief showcase of my work and a little about me.
    Use the navigation bar on the left to explore.
    """)
    image = Image.open("profile_picture.jpg")  # Use an image of yourself if available
    st.image(image, caption="This is me!", use_column_width=True)

# About Me Page
elif page == "About Me":
    st.header("About Me")
    st.write("""
    ### Background
    I was born in [City, Country], and I've always been passionate about [Your Passion]. 
    After completing my education at [Your School/University], I began working in [Your Field].
    
    ### Skills
    - Skill 1
    - Skill 2
    - Skill 3
    
    ### Experience
    I have worked with [Company A], [Company B], and [Company C], where I specialized in [Your Specialization].
    """)

    # Timeline of your life
    st.subheader("My Journey")
    journey_data = {
        "Year": ["2000", "2010", "2015", "2020", "2023"],
        "Milestone": ["Born", "Graduated High School", "Graduated College", "Started First Job", "Current Position"]
    }
    df_journey = pd.DataFrame(journey_data)
    st.table(df_journey)

    # Add an expander with more personal details
    with st.expander("More About Me"):
        st.write("In my free time, I enjoy [Hobby 1], [Hobby 2], and [Hobby 3].")

# Portfolio Page
elif page == "Portfolio":
    st.header("Portfolio")
    st.write("Here are some of the projects I've worked on:")

    # Project 1
    st.subheader("Project 1: [Project Title]")
    st.write("Description of the project, tools used, and outcome.")
    st.image("project1_image.jpg", caption="Project 1 Screenshot", use_column_width=True)

    # Project 2
    st.subheader("Project 2: [Project Title]")
    st.write("Description of the project, tools used, and outcome.")
    st.image("project2_image.jpg", caption="Project 2 Screenshot", use_column_width=True)

    # Project 3
    st.subheader("Project 3: [Project Title]")
    st.write("Description of the project, tools used, and outcome.")
    st.image("project3_image.jpg", caption="Project 3 Screenshot", use_column_width=True)

    # Add a chart for your skills
    st.subheader("Skills Breakdown")
    skills_data = {
        "Skill": ["Python", "JavaScript", "HTML/CSS", "SQL", "Machine Learning"],
        "Proficiency": [90, 80, 85, 75, 70]
    }
    df_skills = pd.DataFrame(skills_data)
    st.bar_chart(df_skills.set_index("Skill"))

# Contact Page
elif page == "Contact":
    st.header("Contact Me")
    st.write("I'd love to hear from you! Please fill out the form below.")

    # Contact Form
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Submit")

        if submitted:
            st.write(f"Thank you, {name}! We have received your message.")

    # Display a map of your location (for example, New York)
    st.subheader("My Location")
    st.map()

    # Social media links
    st.subheader("Find me on:")
    st.write("[LinkedIn](https://www.linkedin.com/in/yourprofile)")
    st.write("[GitHub](https://github.com/yourusername)")
    st.write("[Twitter](https://twitter.com/yourusername)")

# Footer
st.sidebar.write("---")
st.sidebar.write("© 2024 [Your Name]. All rights reserved.")
