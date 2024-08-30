
import streamlit as st

st.title("My Autobiography and Portfolio")

pages = ["Home", "About Me", "Portfolio", "Autobiography"]

selected_page = st.selectbox("Navigate a page", pages)

















st.markdown("""
 <style>
body{ 
background-color: #f0f2f6;

}
 </style>
    """, unsafe_allow_html=True)

