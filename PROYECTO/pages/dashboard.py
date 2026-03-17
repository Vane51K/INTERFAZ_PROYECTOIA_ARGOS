import streamlit as st

st.title("📊 Dashboard")

st.info("Aquí irán estadísticas del sistema")

col1, col2, col3 = st.columns(3)

col1.metric("Rostros detectados", "147")
col2.metric("Coincidencias", "142")
col3.metric("Alertas", "5")