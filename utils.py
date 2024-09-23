from pathlib import Path

import streamlit as st
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_community.vectorstores.faiss import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_openai.chat_models import ChatOpenAI
from pydantic import BaseModel
from configs import *
# Carregar diretamente da variável de ambiente
import os
import dotenv
from dotenv import load_dotenv, find_dotenv


_ = load_dotenv(find_dotenv())


def carrega_vector_store():

    embedding_model = OpenAIEmbeddings()

    # Carregar o FAISS index salvo no diretório
    vector_store = FAISS.load_local("Algorithmic_Trading", embedding_model, allow_dangerous_deserialization=True)

    return vector_store


def cria_chain_conversa():
    vector_store = carrega_vector_store()

    # Passar diretamente a chave da API como variável de ambiente
    chat = ChatOpenAI(model=get_config('model_name'))

    memory = ConversationBufferMemory(
        return_messages=True,
        memory_key='chat_history',
        output_key='answer'
    )
    
    retriever = vector_store.as_retriever(
        search_type=get_config('retrieval_search_type'),
        search_kwargs=get_config('retrieval_kwargs')
    )
    
    prompt = PromptTemplate.from_template(get_config('prompt'))
    
    chat_chain = ConversationalRetrievalChain.from_llm(
        llm=chat,
        memory=memory,
        retriever=retriever,
        return_source_documents=True,
        verbose=True,
        combine_docs_chain_kwargs={'prompt': prompt}
    )

    st.session_state['chain'] = chat_chain