import streamlit as st

st.set_page_config(page_title="Testar Markdown", layout="wide")

col1, col2 = st.columns(2, gap="large")

with col1:
  st.header("Teste o seu código Markdown")
  md_code = st.text_area("Copie e cole o seu código Markdown para fazer edições e testar em tempo real", height=500)

with col2:
  st.markdown(md_code)