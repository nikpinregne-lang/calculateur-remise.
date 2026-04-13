import streamlit as st
import random
from datetime import datetime
import time

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="Hacker Cosmic Control", page_icon="🛰️", layout="wide")

# 2. DESIGN NÉON & GALAXIE (Le Peak du Design)
st.markdown("""
    <style>
    .stApp { background: radial-gradient(ellipse at bottom, #1B2735 0%, #090A0F 100%); color: white; }
    @keyframes move-twinkle-back { from {background-position:0 0;} to {background-position:-10000px 5000px;} }
    .stApp::before {
        content: ""; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
        background: transparent url('https://transparenttextures.com') repeat;
        z-index: -1; opacity: 0.4; animation: move-twinkle-back 200s linear infinite;
    }
    h1 { color: #FF00FF !important; text-shadow: 0 0 15px #FF00FF; text-align: center; }
    h2, h3, label, p, span { color: #00FFFF !important; text-shadow: 0 0 8px #00FFFF; }
    .stMetric div { color: #39FF14 !important; }
    img { border-radius: 50%; border: 4px solid #FF00FF; box-shadow: 0 0 20px #FF00FF; }
    [data-testid="stSidebar"] { background-color: rgba(10, 10, 30, 0.9); border-right: 3px solid #00FFFF; }
    </style>
    """, unsafe_allow_html=True)

# 3. MENU SIDEBAR (Poste de Pilotage)
with st.sidebar:
    st.markdown('<p style="color:#FF00FF; font-weight:bold; border:2px solid #FF00FF; padding:10px; border-radius:15px; text-align:center;">👑 CRÉATEUR : RÈGNE</p>', unsafe_allow_html=True)
    st.title("🛰️ Navigation")
    menu = st.radio("Contrôles :", [
        "💰 Calculateur Pro", "📐 Zone Maths", "📚 Exposé Codage", 
        "🧠 Exercices Code", "👾 Mission Solo", "⚔️ Duel Multijoueur",
        "💬 Hacker Chat", "🛰️ Radar Mondial", "🟢 Matrix Mode"
    ])
    st.write("---")
    st.caption("🚀 Hacker Cosmic v13.0 | By Règne")

# 4. EN-TÊTE
col1, col2 = st.columns(2)
with col1: st.image("IMG_0956.png", width=200)
with col2:
    st.title("COSMIC 1CA")
    st.components.v1.html("""
        <script>function parler(){var m=new SpeechSynthesisUtterance("Initialisation du Poste de Contrôle. Bienvenue, Maître Règne.");m.lang='fr-FR';window.speechSynthesis.speak(m);}</script>
        <button onclick="parler()" style="background-color:transparent; color:#FF00FF; border:2px solid #FF00FF; padding:10px; border-radius:15px; cursor:pointer; font-weight:bold; width: 100%;">🔈 LANCER LE SYSTÈME</button>
    """, height=70)

# 5. LOGIQUE DES CONTRÔLES

if menu == "💰 Calculateur Pro":
    st.header("💰 Calculateur de Soldes")
    c1, c2 = st.columns(2)
    pi = c1.number_input("Prix d'origine (€)", value=100.0)
    re = c2.slider("Réduction (%)", 0, 100, 20)
    rf = pi * (1 - re/100)
    st.metric("Prix Final", f"{rf} €", delta=f"-{(pi*re)/100} €", delta_color="inverse")

elif menu == "📐 Zone Maths":
    st.header("📐 Zone Mathématiques")
    st.write("### Produit en Croix (Proportionnalité)")
    ma, mb, mc = st.columns(3)
    a_v, b_v, c_v = ma.number_input("A", 1.0), mb.number_input("B", 10.0), mc.number_input("C", 5.0)
    if a_v != 0: st.success(f"Résultat : **{(b_v * c_v) / a_v}**")

elif menu == "📚 Exposé Codage":
    st.header("📚 L'Essentiel du Codage")
    st.write("Le codage est le langage des machines. Variables, conditions et boucles sont tes outils !")

elif menu == "🧠 Exercices Code":
    st.header("🧠 Teste tes connaissances")
    q = st.radio("Quel symbole sert à multiplier en Python ?", ["+", "x", "*"])
    if q == "*": st.success("Bravo ! C'est l'étoile.")

elif menu == "👾 Mission Solo":
    st.header("👾 Répare le Bug")
    st.code('print(Hello World)')
    rep = st.text_input("Répare le code (indice : guillemets) :")
    if rep == 'print("Hello World")': st.balloons(); st.success("✅ Infiltré !")

elif menu == "⚔️ Duel Multijoueur":
    st.header("⚔️ Duel : Hacker vs Hacker")
    if 'secret' not in st.session_state: st.session_state.secret = random.randint(1, 20)
    if 'win' not in st.session_state: st.session_state.win = None
    cp1, cp2 = st.columns(2)
    h1 = cp1.number_input("Hacker 1 :", 1, 20, key="h1")
    if cp1.button("Valider H1"):
        if h1 == st.session_state.secret: st.session_state.win = "Hacker 1"
    h2 = cp2.number_input("Hacker 2 :", 1, 20, key="h2")
    if cp2.button("Valider H2"):
        if h2 == st.session_state.secret: st.session_state.win = "Hacker 2"
    if st.session_state.win:
        st.balloons(); st.success(f"🏆 {st.session_state.win} gagne !")
        if st.button("Rejouer"):
            st.session_state.secret = random.randint(1, 20); st.session_state.win = None
            st.rerun()

elif menu == "💬 Hacker Chat":
    st.header("💬 Message Éphémère")
    if 'msg' not in st.session_state: st.session_state.msg = "Aucun message..."
    txt = st.text_input("Écris un message secret :")
    if st.button("Enregistrer"): st.session_state.msg = txt
    st.info(f"📜 En mémoire : {st.session_state.msg}")

elif menu == "🛰️ Radar Mondial":
    st.header("🛰️ Distance depuis Bruxelles")
    v = st.selectbox("Destination :", ["Paris (264km)", "Londres (320km)", "New York (5885km)"])
    st.success(f"Signal verrouillé sur {v}")

elif menu == "🟢 Matrix Mode":
    st.header("🟢 Infiltration Matrix")
    if st.button("DÉMARRER LE SCAN"):
        st.write("Analyse des ports...")
        time.sleep(1)
        st.code("\n".join(["".join([random.choice("01") for _ in range(30)]) for _ in range(5)]))
        st.warning("ACCÈS TOTAL OBTENU.")
