import streamlit as st
from utils.api import upload_pdfs_api


def render_uploader():
    st.sidebar.header("Carregar documentos médicos (.PDFs)")
    uploaded_files = st.sidebar.file_uploader("Carregar arquivos", type="pdf",accept_multiple_files=True)
    if st.sidebar.button("Upload DB") and uploaded_files:
        response = upload_pdfs_api(uploaded_files)
        if response.status_code==200:
            st.sidebar.success("Carregado com sucesso")
        else:
            st.sidebar.error(f"Error:{response.text}")