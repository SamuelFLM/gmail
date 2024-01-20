import streamlit as st
from utilidades  import *

def pag_lista_emails():
    st.markdown("# Lista emails".title())
    st.divider()

    for arquivo in PASTA_LISTA_EMAILS.glob("*.txt"):
        nome_arquivo = arquivo.stem.replace("_", " ").upper()
        col1, col2, col3 = st.columns([0.6, 0.2, 0.2])
        col1.button(
            nome_arquivo,
            key=f"{nome_arquivo}",
            use_container_width=True,
            on_click=_usar_lista,
            args=(nome_arquivo,),
        )
        col2.button(
            "Editar",
            key=f"editar_{nome_arquivo}",
            use_container_width=True,
            on_click=_edita_lista,
            args=(nome_arquivo,),
        )
        col3.button(
            "Excluir",
            key=f"excluir_{nome_arquivo}",
            use_container_width=True,
            on_click=_remove_lista,
            args=(nome_arquivo,),
        )
    st.divider()
    st.button("Adicionar Lista", on_click=mudar_pagina, args=("adicionar_nova_lista",))


def _usar_lista(nome):
    nome_arquivo = nome.replace(" ", "_").lower() + ".txt"
    with open(PASTA_LISTA_EMAILS / nome_arquivo) as f:
        texto_arquivo = f.read()
    st.session_state.destinatarios_atual = texto_arquivo
    mudar_pagina("home")


def _edita_lista(nome):
    nome_arquivo_lista = nome.replace(" ", "_").lower() + ".txt"
    with open(PASTA_LISTA_EMAILS / nome_arquivo_lista) as f:
        texto_lista = f.read()
    st.session_state.nome_arquivo_lista = nome
    st.session_state.texto_lista = texto_lista
    mudar_pagina("editar_lista")


def _remove_lista(nome):
    nome_arquivo = nome.replace(" ", "_").lower() + ".txt"
    (PASTA_LISTA_EMAILS / nome_arquivo).unlink()


def pag_adicionar_nova_lista(nome_lista="", emails_lista=""):
    nome_lista = st.text_input("Nome do template: ", value=nome_lista)
    emails_lista = st.text_area(
        "Escreva os emails separados por virgula: ", value=emails_lista, height=600
    )
    st.button("Salvar", on_click=_salvar_lista, args=(nome_lista, emails_lista))


def _salvar_lista(nome, texto):
    PASTA_LISTA_EMAILS.mkdir(exist_ok=True)
    nome_arquivo = nome.replace(" ", "_").lower() + ".txt"
    with open(PASTA_LISTA_EMAILS / nome_arquivo, "w") as f:
        f.write(texto)
    mudar_pagina("lista_emails")
