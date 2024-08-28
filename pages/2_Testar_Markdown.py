import streamlit as st
from utils import shared_ui

st.set_page_config(page_title="Testar Markdown", layout="wide")

col1, col2 = st.columns(2, gap="large")

with col1:
  st.header("Teste o seu código Markdown")
  md_code = st.text_area("Copie e cole o seu código Markdown para fazer edições e testar em tempo real", height=500)
  shared_ui.save_btn("Markdown")

with col2:
  st.markdown(md_code)