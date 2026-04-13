import streamlit as st
import random
from datetime import datetime

# 1. CONFIGURATION ÉLITE
st.set_page_config(page_title="Hacker Cosmic 2026", page_icon="❄️", layout="wide")

# 2. DESIGN GLACIER NÉON (Le retour du look Hacker)
st.markdown("""
    <style>
    .stApp { background: radial-gradient(ellipse at bottom, #001f3f 0%, #00050a 100%); color: #e0f7fa; }
    @keyframes move-snow { from {background-position: 0px 0px;} to {background-position: 500px 1000px;} }
    .stApp::before {
        content: ""; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
        background: transparent url('https://transparenttextures.com') repeat;
        z-index: -1; opacity: 0.5; animation: move-snow 100s linear infinite;
    }
    h1 { color: #ffffff !important; text-shadow: 0 0 15px #00ffff, 0 0 30px #00ffff; text-align: center; font-family: 'Orbitron', sans-serif; }
    h2, h3, label, p, span { color: #00ffff !important; text-shadow: 0 0 8px #00ffff; }
    .stMetric div { color: #b2ff59 !important; text-shadow: 0 0 15px #b2ff59; }
    [data-testid="stSidebar"] { background-color: #000b1a !important; border-right: 3px solid #00ffff; }
    img { border-radius: 50%; border: 4px solid #ffffff; box-shadow: 0 0 30px #00ffff; transition: 1s; }
    img:hover { transform: rotate(360deg) scale(1.1); }
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR (Créé par RÈGNE)
with st.sidebar:
    st.markdown('<p style="color:#00ffff; font-weight:bold; border:2px solid #ffffff; padding:10px; border-radius:15px; text-align:center; box-shadow: 0 0 15px #00ffff;">🧊 ÉTAT : CRYOGÉNISÉ</p>', unsafe_allow_html=True)
    langue = st.selectbox("🌐 Langue", ["Français", "English", "Español"])
    st.write("---")
    m_txt = {"Français": ["🤖 IA Cosmique", "💰 Calculateur Pro", "📐 Zone Maths", "📚 Encyclopédie", "🎮 Mission Code", "⚔️ Duel Multi"], 
             "English": ["🤖 Cosmic AI", "💰 Pro Calculator", "📐 Math Zone", "📚 Encyclopedia", "🎮 Code Mission", "⚔️ Multi Duel"],
             "Español": ["🤖 IA Cósmica", "💰 Calculadora Pro", "📐 Zona Mates", "📚 Enciclopedia", "🎮 Misión Code", "⚔️ Duelo Multi"]}
    menu = st.radio("Secteurs :", m_txt[langue])
    st.write("---")
    st.markdown(f"<p style='font-size: 12px; opacity: 0.7;'>❄️ Hacker Cosmic Glacier | Créé par <b>RÈGNE</b></p>", unsafe_allow_html=True)

# 4. EN-TÊTE
col1, col2 = st.columns(2)
with col1: st.image("IMG_0956.png", width=200)
with col2:
    st.title("HACKER COSMIC 1CA 2026")
    v_txt = {"Français": "Liaison établie. Bonjour Maître Règne.", "English": "Link established. Hello Master Règne.", "Español": "Conexión lista. Hola Maestro."}
    v_lang = {"Français": "fr-FR", "English": "en-US", "Español": "es-ES"}
    st.components.v1.html(f"""
        <script>function parler(){{var m=new SpeechSynthesisUtterance("{v_txt[langue]}");m.lang='{v_lang[langue]}';window.speechSynthesis.speak(m);}}</script>
        <button onclick="parler()" style="background-color:transparent; color:#ffffff; border:2px solid #00ffff; padding:10px; border-radius:15px; cursor:pointer; font-weight:bold; width:100%; box-shadow: 0 0 15px #00ffff;">🔈 INITIALISER</button>
    """, height=70)

# 5. PAGES
if "IA" in menu:
    st.header("🤖 IA Chatbot")
    q = st.text_input("Pose ta question :").lower()
    if st.button("INTERROGER"):
        if "salut" in q: st.write("❄️ Salut Hacker ! Prêt pour une mission ?")
        elif "qui" in q: st.write("👑 Je suis l'IA créée par le Maître Règne.")
        else: st.write("🔍 Analyse en cours...")

elif "Calcul" in menu:
    st.header("💰 Calculateur de Soldes")
    pi = st.number_input("Prix (€)", value=100.0)
    re = st.slider("Réduction (%)", 0, 100, 20)
    st.metric("PRIX FINAL", f"{pi*(1-re/100)} €", delta=f"-{(pi*re)/100} €")

elif "Math" in menu or "Mates" in menu:
    st.header("📐 Zone Mathématique")
    ma, mb, mc = st.columns(3)
    res = (mb.number_input("B", value=10.0) * mc.number_input("C", value=5.0)) / ma.number_input("A", value=1.0)
    st.success(f"Résultat : {res}")

elif "Ency" in menu:
    st.header("📚 L'Encyclopédie du Codage")
    st.write("Le codage est l'art de parler aux machines.")
    st.video("https://youtube.com")

elif "Mission" in menu:
    st.header("🎮 Mission : Répare le Bug")
    st.code('print(Bonjour 1CA)')
    if st.text_input("Répare le code :") == 'print("Bonjour 1CA")': st.balloons()
