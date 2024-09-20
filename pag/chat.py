import time
import streamlit as st
from utils import cria_chain_conversa

def sidebar():
    label_botao = 'Inicializar ChatBot'
    if 'chain' in st.session_state:
        label_botao = 'Atualizar ChatBot'
    if st.button(label_botao, use_container_width=True):
        st.success('Inicializando o ChatBot...')
        cria_chain_conversa()
        st.rerun()

def chat_window():
    st.header('🤖 Bem-vindo ao Chat', divider=True)

    if not 'chain' in st.session_state:
        st.error('O chatbot não foi inicializado corretamente!')
        st.stop()
    
    chain = st.session_state['chain']
    memory = chain.memory

    mensagens = memory.load_memory_variables({})['chat_history']

    container = st.container()
    for mensagem in mensagens:
        chat = container.chat_message(mensagem.type)
        chat.markdown(mensagem.content)

    nova_mensagem = st.chat_input('Converse com seus documentos...')
    if nova_mensagem:
        chat = container.chat_message('human')
        chat.markdown(nova_mensagem)
        chat = container.chat_message('ai')
        chat.markdown('Gerando resposta')

        resposta = chain.invoke({'question': nova_mensagem})
        st.session_state['ultima_resposta'] = resposta
        st.rerun()

def main():
    with st.sidebar:
        sidebar()
    chat_window()

if __name__ == '__main__':
    main()
