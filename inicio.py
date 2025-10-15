import streamlit as st

with open("style.css") as f:
    st.markdown(f"<style> {f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(layout="wide", page_title="Página inicial")

st.title("Começando com o SmartNotes")

html_code2 = """
<h4 style=font-family: DejaVu Sans Mon;">Bem vindo ao SmartNotes! </h4>
"""
st.markdown(html_code2, unsafe_allow_html=True)

html_code3 = """
<ul>
  <li>Clique na aba 'Nova anotação' para criar uma anotação </li>
  <li>Escolha um título, categoria e conteúdo para sua anotação e ao final clique no botão 'Salvar'</li>
  <li>Clique na aba 'Busca por anotações' para encontrar suas anotações</li>
  <li>Na aba 'Busca por anotações' é possível editar e excluir anotações </li>
</ul>
"""
st.markdown(html_code3, unsafe_allow_html=True)








        

    




