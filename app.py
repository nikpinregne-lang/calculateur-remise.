import streamlit as st
import random
from datetime import datetime
import time

# 1. CONFIGURATION
st.set_page_config(page_title="Hacker Cosmic Global", page_icon="🤖", layout="wide")

# 2. SYSTÈME MULTILINGUE (Dictionnaire de traduction)
if 'lang' not in st.session_state:
    st.session_state.lang = "Français"

# 3. DESIGN NÉON & GALAXIE
st.markdown("""
    <style>
    .stApp { background: radial-gradient(ellipse at bottom, #1B2735 0%, #090A0F 100%); color: white; }
    h1 { color: #FF00FF !important; text-shadow: 0 0 15px #FF00FF; text-align: center; }
    h2, h3, label, p, span { color: #00FFFF !important; text-shadow: 0 0 8px #00FFFF; }
    [data-testid="stSidebar"] { background-color: rgba(10, 10, 30, 0.9); border-right: 3px solid #00FFFF; }
    </style>
    """, unsafe_allow_html=True)

# 4. MENU SIDEBAR
with st.sidebar:
    st.markdown('<p style="color:#FF00FF; font-weight:bold; border:2px solid #FF00FF; padding:10px; border-radius:15px; text-align:center;">👑 CRÉATEUR : RÈGNE</p>', unsafe_allow_html=True)
    
    # SÉLECTEUR DE LANGUE
    st.session_state.lang = st.selectbox("🌐 Language / Langue", ["Français", "English", "Español"])
    
    st.title("🛰️ Navigation")
    
    # Traductions du menu
    menu_titles = {
        "Français": ["💰 Calculateur", "🤖 Cosmic Chatbot", "⚔️ Duel Multi", "📐 Zone Maths", "🟢 Matrix"],
        "English": ["💰 Calculator", "🤖 Cosmic Chatbot", "⚔️ Multi Duel", "📐 Math Zone", "🟢 Matrix"],
        "Español": ["💰 Calculadora", "🤖 Cosmic Chatbot", "⚔️ Duelo Multi", "📐 Zona mates", "🟢 Matrix"]
    }
    
    menu = st.radio("Menu :", menu_titles[st.session_state.lang])
    st.write("---")
    st.caption(f"🚀 Hacker Cosmic v14.0 | {st.session_state.lang}")

# 5. EN-TÊTE
col1, col2 = st.columns(2)
with col1: st.image("IMG_0956.png", width=200)
with col2:
    welcome_text = {
        "Français": "COSMIC 1CA",
        "English": "COSMIC GLOBAL",
        "Español": "COSMIC MUNDIAL"
    }
    st.title(welcome_text[st.session_state.lang])
    
    # IA Vocale adaptable
    vocal_msg = {
        "Français": "Bienvenue sur le réseau mondial, Maître Règne.",
        "English": "Welcome to the global network, Master Règne.",
        "Español": "Bienvenido a la red mundial, Maestro Règne."
    }
    vocal_lang = {"Français": "fr-FR", "English": "en-US", "Español": "es-ES"}
    
    st.components.v1.html(f"""
        <script>function parler(){{var m=new SpeechSynthesisUtterance("{vocal_msg[st.session_state.lang]}");m.lang='{vocal_lang[st.session_state.lang]}';window.speechSynthesis.speak(m);}}</script>
        <button onclick="parler()" style="background-color:transparent; color:#FF00FF; border:2px solid #FF00FF; padding:10px; border-radius:15px; cursor:pointer; font-weight:bold; width: 100%;">🔈 INITIALISER L'IA</button>
    """, height=70)

# 6. LOGIQUE DES PAGES

# --- PAGE CHATBOT ---
if "Chatbot" in menu:
    st.header("🤖 Cosmic Chatbot (IA)")
    st.write("Pose une question au système...")
    user_q = st.text_input("Message :", placeholder="ex: Qui es-tu ?")
    
    if st.button("Envoyer 🚀"):
        responses = {
            "Qui es-tu ?": "Je suis l'IA de Hacker Cosmic, créée par le Maître Règne.",
            "Who are you?": "I am the Hacker Cosmic AI, created by Master Règne.",
            "Quel est ton but ?": "Aider les élèves de 1CA à dominer le monde des maths et du code.",
            "Salut": "Salut Hacker ! Système prêt pour l'action.",
            "Hello": "Hello Hacker! System ready for action."
        }
        # Réponse par défaut si la question n'est pas connue
        default_res = "Analyse en cours... Ma base de données est encore en apprentissage !"
        res = responses.get(user_q, default_res)
        
        with st.chat_message("assistant"):
            st.write(res)

# --- PAGE CALCULATEUR ---
elif "Calcul" in menu:
    st.header("💰 Calculateur de Soldes")
    pi = st.number_input("Prix (€)", value=100.0)
    re = st.slider("Réduction (%)", 0, 100, 20)
    st.metric("Prix Final", f"{pi * (1 - re/100)} €")

# --- PAGE DUEL ---
elif "Duel" in menu:
    st.header("⚔️ Duel : Hacker vs Hacker")
    if 'sec' not in st.session_state: st.session_state.sec = random.randint(1, 10)
    guess = st.number_input("Devine le chiffre (1-10) :", 1, 10)
    if st.button("Vérifier"):
        if guess == st.session_state.sec:
            st.balloons(); st.success("GAGNÉ ! Nouveau code généré."); st.session_state.sec = random.randint(1, 10)
        else: st.error("FAUX ! Le système résiste.")

# --- PAGE MATHS ---
elif "Math" in menu:
    st.header("📐 Zone Mathématiques")
    st.write("Assistant de calcul 1CA activé.")
    st.number_input("Valeur A", value=1.0)

# --- PAGE MATRIX ---
elif "Matrix" in menu:
    st.header("🟢 Matrix Mode")
    if st.button("START"):
        st.code("\n".join(["".join([random.choice("01") for _ in range(40)]) for _ in range(5)]))
