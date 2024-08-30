
import streamlit as st


st.title("My Autobiography and Portfolio")

pages = ["Home", "About Me", "Portfolio", "Autobiography"]

selected_page = st.selectbox("Navigate a page", pages)

if selected_page == "Home":
    st.title("Home")
 
elif selected_page == "About Me":
    st.title("About Me")

htp = "https://github.com/dakkkkkk/CSIT342-Portfolio/blob/main/Untitled.png"
st.image(htp, caption= 'logo', width=350)
  
elif selected_page == "Portfolio":
    st.title("Portfolio")
   
elif selected_page == "Autobiography":
    st.title("Autobiography")














