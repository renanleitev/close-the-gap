import streamlit as st

st.set_page_config(page_title="Testar HTML", layout="wide")

col1, col2 = st.columns(2, gap="large")

with col1:
  st.header("Teste o seu código HTML")
  html_code = st.text_area("Copie e cole o seu código HTML para fazer edições e testar em tempo real", height=500)

with col2:
  # Para exibir o HTML com fundo branco
  st.markdown("""
    <style>iframe {background-color: white;}</style>
  """, unsafe_allow_html=True)
  st.components.v1.html(html_code, scrolling=True, height=600)