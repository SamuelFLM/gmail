import streamlit as st
from utilidades import *
from pagina_template import *
from pagina_lista_emails import *
from pagina_configuracoes import *


def home():
    st.markdown("# Central de emails".title())

    destinatarios = st.text_input(
        "Destinatarios do email: ", value=st.session_state.destinatarios_atual
    )
    titulo = st.text_input("Titulo do email: ", value=st.session_state.titulo_atual)
    corpo_email = st.text_area(
        "Digite o email: ", height=400, value=st.session_state.corpo_atual
    )

    col1, col2, col3 = st.columns(3)
    st.session_state.destinatarios_atual = destinatarios
    st.session_state.titulo_atual = titulo
    st.session_state.corpo_atual = corpo_email

    enviar = col1.button(
        "Enviar",
        use_container_width=True,
        on_click=_enviar_email,
        args=(destinatarios, titulo, corpo_email),
    )

    limpar = col3.button("Limpar", use_container_width=True, on_click=_limpar_home)


def _enviar_email(destinatarios, titulo, corpo):
    destinatarios = destinatarios.replace(" ", "").split(",")
    email_usuario = ler_email_usuario()
    chave_usuario = ler_chave_usuario()

    if email_usuario == "":
        st.error("Adicione email na pagina de configuracoes")

    elif chave_usuario == "":
        st.error("Adicione chave na pagina de configuracoes")
    else:
        enviar_email(
            email_usuario,
            destinatarios=destinatarios,
            titulo=titulo,
            corpo=corpo,
            senha_app=chave_usuario,
        )


def _limpar_home():
    st.session_state.destinatarios_atual = ""
    st.session_state.titulo_atual = ""
    st.session_state.corpo_atual = ""


def main():
    inicializacao()

    st.sidebar.button(
        "Central de emails".title(),
        use_container_width=True,
        on_click=mudar_pagina,
        args=("home",),
    )
    st.sidebar.button(
        "Templates".title(),
        use_container_width=True,
        on_click=mudar_pagina,
        args=("templates",),
    )
    st.sidebar.button(
        "Lista de emails".title(),
        use_container_width=True,
        on_click=mudar_pagina,
        args=("lista_emails",),
    )
    st.sidebar.button(
        "Configuração".title(),
        use_container_width=True,
        on_click=mudar_pagina,
        args=("configuracao",),
    )

    if st.session_state.pagina_central_email == "home":
        home()

    elif st.session_state.pagina_central_email == "templates":
        pag_templates()

    elif st.session_state.pagina_central_email == "adicionar_novo_template":
        pag_adicionar_novo_template()

    elif st.session_state.pagina_central_email == "editar_template":
        nome_template_editar = st.session_state.nome_template_editar
        texto_template_editar = st.session_state.texto_template_editar
        pag_adicionar_novo_template(nome_template_editar, texto_template_editar)

    elif st.session_state.pagina_central_email == "lista_emails":
        pag_lista_emails()

    elif st.session_state.pagina_central_email == "adicionar_nova_lista":
        pag_adicionar_nova_lista()

    elif st.session_state.pagina_central_email == "editar_lista":
        nome_lista = st.session_state.nome_arquivo_lista
        texto_lista = st.session_state.texto_lista
        pag_adicionar_nova_lista(nome_lista, texto_lista)

    elif st.session_state.pagina_central_email == "configuracao":
        pag_configuracao()

if __name__ == "__main__":
    main()
