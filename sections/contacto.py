import streamlit as st
from backend.database import init_db, save_contact

def mostrar():
    init_db()
    st.header("Contacto")
    with st.form("contact_form"):
        name = st.text_input("Nombre")
        email = st.text_input("Email")
        message = st.text_area("Mensaje / ¿Qué te interesa?")
        submitted = st.form_submit_button("Enviar")
    if submitted:
        if not name or not email:
            st.warning("Completa nombre y email.")
        else:
            save_contact(name, email, message)
            st.success("¡Gracias! Tu mensaje ha sido guardado.")
