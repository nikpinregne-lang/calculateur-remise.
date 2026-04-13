import streamlit as st
import random
from datetime import datetime
import time

# 1. CONFIGURATION
st.set_page_config(page_title="Hacker Cosmic 1CA", page_icon="🛰️", layout="wide")

# 2. DESIGN ÉLITE (Néon, Étoiles et Style 1CA)
st.markdown("""
    <style>
    .stApp { background: radial-gradient(ellipse at bottom, #1B2735 0%, #050505 100%); color: white; }
    @keyframes move-twinkle-back { from {background-position:0 0;} to {background-position:-10000px 5000px;} }
    .stApp::before {
        content: ""; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
        background: transparent url('https://transparenttextures.com') repeat;
        z-index: -1; opacity: 0.3; animation: move-twinkle-back 200s linear infinite;
    }
    
    /* Titre HACKER COSMIC 1CA 2026 */
    h1 { 
        color: #FF00FF !important; 
        text-shadow: 0 0 20px #FF00FF, 0 0 40px #FF00FF; 
        text-align: center; 
        font-family: 'Orbitron', sans-serif;
    }
    
    h2, h3, label, p, span { color: #00FFFF !important; text-shadow: 0 0 10px #00FFFF; }
    .stMetric div { color: #39FF14 !important; text-shadow: 0 0 15px #39FF14; }
    
    /* Logo 1CA avec effet Glow */
    img { border-radius: 50%; border: 3px solid #00FFFF; box-shadow: 0 0 25px #00FFFF; transition: 0.6s; }
    img:hover { transform: scale(1.1); border-color: #FF00FF; box-shadow: 0 0 35px #FF00FF; }

    /* Sidebar Spéciale 1CA */
    [data-testid="stSidebar"] { background-color: #000000 !important; border-right: 2px solid #FF00FF; }
    
    .stButton>button {
        background-color: transparent;
        color: #00FFFF;
        border: 2px solid #00FFFF;
        border-radius: 15px;
        box-shadow: 0 0 10px #00FFFF;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. INITIALISATION MÉMOIRE
if 'historique' not in st.session_state: st.session_state.historique = []

# 4. SIDEBAR (Signé Règne pour la 1CA)
with st.sidebar:
    st.markdown('<p style="color:#FF00FF; font-weight:bold; border:2px solid #FF00FF; padding:10px; border-radius:15px; text-align:center; box-shadow: 0 0 15px #FF00FF;">👑 CRÉATEUR : RÈGNE</p>', unsafe_allow_html=True)
    st.title("🛰️ Navigation 1CA")
    menu = st.radio("Systèmes :", [
        "💰 Calculateur Pro", "📚 Encyclopédie du Code", "🪐 Gravité Spatiale",
        "📟 Traducteur Morse", "🤖 Cosmic Chatbot", "⚔️ Duel Multijoueur",
        "📐 Zone Maths", "📜 Journal de Bord", "🟢 Matrix Mode"
    ])
    st.write("---")
    st.caption("🚀 Hacker Cosmic 2026 | Spécial 1CA")

# 5. EN-TÊTE (LOGO + TITRE FINAL + VOIX)
col1, col2 = st.columns(2)
with col1: st.image("IMG_0956.png", width=220)
with col2:
    st.title("HACKER COSMIC 1CA 2026")
    st.components.v1.html("""
        <script>function parler(){var m=new SpeechSynthesisUtterance("Liaison établie. Bienvenue dans le domaine de la meilleure classe de l'univers : la un cé ah. Salut à tous les élèves de deux mille vingt-six.");m.lang='fr-FR';window.speechSynthesis.speak(m);}</script>
        <button onclick="parler()" style="background-color:transparent; color:#00FFFF; border:2px solid #00FFFF; padding:10px; border-radius:15px; cursor:pointer; font-weight:bold; width: 100%; box-shadow: 0 0 15px #00FFFF;">🔈 INITIALISER LA SESSION 1CA</button>
    """, height=70)

# 6. LOGIQUE DES PAGES
if menu == "💰 Calculateur Pro":
    st.header("💰 Calculateur de Soldes")
    pi = st.number_input("Prix d'origine (€)", value=100.0)
    re = st.slider("Réduction (%)", 0, 100, 20)
    rf = pi * (1 - re/100)
    st.metric("Prix Final", f"{rf} €", delta=f"-{(pi*re)/100} €")
    if st.button("💾 Sauvegarder"):
        st.session_state.historique.append(f"{pi}€ - {re}% = {rf}€")
        st.toast("Enregistré pour la 1CA !")

elif menu == "📚 Encyclopédie du Code":
    st.header("📚 L'Essentiel du Codage")
    st.write("Apprendre à coder, c'est apprendre à construire le monde de demain.")

elif menu == "🪐 Gravité Spatiale":
    st.header("🪐 Ton poids dans l'espace")
    p = st.number_input("Poids sur Terre (kg) :", value=45.0)
    f = {"Lune 🌑": 0.16, "Mars 🔴": 0.37, "Jupiter 🪐": 2.52}
    dest = st.selectbox("Choisir une planète :", list(f.keys()))
    st.metric(f"Sur {dest}", f"{round(p*f[dest], 2)} kg")

elif menu == "📟 Traducteur Morse":
    st.header("📟 Codes Secrets")
    t = st.text_input("Message à coder :", value="1CA")
    d = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.','0':'-----',' ':'/'}
    st.code(" ".join([d.get(c.upper(), '') for c in t]))

elif menu == "📜 Journal de Bord":
    st.header("📜 Historique de Session")
    if not st.session_state.historique: st.write("Journal vide.")
    for item in reversed(st.session_state.historique): st.write(f"🔹 {item}")
    if st.button("🗑️ Effacer"): 
        st.session_state.historique = []
        st.rerun()

elif menu == "⚔️ Duel Multijoueur":
    st.header("⚔️ Duel 1 vs 1 (Spécial 1CA)")
    if 's' not in st.session_state: st.session_state.s = random.randint(1, 10)
    g = st.number_input("Devine le code secret (1-10) :", 1, 10)
    if st.button("Vérifier"):
        if g == st.session_state.s: 
            st.balloons(); st.success("WIN ! Le code était bien " + str(g)); st.session_state.s = random.randint(1, 10)
        else: st.error("ÉCHEC. Le système résiste !")

elif menu == "🟢 Matrix Mode":
    st.header("🟢 Infiltration du Réseau")
    if st.button("DÉMARRER LE SCAN"):
        st.code("\n".join(["".join([random.choice("01") for _ in range(40)]) for _ in range(5)]))

elif menu == "📐 Zone Maths":
    st.header("📐 Aide aux Devoirs 1CA")
    st.write("Assistant mathématique activé.")
    st.number_input("Valeur de base", value=1.0)
