import streamlit as st
import random
from datetime import datetime

# 1. CONFIGURATION
st.set_page_config(page_title="Hacker Cosmic Total", page_icon="🌍", layout="wide")

# 2. DESIGN NÉON GLOBAL
st.markdown("""
    <style>
    .stApp { background: radial-gradient(ellipse at bottom, #1B2735 0%, #050505 100%); color: white; }
    h1 { color: #FF00FF !important; text-shadow: 0 0 20px #FF00FF; text-align: center; font-family: 'Orbitron', sans-serif; }
    h2, h3, label, p, span { color: #00FFFF !important; text-shadow: 0 0 10px #00FFFF; }
    .stMetric div { color: #39FF14 !important; }
    [data-testid="stSidebar"] { background-color: #000000 !important; border-right: 2px solid #39FF14; }
    img { border-radius: 50%; border: 3px solid #00FFFF; box-shadow: 0 0 20px #00FFFF; }
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR AVEC TOUTES LES OPTIONS
with st.sidebar:
    st.markdown('<p style="color:#39FF14; font-weight:bold; border:1px solid #39FF14; padding:10px; border-radius:15px; text-align:center;">🟢 SYSTÈME : ONLINE</p>', unsafe_allow_html=True)
    langue = st.selectbox("🌐 Langue / Language", ["Français", "English", "Español"])
    st.write("---")
    
    m_txt = {
        "Français": ["🤖 IA & Chatbot", "💰 Calculateur Pro", "📐 Zone Maths", "📚 Encyclopédie", "🎮 Missions Code", "⚔️ Duel Multi", "🪐 Espace"],
        "English": ["🤖 IA & Chatbot", "💰 Pro Calculator", "📐 Math Zone", "📚 Encyclopedia", "🎮 Code Missions", "⚔️ Multi Duel", "🪐 Space"],
        "Español": ["🤖 IA & Chatbot", "💰 Calculadora Pro", "📐 Zona Mates", "📚 Enciclopedia", "🎮 Misiones Code", "⚔️ Duelo Multi", "🪐 Espacio"]
    }
    menu = st.radio("Navigation :", m_txt[langue])
    st.write("---")
    st.caption(f"🚀 Créé par RÈGNE | 1CA 2026")

# 4. EN-TÊTE
col1, col2 = st.columns(2)
with col1: st.image("IMG_0956.png", width=200)
with col2:
    st.title("HACKER COSMIC 1CA 2026")
    vocal = {"Français": "Système prêt. Bonjour Maître.", "English": "System ready. Hello Master.", "Español": "Sistema listo. Hola Maestro."}
    v_lang = {"Français": "fr-FR", "English": "en-US", "Español": "es-ES"}
    st.components.v1.html(f"""
        <script>function parler(){{var m=new SpeechSynthesisUtterance("{vocal[langue]}");m.lang='{v_lang[langue]}';window.speechSynthesis.speak(m);}}</script>
        <button onclick="parler()" style="background-color:transparent; color:#FF00FF; border:2px solid #FF00FF; padding:10px; border-radius:15px; cursor:pointer; font-weight:bold; width:100%;">🔈 INITIALISER L'IA</button>
    """, height=70)

# 5. LOGIQUE DES PAGES (TOUT EST ICI)

if "IA" in menu:
    st.header(f"🤖 IA Chatbot ({langue})")
    q = st.text_input("Pose ta question :").lower()
    if st.button("OK"):
        if "salut" in q or "hello" in q: st.chat_message("assistant").write("Salut Hacker ! ⚡")
        elif "qui" in q: st.chat_message("assistant").write("Je suis l'IA de Maître Règne. 👑")
        else: st.chat_message("assistant").write("Analyse en cours...")

elif "Calcul" in menu:
    st.header("💰 Calculateur de Soldes")
    pi = st.number_input("Prix (€)", value=100.0)
    re = st.slider("Réduction (%)", 0, 100, 20)
    st.metric("Prix Final", f"{pi*(1-re/100)} €", delta=f"-{(pi*re)/100} €")

elif "Math" in menu or "Mates" in menu:
    st.header("📐 Zone Mathématiques")
    st.write("### Produit en Croix")
    ma, mb, mc = st.columns(3)
    res = (mb.number_input("B", value=10.0) * mc.number_input("C", value=5.0)) / ma.number_input("A", value=1.0)
    st.success(f"Résultat : {res}")

elif "Ency" in menu:
    st.header("📚 Encyclopédie du Code")
    st.write("Le codage est le langage du futur. Variables, Conditions et Boucles sont les bases.")

elif "Mission" in menu:
    st.header("🎮 Mission Codeur")
    st.code('print("Hello 1CA")')
    if st.text_input("Répare le code :") == 'print("Hello 1CA")': st.balloons()

elif "Duel" in menu:
    st.header("⚔️ Duel Multijoueur")
    if 's' not in st.session_state: st.session_state.s = random.randint(1, 10)
    g = st.number_input("Devine (1-10) :", 1, 10)
    if st.button("Vérifier"):
        if g == st.session_state.s: st.balloons(); st.session_state.s = random.randint(1, 10)

elif "Espace" in menu or "Space" in menu:
    st.header("🪐 Gravité Spatiale")
    p = st.number_input("Poids (kg)", value=50.0)
    st.write(f"Sur Mars : {p*0.37} kg")
