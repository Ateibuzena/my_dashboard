import streamlit as st
import importlib
from sections import portada, habilidades, experiencia, santander, contacto

SECTIONS = {
    "Portada": portada,
    "Habilidades": habilidades,
    "Experiencia": experiencia,
    "Santander": santander,
    "Contacto": contacto
}

def main():
    st.set_page_config(page_title="Dashboard - Ana Zubieta", layout="wide")
    st.sidebar.title("Navegación")
    choice = st.sidebar.radio("Ir a", list(SECTIONS.keys()))
    module = SECTIONS[choice]
    importlib.reload(module)
    module.mostrar() #

if __name__ == "__main__":
    main()
