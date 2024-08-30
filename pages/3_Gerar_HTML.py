import streamlit as st
from utils import call_ai
from utils import format_code

st.set_page_config(page_title="Gerar", layout="wide")

st.header("Gere o seu código HTML")
html_code = st.text_area("Copie e cole o seu código HTML:", height=500)
text_input = st.text_input('Escreva a sua pergunta:', '')

input_model, input_tokens, input_temperature = call_ai.sidebar()

if st.button("Enviar"): 
  response = call_ai.run(input_model, 
                        input_tokens, 
                        input_temperature, 
                        text_input, 
                        html_code,
                        'responda apenas em código HTML, sem comentários')

  col1, col2 = st.columns(2, gap="large")

  # Para limpar o markdown caso venha com isso na resposta
  response_edited = response.removeprefix('```html').removesuffix('```')
  
  with col1:
    st.markdown(f"```html{response_edited }```")

  with col2:
    format_code.html(str(response_edited))