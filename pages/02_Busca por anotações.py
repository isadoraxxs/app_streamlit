import streamlit as st
from google.cloud import firestore

with open("style.css") as f:
    st.markdown(f"<style> {f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(layout="wide", page_title="Anotações")


baseDados = firestore.Client.from_service_account_json("firebase.json")


def ordenacao_notas(nome_colecao):
    notas = (baseDados.collection(nome_colecao).stream())
    
    lista_notas = []
    for nota in notas:
        nota_data = nota.to_dict()
        nota_data["id"] = nota.id
        lista_notas.append(nota_data)
    notas_ordenadas = sorted(lista_notas,key=lambda n: n.get("data_criacao"), reverse=True)
    return notas_ordenadas

notas_ordenadas = ordenacao_notas("notas")

st.markdown("<h1 id='busca-por-anotacoes'>Busca por anotações</h1>", unsafe_allow_html=True)

opcao = st.selectbox("Selecione uma nota:", [nota["titulo"] for nota in notas_ordenadas],
)


for nota in notas_ordenadas:
    if nota["titulo"] == opcao:
        st.write("---")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown(f"<p style='font-size:13px;'><b>Título:</b> {nota.get('titulo', ':')}</p>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<p style='font-size:13px;'><b>Categoria:</b> {nota.get('categoria', ':')}</p>", unsafe_allow_html=True)
        with col3:
            data_c = nota.get("data_criacao") 
            data_c_formatada = data_c.strftime("%d/%m/%Y %H:%M")
            st.markdown(f"<p style='font-size:13px;'><b>Data criação:</b> {data_c_formatada}</p>", unsafe_allow_html=True)
        with col4:
            data_m = nota.get("data_modificacao") 
            if data_m: data_m_formatada = data_m.strftime("%d/%m/%Y %H:%M")
            else: data_m_formatada = "—"
            st.markdown(f"<p style='font-size:13px;'><b>Data modificação:</b> {data_m_formatada}</p>", unsafe_allow_html=True)
        conteudo = st.text_input("", value=nota["conteudo"])
        st.write("---")
        col5, col6  = st.columns(2)
        with col5:
            if st.button("Salvar modificações"):
                baseDados.collection("notas").document(nota["id"]).update({"conteudo": conteudo})
                baseDados.collection("notas").document(nota["id"]).update({"data_modificacao": firestore.SERVER_TIMESTAMP})
                st.success(f"Conteúdo atualizado!")
                st.rerun()
        with col6:
            if st.button("Excluir"):
                baseDados.collection("notas").document(nota["id"]).delete()
                st.warning("Nota excluída!")
                st.rerun()
            break
        

