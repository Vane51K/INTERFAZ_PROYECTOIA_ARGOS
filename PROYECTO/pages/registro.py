import streamlit as st
import pickle
import os
from datetime import datetime

st.title("➕ Registro de Usuarios")

DB_FILE = "argos_database.pkl"

def load_db():
    return pickle.load(open(DB_FILE, 'rb')) if os.path.exists(DB_FILE) else {}

def save_db(db):
    pickle.dump(db, open(DB_FILE, 'wb'))

nombre = st.text_input("Nombre")
id_user = st.text_input("ID")

if st.button("Guardar"):
    if nombre and id_user:
        db = load_db()
        db[id_user] = {
            "nombre": nombre,
            "fecha": datetime.now().isoformat()
        }
        save_db(db)
        st.success("Usuario registrado")
    else:
        st.error("Completa los datos")

# Mostrar usuarios
db = load_db()
st.write("Usuarios registrados:", db)