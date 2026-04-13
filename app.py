import streamlit as st
import random
from datetime import datetime

# 1. CONFIGURATION
st.set_page_config(page_title="Hacker Cosmic Global", page_icon="🌍", layout="wide")

# 2. DESIGN NÉON
st.markdown("""
    <style>
    .stApp { background: radial-gradient(ellipse at bottom, #1B2735 0%, #050505 100%); color: white; }
    h1 { color: #FF00FF !important; text-shadow: 0 0 20px #FF00FF; text-align: center; }
    h2, h3, label, p, span { color: #00FFFF !important; text-shadow: 0 0 10px #00FFFF; }
    [data-testid="stSidebar"] { background-color: #000000 !important; border-right: 2px solid #39FF14; }
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR AVEC MULTILANGUE
with st.sidebar:
    st.markdown('<p style="color:#39FF14; font-weight:bold; border:1px solid #39FF14; padding:10px; border-radius:15px; text-align:center;">🟢 SYSTÈME : ONLINE</p>', unsafe_allow_html=True)
    
    # LE RETOUR DU MULTILANGUE
    langue = st.selectbox("🌐 Langue / Language", ["Français", "English", "Español"])
    
    st.write("---")
    
    # Traduction du Menu
    m_txt = {
        "Français": ["🤖 IA Intelligente", "💰 Calculateur Pro", "📐 Zone Scolaire", "🎮 Mission Solo"],
        "English": ["🤖 Smart AI", "💰 Pro Calculator", "📐 School Zone", "🎮 Solo Mission"],
        "Español": ["🤖 IA Inteligente", "💰 Calculadora Pro", "📐 Zona Escolar", "🎮 Misión Solo"]
    }
    menu = st.radio("Navigation :", m_txt[langue])
    st.write("---")
    st.caption(f"🚀 Créé par RÈGNE | {langue}")

# 4. EN-TÊTE
col1, col2 = st.columns(2)
with col1: st.image("IMG_0956.png", width=200)
with col2:
    titre_app = {"Français": "HACKER COSMIC 1CA", "English": "COSMIC HACKER 1CA", "Español": "HACKER CÓSMICO 1CA"}
    st.title(f"{titre_app[langue]} 2026")
    
    # Voix adaptable
    vocal = {
        "Français": f"Système en français activé. Bonjour Maître Règne.",
        "English": f"English system activated. Hello Master Règne.",
        "Español": f"Sistema en español activado. Hola Maestro Règne."
    }
    v_lang = {"Français": "fr-FR", "English": "en-US", "Español": "es-ES"}
    
    st.components.v1.html(f"""
        <script>function parler(){{var m=new SpeechSynthesisUtterance("{vocal[langue]}");m.lang='{v_lang[langue]}';window.speechSynthesis.speak(m);}}</script>
        <button onclick="parler()" style="background-color:transparent; color:#FF00FF; border:2px solid #FF00FF; padding:10px; border-radius:15px; cursor:pointer; font-weight:bold; width:100%;">🔈 INITIALISER L'IA</button>
    """, height=70)

# 5. LOGIQUE DES PAGES
if "IA" in menu or "Smart" in menu:
    st.header(f"🤖 {menu}")
    prompt = {"Français": "Pose une question...", "English": "Ask a question...", "Español": "Haz una pregunta..."}
    user_q = st.text_input(prompt[langue]).lower()
    
    if st.button("OK"):
        if "salut" in user_q or "hello" in user_q or "hola" in user_q:
            resp = {"Français": "Salut Hacker ! ⚡", "English": "Hello Hacker! ⚡", "Español": "¡Hola Hacker! ⚡"}
            st.chat_message("assistant").write(resp[langue])
        else:
            st.chat_message("assistant").write("🔍 ...")

elif "Calcul" in menu:
    st.header("💰 Calculateur")
    pi = st.number_input("Prix / Price (€)", value=100.0)
    re = st.slider("Réduction / Discount (%)", 0, 100, 20)
    st.metric("Total", f"{pi*(1-re/100)} €")

elif "Zone" in menu:
    st.header("📐 Zone Scolaire / School")
    st.success("Outil prêt !")

elif "Mission" in menu or "Misión" in menu:
    st.header("🎮 Mission Solo")
    st.code('print("Hello")')
