import streamlit as st

st.set_page_config(page_title="Testar HTML", layout="wide")

col1, col2 = st.columns(2, gap="large")

with col1:
  st.header("Teste o seu código HTML")
  html_code = st.text_area("Copie e cole o seu código HTML gerado por Inteligência Artificial", height=500)

with col2:
  st.html(html_code)