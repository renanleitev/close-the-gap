import streamlit as st

def save_btn(text):
  if st.button("Salvar"):
    st.success(f"{text} salvo com sucesso.")