import streamlit as st

# =========================
# CONFIGURACIÓN GENERAL
# =========================
st.set_page_config(
    page_title="ARGOS | Sistema de Monitoreo",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# ESTILOS PERSONALIZADOS
# =========================
def aplicar_estilos():
    st.markdown("""
    <style>
    /* ======== GENERAL ======== */
    .stApp {
        background-color: #091413;
        color: #B0E4CC;
        font-family: 'Inter', sans-serif;
    }

    /* ======== SIDEBAR ======== */
    section[data-testid="stSidebar"] {
        background-color: #0E1E1B;
        border-right: 1px solid #285A48;
        padding-top: 2rem;
    }

    section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] h2, 
    section[data-testid="stSidebar"] h3 {
        color: #B0E4CC;
    }

    div[data-testid="stSidebarNav"] p, 
    div[data-testid="stSidebarNav"] span {
        color: #B0E4CC !important;
    }

    /* ======== TITULOS ======== */
    h1, h2, h3 {
        color: #B0E4CC;
        font-weight: 600;
    }

    /* ======== TARJETAS ======== */
    .card {
        background-color: #132822;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 0 10px rgba(64, 138, 113, 0.2);
        margin-bottom: 20px;
    }

    /* ======== BOTONES ======== */
    div.stButton > button {
        background-color: #285A48;
        color: #B0E4CC;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.2rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }

    div.stButton > button:hover {
        background-color: #408A71;
        color: #091413;
        transform: scale(1.03);
    }

    /* ======== RADIO BUTTONS ======== */
    div[role="radiogroup"] > label {
        background-color: #132822;
        color: #B0E4CC;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        margin-bottom: 0.5rem;
        display: block;
        transition: all 0.3s ease;
    }

    div[role="radiogroup"] > label:hover {
        background-color: #285A48;
        cursor: pointer;
    }

    /* ======== FOOTER ======== */
    footer {
        visibility: hidden;
    }
    </style>
    """, unsafe_allow_html=True)

# =========================
# APLICAR ESTILOS
# =========================
aplicar_estilos()

# =========================
# INTERFAZ PRINCIPAL
# =========================
st.sidebar.image("assets/logo_argos.png", use_container_width=True)
st.sidebar.title("📡 ARGOS")
st.sidebar.markdown("---")

opcion = st.sidebar.radio(
    "Navegación",
    ["🏠 Inicio", "📝 Registro", "🎥 Monitoreo", "📊 Dashboard"]
)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.title("🛰️ ARGOS - Sistema de Monitoreo Inteligente")
st.markdown("### Control y supervisión avanzada en tiempo real")
st.markdown("---")

# =========================
# CONTENIDO SEGÚN OPCIÓN
# =========================
if opcion == "🏠 Inicio":
    st.markdown("""
    <div style="text-align: center; padding: 2rem;">
        <h2>Bienvenido al sistema <span style="color:#408A71;">ARGOS</span></h2>
        <p style="font-size:1.1rem; color:#B0E4CC;">
        Supervisa, analiza y gestiona tus cámaras de seguridad con tecnología avanzada de detección.
        </p>
        <img src="https://cdn-icons-png.flaticon.com/512/1040/1040230.png" width="120">
    </div>
    """, unsafe_allow_html=True)

elif opcion == "📝 Registro":
    import pages.registro as registro
    registro.run()

elif opcion == "🎥 Monitoreo":
    import pages.monitor as monitor
    monitor.run()

elif opcion == "📊 Dashboard":
    import pages.dashboard as dashboard
    dashboard.run()

st.markdown('</div>', unsafe_allow_html=True)