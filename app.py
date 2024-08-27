import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import os
from groq import Groq
from dotenv import load_dotenv

# Carregando as variáveis de ambiente
load_dotenv()

# Configurando a IA
# https://console.groq.com/settings/limits

# Configuração padrão
model_ia = "llama-3.1-70b-versatile"
max_tokens = 1000
temperature = 0.7

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

# Streamlit webpage layout
st.title('Close The Gap')
st.write('Plataforma de ensino que permite gerar aulas e resumos usando Inteligência Artificial')

# Barra Lateral
st.sidebar.markdown("# Configurações de IA")
input_model = st.sidebar.selectbox(
    "Modelo de IA",
    (list_ia),
     index=list_ia.index(model_ia)
)
input_tokens = str(st.sidebar.number_input("Tokens", value=max_tokens))
input_temperature = str(st.sidebar.number_input("Temperatura", value=temperature))
save_config_btn = st.sidebar.button("Salvar", use_container_width=True)
reset_config_btn = st.sidebar.button("Redefinir", use_container_width=True)

if save_config_btn:
  model_ia = input_model
  max_tokens = input_tokens
  temperature = input_temperature
  st.sidebar.success("Configurações salvas com sucesso.")

if reset_config_btn:
  model_ia = "llama-3.1-70b-versatile"
  max_tokens = 1000
  temperature = 0.7
  st.sidebar.success("Configurações redefinidas com sucesso.")


with st.form("my_form"):
  # Input for YouTube Video ID
  video_URL = st.text_input('Digite a URL do vídeo do YouTube:', '')
  text_input = st.text_input('Escreva a sua pergunta:', '')

  submitted = st.form_submit_button("Enviar")

  video_id = ''

  if video_URL:
    video_id = video_URL.split("https://www.youtube.com/watch?v=")[1]

  if submitted and video_id and text_input:
      try:
          # Obtendo a transcrição do vídeo
          transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['pt-br', 'en'])
          full_transcript = " ".join([t['text'] for t in transcript_list])

          # Mostrando a transcrição do vídeo
          # st.subheader('Transcript:')
          # st.write(full_transcript)

          # Connect to the GROQ API
          client = Groq(
            api_key=os.environ.get("GROQ_API_KEY"),
          )

          chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f'{text_input}, responda em markdown e sempre transcreva a resposta para Português do Brasil: {full_transcript}',
                }
            ],
            model=model_ia,
            max_tokens=max_tokens,
            temperature=temperature
          )

          response = chat_completion.choices[0].message.content
          st.subheader('Resumo:')
          st.markdown(response)
      except Exception as e:
        st.error(f'Aconteceu um erro: {e}')