import streamlit as st
from utils import call_ai

# Configurando a página
st.set_page_config(
    page_title="Close The Gap",
)

# Streamlit webpage layout
st.title('Close The Gap')
st.write('Plataforma de ensino que permite gerar aulas e resumos usando Inteligência Artificial')

input_model, input_tokens, input_temperature = call_ai.sidebar()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Mensagem"):
    try:
      # Display user message in chat message container
      st.chat_message("user", avatar="🤓").markdown(prompt)
      # Add user message to chat history
      st.session_state.messages.append({"role": "user", "content": prompt})

      # Display assistant response in chat message container
      with st.chat_message("assistant", avatar="🤖"):
        with st.spinner('Carregando...'):
            response_ai = call_ai.run(input_model, input_tokens, input_temperature, prompt)
            response_stream = st.write_stream(call_ai.response_generator(response_ai))
      # Add assistant response to chat history
      st.session_state.messages.append({"role": "assistant", "content": response_ai})
    except Exception as e:
      st.error(f'Aconteceu um erro: {e}')