import streamlit as st

st.set_page_config(
    page_title="Instagram AI Manager",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Instagram AI Manager")
st.subheader("@its.roxanarolon")
st.info(
    "Fase 1: base local del analizador. Carga un CSV de Instagram para comenzar."
)

uploaded_file = st.file_uploader(
    "Carga tu exportación CSV de Instagram",
    type=["csv"],
)

if uploaded_file:
    st.success(f"Archivo recibido: {uploaded_file.name}")
    st.write("El motor analítico se incorporará en el siguiente módulo.")
else:
    st.caption("Todavía no se ha cargado ningún dataset.")
