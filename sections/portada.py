import streamlit as st

def mostrar():
    st.title("👋 Hola, soy Ana Zubieta")
    st.subheader("📊 Analista de Datos | 🧠 Programador | 🚀 En busca de un futuro en Banco Santander")
    st.write("""
    Soy una profesional apasionada por los datos y la tecnología.
    Este dashboard interactivo muestra mis habilidades, proyectos y una propuesta específica para Banco Santander.
    """)
    st.markdown("---")
    col1, col2 = st.columns([1,3])
    with col1:
        st.image("https://via.placeholder.com/180", width=160)  # reemplaza con tu foto
    with col2:
        st.write("📍 Málaga · 🇪🇸")
        st.write("[GitHub](https://github.com/Ateibuzena) • [LinkedIn](https://www.linkedin.com/in/tu-perfil)")
