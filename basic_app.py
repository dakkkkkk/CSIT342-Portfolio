
import streamlit as st

st.title("My Autobiography and Portfolio")

pages = ["Home", "About Me", "Portfolio", "Autobiography"]

selected_page = st.selectbox("Navigate a page", pages)

