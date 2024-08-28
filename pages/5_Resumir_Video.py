import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import os
from utils import call_ai

# Configurando a página
st.set_page_config(
    page_title="Resumir Video",
)

# Streamlit webpage layout
st.title('Resumir Video')
st.write('Utilize vídeos do Youtube para gerar aulas e resumos usando Inteligência Artificial')
st.write('ATENÇÃO: Funcionalidade indisponível na versão online. Para rodar o projeto localmente, visite: https://github.com/renanleitev/close-the-gap')

input_model, input_tokens, input_temperature = call_ai.sidebar()

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

          response_ai = call_ai.run(input_model, 
                                input_tokens, 
                                input_temperature, 
                                text_input, 
                                full_transcript,
                                'responda em markdown e sempre transcreva a resposta para Português do Brasil')

          response_stream = st.write_stream(call_ai.response_generator(response_ai))
      except Exception as e:
        st.error(f'Aconteceu um erro: {e}')