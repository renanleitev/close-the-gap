import streamlit as st
from utils import format_code, shared_ui

st.set_page_config(page_title="Testar HTML", layout="wide")

col1, col2 = st.columns(2, gap="large")

with col1:
  st.header("Teste o seu código HTML")
  html_code = st.text_area("Copie e cole o seu código HTML para fazer edições e testar em tempo real", height=500)
  shared_ui.save_btn("HTML")

with col2:
  format_code.html(html_code)