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
    # Correct indentation here
    st.markdown(f"""
        <div style="text-align: center;">
            <img src="{htp}" alt="Me" width="500">
        </div>
    """, unsafe_allow_html=True)

elif selected_page == "Portfolio":
    st.title("Portfolio")
   
elif selected_page == "Autobiography":
    st.title("Autobiography")
