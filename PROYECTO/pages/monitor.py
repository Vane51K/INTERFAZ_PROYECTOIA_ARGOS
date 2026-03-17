import streamlit as st
import cv2
import time

def run():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.title("📹 Centro de Monitoreo")

    if "camara_activa" not in st.session_state:
        st.session_state.camara_activa = False

    col1, col2 = st.columns([1,2])

    with col1:
        st.subheader("⚙️ Control")

        if st.button("▶️ Encender cámara"):
            st.session_state.camara_activa = True

        if st.button("⏹️ Apagar cámara"):
            st.session_state.camara_activa = False

        estado = "🟢 Activa" if st.session_state.camara_activa else "🔴 Apagada"
        st.write(f"Estado: {estado}")

    with col2:
        st.subheader("🎥 Vista en Vivo")
        frame_placeholder = st.empty()

        if st.session_state.camara_activa:
            cap = cv2.VideoCapture(0)

            if not cap.isOpened():
                st.error("No se pudo acceder a la cámara")
            else:
                while st.session_state.camara_activa:
                    ret, frame = cap.read()

                    if not ret:
                        st.error("Error al capturar frame")
                        break

                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame_placeholder.image(frame, use_container_width=True)

                    time.sleep(0.03)  # controla velocidad (30 FPS aprox)

            cap.release()
        else:
            st.info("Cámara apagada")

    st.markdown('</div>', unsafe_allow_html=True)