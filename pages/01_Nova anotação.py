import streamlit as st
from google.cloud import firestore
import json

with open("style.css") as f:
    st.markdown(f"<style> {f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(layout="wide", page_title="Nova anotação")


baseDados = firestore.Client.from_service_account_json("firebase.json")


st.markdown("<h1 id='crie-uma-nova-anotacao'>Crie uma nova anotação</h1>", unsafe_allow_html=True)



titulo = st.text_input("Título")
categoria = st.text_input("Categoria")
conteudo = st.text_area("Conteúdo")

if st.button("Salvar"):
    baseDados.collection("notas").add({
        "titulo": titulo,
        "conteudo": conteudo,
        "categoria": categoria,
        "data_criacao": firestore.SERVER_TIMESTAMP
    })
    st.success("Nota salva com sucesso!")


