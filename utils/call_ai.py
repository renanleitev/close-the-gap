import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Carregando variáveis de ambiente
load_dotenv()

# Configuração padrão
model_ia = "llama-3.1-70b-versatile"
max_tokens = 1000
temperature = 0.7

# https://console.groq.com/settings/limits
list_ia = [
    "gemma-7b-it", 
    "gemma2-9b-it", 
    "llama-3.1-70b-versatile", 
    "llama-3.1-8b-instant", 
    "llama-guard-3-8b",
    "llama3-70b-8192",
    "llama3-8b-8192",
    "llama3-groq-70b-8192-tool-use-preview",
    "llama3-groq-8b-8192-tool-use-preview",
    "mixtral-8x7b-32768",
]

# Barra Lateral
def sidebar():
  st.sidebar.markdown("# Configurações de IA")
  input_model = st.sidebar.selectbox(
      "Modelo de IA",
      (list_ia),
      index=list_ia.index(model_ia)
  )
  input_tokens = int(st.sidebar.number_input("Tokens", value=max_tokens))
  input_temperature = float(st.sidebar.number_input("Temperatura", value=temperature))

  if st.sidebar.button("Salvar", use_container_width=True):
    st.sidebar.success("Configurações salvas com sucesso.")

  return input_model, input_tokens, input_temperature

def run(input_model, input_tokens, input_temperature, text_input, content, message):
  response = ''

  if text_input and content:
    # Connect to the GROQ API
    client = Groq(
      api_key=os.environ.get("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
      messages=[
          {
              "role": "user",
              "content": f'{text_input}, {message}: {content}',
          }
      ],
      model=input_model,
      max_tokens=input_tokens,
      temperature=input_temperature
    )

    response = chat_completion.choices[0].message.content

  return response
