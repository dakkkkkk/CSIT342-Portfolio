
import streamlit as st

st.markdown("""
 <style>
 
body{ 
background-color: #f0f2f6;

}

.stTitle{

font-size: 18px;

}
 </style>
    """, unsafe_allow_html=True)

st.title("My Autobiography and Portfolio")

pages = ["Home", "About Me", "Portfolio", "Autobiography"]

selected_page = st.selectbox("Navigate a page", pages)

















