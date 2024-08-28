import streamlit as st

def html(value, height=600):
  st.markdown("""
    <style>iframe {background-color: white;}</style>
  """, unsafe_allow_html=True)
  st.components.v1.html(value, scrolling=True, height=height)