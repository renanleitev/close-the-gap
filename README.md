# Close The Gap

Plataforma de ensino com foco em gamificação.

## Introdução

Quando uma pessoa colaboradora precisa aprender um processo da empresa, é necessário que ela busque as instruções em 
documentos e também que peça ajuda a várias pessoas. Os documentos sobre os processos (fluxos, instruções, vídeos, etc) estão descentralizados e com formatos diferentes de acordo com cada área. 

Esse processo de encontrar e entender o material ideal, assim como acessar as pessoas adequadas pode ser longo. Em alguns casos, mesmo com o fluxo do processo mapeado, é possível que a pessoa colaboradora não o compreenda e acabe precisando de outras formas de ajuda.

## Solução

Nossa solução consiste em uma plataforma de ensino com foco em gamificação, de modo que gamificar o processo de centralização e padronização de documentos pode tornar a tarefa mais envolvente e motivadora para os colaboradores.

## Objetivos

1. **Sistema de Pontuação e Recompensas**: Atribua pontos para cada tarefa concluída, como a criação de um documento padronizado ou a centralização de arquivos. Os colaboradores podem trocar pontos por recompensas, como dias de folga ou vales-presente.
2. **Desafios e Missões**: Crie desafios semanais ou mensais, como “Centralize 10 documentos esta semana” ou “Padronize 5 fluxos de trabalho este mês”. Ofereça prêmios para quem completar as missões.
3. **Quadro de Líderes**: Mantenha um quadro de líderes visível para todos, destacando os colaboradores que mais contribuíram para a centralização e padronização dos documentos. Isso pode incentivar uma competição saudável.
4. **Badges e Conquistas**: Distribua badges ou conquistas digitais para marcos específicos, como “Primeiro Documento Padronizado” ou “100 Documentos Centralizados”. Esses reconhecimentos podem ser exibidos no perfil do 
colaborador em uma plataforma interna.
5. **Feedback e Reconhecimento**: Ofereça feedback positivo e reconhecimento público para os colaboradores que se destacam. Isso pode ser feito em reuniões de equipe ou através de comunicados internos.
6. **Treinamento Interativo**: Utilize plataformas de e-learning gamificadas para treinar os colaboradores sobre como centralizar e padronizar documentos. Inclua quizzes, vídeos interativos e simulações.
7. **Histórias e Narrativas**: Crie uma narrativa envolvente onde os colaboradores são “heróis” em uma missão para organizar e padronizar os documentos da empresa. Isso pode tornar o processo mais divertido e significativo.

## Pré-requisitos:

- Python: https://www.python.org/downloads/
- PiP: https://pip.pypa.io/en/stable/installation/
- Groq: https://console.groq.com/docs/quickstart

## Instalação

### Criar um arquivo .env na raiz do projeto e adicionar sua chave de API Groq (igual ao .env.example):

    GROQ_API_KEY=gsk_API_KEY

### Executar o comando abaixo no seu terminal:

    pip install -r requirements.txt

### Executar o aplicativo Streamlit no seu terminal:

     streamlit run app.py

### Copiar o endereço URL abaixo e abrir no navegador:

    http://localhost:8501/

## Ferramentas

- [Streamlit](https://streamlit.io/): Streamlit transforma scripts de dados em aplicativos web compartilháveis ​​em minutos. Tudo em Python puro. Não é necessária experiência de front-end.
- [Groq](https://groq.com/): Groq é uma inferência de IA rápida, alimentada pela tecnologia de inferência de IA LPU™ que oferece IA rápida, acessível e com eficiência energética.
- [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/): API python que permite obter transcrições/legendas de um determinado vídeo do YouTube. 

## Equipe

- Flávio Raposo
- João Pedro Marinho
- José Adeilton
- Renan Leite Vieira
- Rian Vinícius
- Robério José