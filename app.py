import streamlit as st
import random
from datetime import datetime
import time

# 1. CONFIGURATION
st.set_page_config(page_title="Hacker Cosmic 1CA", page_icon="🛰️", layout="wide")

# 2. DESIGN ÉLITE NÉON
st.markdown("""
    <style>
    .stApp { background: radial-gradient(ellipse at bottom, #1B2735 0%, #050505 100%); color: white; }
    h1 { color: #FF00FF !important; text-shadow: 0 0 20px #FF00FF, 0 0 40px #FF00FF; text-align: center; font-family: 'Orbitron', sans-serif; }
    h2, h3, label, p, span { color: #00FFFF !important; text-shadow: 0 0 10px #00FFFF; }
    .stMetric div { color: #39FF14 !important; }
    img { border-radius: 20px; border: 3px solid #00FFFF; box-shadow: 0 0 20px #00FFFF; }
    [data-testid="stSidebar"] { background-color: #000000 !important; border-right: 2px solid #FF00FF; }
    </style>
    """, unsafe_allow_html=True)

# 3. MENU SIDEBAR (Signé Règne)
with st.sidebar:
    st.markdown('<p style="color:#FF00FF; font-weight:bold; border:2px solid #FF00FF; padding:10px; border-radius:15px; text-align:center; box-shadow: 0 0 15px #FF00FF;">👑 CRÉATEUR : RÈGNE</p>', unsafe_allow_html=True)
    st.title("🛰️ Navigation 1CA")
    menu = st.radio("Systèmes :", [
        "💰 Calculateur Pro", "📚 Encyclopédie du Code", "🪐 Gravité Spatiale",
        "📟 Traducteur Morse", "⚔️ Duel Multijoueur", "📐 Zone Maths", "🟢 Matrix Mode"
    ])
    st.write("---")
    st.caption("🚀 Hacker Cosmic 2026 | Spécial 1CA")

# 4. EN-TÊTE
col1, col2 = st.columns(2)
with col1: st.image("IMG_0956.png", width=220)
with col2:
    st.title("HACKER COSMIC 1CA 2026")
    st.components.v1.html("""
        <script>function parler(){var m=new SpeechSynthesisUtterance("Lancement du module multimédia. Regardez bien la vidéo d'explication.");m.lang='fr-FR';window.speechSynthesis.speak(m);}</script>
        <button onclick="parler()" style="background-color:transparent; color:#00FFFF; border:2px solid #00FFFF; padding:10px; border-radius:15px; cursor:pointer; font-weight:bold; width: 100%; box-shadow: 0 0 15px #00FFFF;">🔈 INITIALISER L'IA</button>
    """, height=70)

# 5. LOGIQUE DES PAGES

if menu == "📚 Encyclopédie du Code":
    st.header("📚 L'Encyclopédie du Code")
    
    # Image de Cyber-Codeur
    st.image("https://unsplash.com", caption="Le monde du codage t'attend...")
    
    st.write("""
    ### 🤖 1. C'est quoi le codage ?
    Imagine que tu veux commander un robot pour qu'il te prépare un **chocolat chaud**. Tu ne peux pas lui dire simplement "fais-moi un chocolat". Il faut lui donner des **étapes ultra précises**.
    
    ### 🔢 2. Le langage des machines
    L'ordinateur ne connaît que le **Binaire** (des 0 et des 1). Python est le traducteur magique entre ton cerveau et la machine.
    """)
    
    # --- VIDÉO IA ---
    st.subheader("📺 Vidéo : Qu'est-ce que l'Intelligence Artificielle ?")
    st.video("https://youtube.com") # Une vidéo courte et top sur l'IA
    
    st.write("""
    ### 🧱 3. Les trois briques du Hacker
    *   **Les Variables :** La mémoire.
    *   **Les Conditions (IF) :** L'intelligence du choix.
    *   **Les Boucles (FOR) :** La puissance de répétition.
    """)
    st.info("💡 **Le savais-tu ?** Plus de 500 nouveaux langages de code existent, mais Python est le roi pour l'IA !")

elif menu == "💰 Calculateur Pro":
    st.header("💰 Calculateur de Soldes")
    pi = st.number_input("Prix d'achat (€)", value=100.0)
    re = st.slider("Réduction (%)", 0, 100, 20)
    st.metric("Prix Final", f"{pi * (1 - re/100)} €", delta=f"-{(pi*re)/100} €")

elif menu == "🪐 Gravité Spatiale":
    st.header("🪐 Ton poids dans l'espace")
    p = st.number_input("Poids sur Terre (kg) :", value=45.0)
    dest = st.selectbox("Destination :", ["Lune 🌑", "Mars 🔴", "Jupiter 🪐"])
    f = {"Lune 🌑": 0.16, "Mars 🔴": 0.37, "Jupiter 🪐": 2.52}
    st.metric(f"Sur {dest}", f"{round(p*f[dest], 2)} kg")

elif menu == "⚔️ Duel Multijoueur":
    st.header("⚔️ Duel 1 vs 1")
    if 's' not in st.session_state: st.session_state.s = random.randint(1, 10)
    g = st.number_input("Devine le code (1-10) :", 1, 10)
    if st.button("Vérifier"):
        if g == st.session_state.s: 
            st.balloons(); st.success("WIN !"); st.session_state.s = random.randint(1, 10)
        else: st.error("NON !")

elif menu == "🟢 Matrix Mode":
    st.header("🟢 Infiltration")
    if st.button("DÉMARRER"):
        st.code("\n".join(["".join([random.choice("01") for _ in range(40)]) for _ in range(5)]))

elif menu == "📐 Zone Maths":
    st.header("📐 Aide aux Devoirs 1CA")
    v = datetime(2026, 7, 1) - datetime.now()
    st.metric("⏳ Jours avant les vacances", f"{v.days} jours")
