import streamlit as st
import random
from datetime import datetime

# 1. CONFIGURATION
st.set_page_config(page_title="Hacker Cosmic App", page_icon="🚀", layout="wide")

# 2. DESIGN NÉON & GALAXIE
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
    h2, h3, label, p, span { color: #00FFFF !important; text-shadow: 0 0 5px #00FFFF; }
    .stMetric div { color: #39FF14 !important; text-shadow: 0 0 10px #39FF14; }
    img { border-radius: 20px; border: 3px solid #00FFFF; box-shadow: 0 0 20px #00FFFF; transition: 0.4s; }
    img:hover { transform: scale(1.05); }
    [data-testid="stSidebar"] { background-color: rgba(0, 15, 15, 0.9); border-right: 2px solid #00FFFF; }
    </style>
    """, unsafe_allow_html=True)

# 3. MENU SIDEBAR
with st.sidebar:
    st.markdown('<p style="color:#39FF14; font-weight:bold; border:2px solid #39FF14; padding:10px; border-radius:15px; text-align:center;">🟢 SYSTEM ONLINE</p>', unsafe_allow_html=True)
    st.title("🛰️ Navigation")
    menu = st.radio("Outils :", ["💰 Calculateur", "📐 Zone Maths", "🎮 Défi Jeu", "🛠️ Outils Pratiques", "💎 Gamer Tool", "🔐 Sécurité"])
    st.write("---")
    st.subheader("🎵 Ambiance")
    st.video("https://youtube.com")
    st.write("---")
    st.caption("🚀 Hacker Cosmic | 2026")

# 4. EN-TÊTE
col_h1, col_h2 = st.columns(2)
with col_h1: st.image("IMG_0956.png")
with col_h2:
    st.title("HACKER COSMIC 1CA")
    st.components.v1.html("""
        <script>function parler(){var m=new SpeechSynthesisUtterance("Accès autorisé. Bonjour Hacker Cosmic.");m.lang='fr-FR';window.speechSynthesis.speak(m);}</script>
        <button onclick="parler()" style="background-color:transparent; color:#00FFFF; border:2px solid #00FFFF; padding:10px; border-radius:15px; cursor:pointer; font-weight:bold; box-shadow: 0 0 10px #00FFFF;">🔈 ACTIVER L'IA</button>
    """, height=70)

# 5. PAGES
if menu == "💰 Calculateur":
    st.header("💰 Calculateur de Soldes")
    c1, c2 = st.columns(2)
    with c1: pi = st.number_input("Prix (€)", value=100.0)
    with c2: re = st.slider("Réduction (%)", 0, 100, 20)
    rf = pi * (1 - re/100)
    st.metric("Prix Final", f"{rf} €", delta=f"-{(pi*re)/100} €", delta_color="inverse")
    st.info(f"✍️ **Détail :** {pi} € - ({pi} € $\cdot$ {re}/100) = {rf} €")

elif menu == "📐 Zone Maths":
    st.header("📐 Spécial Prof de Math")
    outil = st.selectbox("Outil :", ["Géométrie", "Produit en Croix"])
    if outil == "Géométrie":
        f = st.selectbox("Forme :", ["Rectangle", "Triangle"])
        if f == "Rectangle":
            L = st.number_input("Longueur", value=10.0); l = st.number_input("Largeur", value=5.0)
            st.write("**Formule :** $L \cdot l$")
            st.success(f"Aire = {L*l}")
        else:
            b = st.number_input("Base", value=10.0); h = st.number_input("Hauteur", value=5.0)
            st.write("**Formule :** $(b \cdot h) / 2$")
            st.success(f"Aire = {(b*h)/2}")
    else:
        st.write("Si A $\\rightarrow$ B, alors C $\\rightarrow$ ?")
        ma, mb, mc = st.columns(3)
        res = (mb.number_input("B", value=10.0) * mc.number_input("C", value=5.0)) / ma.number_input("A", value=1.0)
        st.success(f"Résultat : {res}")

elif menu == "🎮 Défi Jeu":
    st.header("🎮 Mission : Le Juste Prix")
    if 'score' not in st.session_state: st.session_state.score = 0
    if 'best' not in st.session_state: st.session_state.best = 0
    if 'cible' not in st.session_state: st.session_state.cible = 25.0
    st.write(f"🏆 Score : **{st.session_state.score}** | 🥇 Record : **{st.session_state.best}**")
    st.warning(f"🎯 Cible : **{st.session_state.cible} €**")
    if st.button("🎲 Nouveau défi"):
        st.session_state.cible = float(random.randint(10, 80)); st.session_state.gagne = False
        st.rerun()
    p_j = st.slider("Réduction (sur base 100€)", 0, 100, 50)
    test = round(100 * (1 - p_j/100), 2)
    st.write(f"💵 Test : **{test} €**")
    if test == st.session_state.cible and not st.session_state.get('gagne', False):
        st.session_state.score += 1; st.session_state.gagne = True
        if st.session_state.score > st.session_state.best: st.session_state.best = st.session_state.score
        st.balloons(); st.success("🏆 COMPTE EST BON !")

elif menu == "🛠️ Outils Pratiques":
    st.header("🛠️ Boîte à Outils")
    v = datetime(2026, 7, 1) - datetime.now()
    st.metric("⏳ Avant les vacances d'été", f"{v.days} jours")
    st.write("---")
    st.subheader("📲 Générateur de QR Code")
    lien = st.text_input("Lien ou texte :", "https://google.com")
    st.image(f"https://qrserver.com{lien}", caption="Scanne-moi !")

elif menu == "💎 Gamer Tool":
    st.header("💎 Gamer Zone")
    eu = st.number_input("Montant (€)", value=10)
    st.write(f"💎 **Robux :** {int(eu*80)} | 🔥 **V-Bucks :** {int(eu*110)}")

elif menu == "🔐 Sécurité":
    st.header("🔐 Hacker Password Gen")
    if st.button("🚀 GÉNÉRER"):
        st.code("".join(random.sample("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*", 12)))
