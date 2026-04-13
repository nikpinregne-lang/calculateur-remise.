import streamlit as st
import random
from datetime import datetime
import time

# 1. CONFIGURATION & DESIGN NÉON
st.set_page_config(page_title="Hacker Cosmic Master", page_icon="🛰️", layout="wide")

st.markdown("""
    <style>
    .stApp { background: radial-gradient(ellipse at bottom, #1B2735 0%, #090A0F 100%); color: white; }
    h1 { color: #FF00FF !important; text-shadow: 0 0 15px #FF00FF; text-align: center; }
    h2, h3, label, p, span { color: #00FFFF !important; text-shadow: 0 0 8px #00FFFF; }
    [data-testid="stSidebar"] { background-color: rgba(10, 10, 30, 0.9); border-right: 3px solid #00FFFF; }
    .stMetric div { color: #39FF14 !important; }
    img { border-radius: 50%; border: 3px solid #FF00FF; box-shadow: 0 0 20px #FF00FF; transition: 0.5s; }
    img:hover { transform: rotate(360deg); }
    </style>
    """, unsafe_allow_html=True)

# 2. INITIALISATION DE LA MÉMOIRE (Session State)
if 'historique' not in st.session_state:
    st.session_state.historique = []

# 3. MENU SIDEBAR (Poste de Pilotage)
with st.sidebar:
    st.markdown('<p style="color:#FF00FF; font-weight:bold; border:2px solid #FF00FF; padding:10px; border-radius:15px; text-align:center;">👑 CRÉATEUR : RÈGNE</p>', unsafe_allow_html=True)
    st.title("🛰️ Navigation")
    menu = st.radio("Contrôles :", [
        "💰 Calculateur Pro", 
        "📚 Encyclopédie du Code", 
        "🪐 Gravité Spatiale",
        "📟 Traducteur Morse",
        "🤖 Cosmic Chatbot", 
        "⚔️ Duel Multijoueur",
        "📐 Zone Maths", 
        "📜 Journal de Bord",
        "🟢 Matrix Mode"
    ])
    st.write("---")
    st.caption("🚀 Hacker Cosmic v16.0 | By Règne")

# 4. EN-TÊTE
col1, col2 = st.columns(2)
with col1: st.image("IMG_0956.png", width=200)
with col2:
    st.title("COSMIC STATION 1CA")
    st.components.v1.html("""
        <script>function parler(){var m=new SpeechSynthesisUtterance("Initialisation complète du module seize point zéro. Bienvenue, Maître Règne.");m.lang='fr-FR';window.speechSynthesis.speak(m);}</script>
        <button onclick="parler()" style="background-color:transparent; color:#FF00FF; border:2px solid #FF00FF; padding:10px; border-radius:15px; cursor:pointer; font-weight:bold; width: 100%;">🔈 LANCER LA SESSION</button>
    """, height=70)

# 5. LOGIQUE DES PAGES

# --- PAGE : CALCULATEUR AVEC HISTORIQUE ---
if menu == "💰 Calculateur Pro":
    st.header("💰 Calculateur de Soldes")
    pi = st.number_input("Prix d'origine (€)", value=100.0)
    re = st.slider("Réduction (%)", 0, 100, 20)
    rf = pi * (1 - re/100)
    st.metric("Prix Final", f"{rf} €", delta=f"-{(pi*re)/100} €")
    
    if st.button("💾 Enregistrer dans le journal"):
        st.session_state.historique.append(f"Remise de {re}% sur {pi}€ = {rf}€")
        st.success("Calcul sauvegardé !")

# --- PAGE : ENCYCLOPÉDIE ---
elif menu == "📚 Encyclopédie du Code":
    st.header("📚 Le Guide du Jeune Hacker")
    st.write("""
    ### 🤖 C'est quoi le codage ?
    C'est comme une recette de cuisine pour robot. Si tu oublies de dire "mélange", il ne se passera rien !
    ### 🔢 Le Binaire
    Les ordinateurs ne parlent qu'avec des **0** et des **1**. Python est notre traducteur magique.
    ### 🧱 Les Variables
    C'est la boîte où tu ranges ton score ou ton nom. Sans variable, l'ordinateur oublie tout !
    """)

# --- PAGE : GRAVITÉ SPATIALE ---
elif menu == "🪐 Gravité Spatiale":
    st.header("🪐 Mission : Ton poids dans l'espace")
    poids = st.number_input("Ton poids sur Terre (kg) :", value=45.0)
    planete = st.selectbox("Choisir une destination :", ["La Lune 🌑", "Mars 🔴", "Jupiter 🪐"])
    
    facteurs = {"La Lune 🌑": 0.165, "Mars 🔴": 0.377, "Jupiter 🪐": 2.528}
    poids_final = poids * facteurs[planete]
    
    st.metric(f"Ton poids sur {planete}", f"{round(poids_final, 2)} kg")
    st.info("💡 Savais-tu que sur Jupiter, tu serais tellement lourd que tu ne pourrais pas marcher ?")

# --- PAGE : MORSE ---
elif menu == "📟 Traducteur Morse":
    st.header("📟 Encodeur Morse Secret")
    texte = st.text_input("Tape ton message (en lettres) :", value="HACKER")
    
    dict_morse = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 
                  'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 
                  'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 
                  'Y':'-.--', 'Z':'--..', ' ':'/'}
    
    code_m = " ".join([dict_morse.get(c.upper(), '') for c in texte])
    st.code(code_m)
    st.caption("Partage ce code à tes amis pour qu'ils te répondent en secret ! 🤫")

# --- PAGE : JOURNAL DE BORD ---
elif menu == "📜 Journal de Bord":
    st.header("📜 Historique de la Session")
    if not st.session_state.historique:
        st.write("Le journal est vide. Fais des calculs pour le remplir !")
    else:
        for item in reversed(st.session_state.historique):
            st.write(f"🔹 {item}")
        if st.button("🗑️ Effacer le journal"):
            st.session_state.historique = []
            st.rerun()

# --- AUTRES PAGES ---
elif menu == "🤖 Cosmic Chatbot":
    st.header("🤖 Cosmic Chatbot")
    q = st.text_input("Question :")
    if st.button("Parler"):
        st.chat_message("assistant").write("Je suis en train d'apprendre... Demande-moi plutôt de calculer une remise !")

elif menu == "⚔️ Duel Multijoueur":
    st.header("⚔️ Duel 1 vs 1")
    if 'sec' not in st.session_state: st.session_state.sec = random.randint(1, 10)
    guess = st.number_input("Devine le chiffre :", 1, 10)
    if st.button("Vérifier"):
        if guess == st.session_state.sec:
            st.balloons(); st.success("GAGNÉ !"); st.session_state.sec = random.randint(1, 10)
        else: st.error("ÉCHEC...")

elif menu == "📐 Zone Maths":
    st.header("📐 Zone Maths")
    st.number_input("Valeur A", value=1.0)

elif menu == "🟢 Matrix Mode":
    st.header("🟢 Matrix Mode")
    if st.button("RUN"):
        st.code("\n".join(["".join([random.choice("01") for _ in range(40)]) for _ in range(5)]))
