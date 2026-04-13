import streamlit as st
import random
from datetime import datetime
import time

# --- 1. CONFIGURATION ÉLITE ---
st.set_page_config(page_title="Hacker Cosmic 2026", page_icon="❄️", layout="wide")

# --- 2. DESIGN GLACIER NÉON (CSS ULTRA COMPLET) ---
st.markdown("""
    <style>
    /* Fond de base style banquise spatiale */
    .stApp { 
        background: radial-gradient(ellipse at bottom, #001f3f 0%, #00050a 100%); 
        color: #e0f7fa; 
    }
    
    /* Animation de neige stellaire infinie */
    @keyframes move-snow {
        from {background-position: 0px 0px;}
        to {background-position: 500px 1000px;}
    }
    .stApp::before {
        content: ""; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
        background: transparent url('https://transparenttextures.com') repeat;
        z-index: -1; opacity: 0.5; animation: move-snow 100s linear infinite;
    }

    /* Titre HACKER COSMIC avec lueur de glace */
    h1 { 
        color: #ffffff !important; 
        text-shadow: 0 0 15px #00ffff, 0 0 30px #00ffff, 0 0 45px #ffffff; 
        text-align: center; 
        font-family: 'Orbitron', sans-serif;
    }
    h2, h3, label, p, span { 
        color: #00ffff !important; 
        text-shadow: 0 0 8px #00ffff; 
    }
    
    /* Résultats chiffrés en Vert Aurore Boréale */
    .stMetric div { 
        color: #b2ff59 !important; 
        text-shadow: 0 0 15px #b2ff59; 
    }

    /* Barre latérale (Sidebar) style cryogénique */
    [data-testid="stSidebar"] { 
        background-color: #000b1a !important; 
        border-right: 3px solid #00ffff; 
    }

    /* Boutons style Cristal Néon */
    .stButton>button {
        background-color: rgba(0, 255, 255, 0.05);
        color: #ffffff;
        border: 2px solid #00ffff;
        border-radius: 20px;
        box-shadow: 0 0 15px #00ffff;
        transition: 0.5s;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #00ffff;
        color: #000000;
        box-shadow: 0 0 30px #ffffff;
        transform: scale(1.05);
    }
    
    /* Logo tournant 1CA */
    img { 
        border-radius: 50%; 
        border: 4px solid #ffffff; 
        box-shadow: 0 0 30px #00ffff; 
        transition: 1s; 
    }
    img:hover { transform: rotate(360deg) scale(1.1); }

    /* Style des boîtes de saisie */
    .stTextInput>div>div>input {
        background-color: #001a33;
        color: #00ffff;
        border: 1px solid #00ffff;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. MÉMOIRE DU SYSTÈME (SESSION STATE) ---
if 'score_multi' not in st.session_state: st.session_state.score_multi = {"H1": 0, "H2": 0}
if 'code_secret' not in st.session_state: st.session_state.code_secret = random.randint(1, 20)
if 'historique_calculs' not in st.session_state: st.session_state.historique_calculs = []

# --- 4. BARRE LATÉRALE (POSTE DE PILOTAGE) ---
with st.sidebar:
    st.markdown('<p style="color:#00ffff; font-weight:bold; border:2px solid #ffffff; padding:10px; border-radius:15px; text-align:center; box-shadow: 0 0 15px #00ffff;">🧊 ÉTAT : CRYOGÉNISÉ</p>', unsafe_allow_html=True)
    
    # SÉLECTEUR DE LANGUE
    langue = st.selectbox("🌐 Zone Linguistique", ["Français", "English", "Español"])
    st.write("---")
    
    # MENU NAVIGATION (TOUT EST GARDÉ + AJOUTS)
    m_dict = {
        "Français": ["🤖 IA Cosmique", "💰 Calculateur Pro", "📐 Zone Maths", "📚 Encyclopédie", "🎮 Mission Code", "⚔️ Duel Multi", "🪐 Espace Givre", "🔐 Labo Secret", "🟢 Matrix Mode", "🕒 Terminal"],
        "English": ["🤖 Cosmic AI", "💰 Pro Calculator", "📐 Math Zone", "📚 Encyclopedia", "🎮 Code Mission", "⚔️ Multi Duel", "🪐 Ice Space", "🔐 Secret Lab", "🟢 Matrix Mode", "🕒 Terminal"],
        "Español": ["🤖 IA Cósmica", "💰 Calculadora Pro", "📐 Zona Mates", "📚 Enciclopedia", "🎮 Misión Code", "⚔️ Duelo Multi", "🪐 Espacio Hielo", "🔐 Labo Secreto", "🟢 Matrix Mode", "🕒 Terminal"]
    }
    menu = st.radio("Secteurs du site :", m_dict[langue])
    
    st.write("---")
    # CHANGEMENT ICI : "BY RÈGNE" DEVIENT "CRÉÉ PAR RÈGNE"
    st.markdown(f"<p style='font-size: 12px; opacity: 0.7;'>❄️ Hacker Cosmic Glacier | Créé par <b>RÈGNE</b></p>", unsafe_allow_html=True)
    st.caption(f"📅 Date stellaire : {datetime.now().strftime('%d/%m/%Y')}")

# --- 5. EN-TÊTE (LOGO + TITRE + VOIX) ---
col1, col2 = st.columns(2)
with col1: st.image("IMG_0956.png", width=220)
with col2:
    st.title("HACKER COSMIC 1CA 2026")
    v_txt = {
        "Français": "Connexion sécurisée. Bienvenue dans ton domaine glacé, Maître Règne.",
        "English": "Secure connection. Welcome to your frozen domain, Master Règne.",
        "Español": "Conexión segura. Bienvenido a tu dominio helado, Maestro Règne."
    }
    v_lang = {"Français": "fr-FR", "English": "en-US", "Español": "es-ES"}
    
    st.components.v1.html(f"""
        <script>function parler(){{var m=new SpeechSynthesisUtterance("{v_txt[langue]}");m.lang='{v_lang[langue]}';window.speechSynthesis.speak(m);}}</script>
        <button onclick="parler()" style="background-color:transparent; color:#ffffff; border:2px solid #00ffff; padding:10px; border-radius:15px; cursor:pointer; font-weight:bold; width:100%; box-shadow: 0 0 15px #00ffff;">🔈 LANCER LA SYNCHRONISATION</button>
    """, height=70)

# --- 6. LOGIQUE DES SECTEURS (PAGES) ---

# --- PAGE IA ---
if "IA" in menu:
    st.header(f"🤖 IA Chatbot {langue}")
    user_q = st.text_input("Pose ta question au cerveau de glace :").lower()
    if st.button("INTERROGER L'IA"):
        if "salut" in user_q: st.write("❄️ Salut Hacker ! Prêt pour une mission givrée ?")
        elif "qui" in user_q: st.write("👑 Je suis l'IA créée par le Maître Règne pour dominer la 1CA.")
        elif "math" in user_q: st.write("📐 Je connais toutes les formules, utilise la Zone Maths !")
        else: st.write("🔍 Analyse du blizzard en cours... Pose-moi une autre question !")

# --- PAGE CALCULATEUR ---
elif "Calcul" in menu:
    st.header("💰 Calculateur de Soldes")
    c1, c2 = st.columns(2)
    p_ini = c1.number_input("Prix d'origine (€)", min_value=0.0, value=100.0)
    p_rem = c2.slider("Réduction (%)", 0, 100, 20)
    final = p_ini * (1 - p_rem/100)
    st.metric("PRIX FINAL GIVRÉ", f"{final} €", delta=f"-{(p_ini*p_rem)/100} €", delta_color="inverse")
    st.info(f"✍️ Formule : {p_ini} € - ({p_rem}%) = {final} €")

# --- PAGE MATHS ---
elif "Math" in menu or "Mates" in menu:
    st.header("📐 Zone Mathématique (Spécial Prof)")
    tab1, tab2 = st.tabs(["Produit en Croix", "Géométrie"])
    with tab1:
        ma, mb, mc = st.columns(3)
        res = (mb.number_input("Valeur B", value=10.0) * mc.number_input("Valeur C", value=5.0)) / ma.number_input("Valeur A", value=1.0)
        st.success(f"Résultat : **{res}**")
    with tab2:
        L = st.number_input("Longueur L", value=10.0)
        l_min = st.number_input("Largeur l", value=5.0)
        st.write(f"Formule de l'aire : $L \cdot l$ = **{L * l_min}**")

# --- PAGE ENCYCLOPÉDIE ---
elif "Ency" in menu:
    st.header("📚 L'Encyclopédie du Codage")
    st.write("Le codage est l'art de donner des instructions précises aux machines.")
    st.video("https://youtube.com")
    st.link_button("🚀 Voir la vidéo en plein écran", "https://youtube.com")

# --- PAGE MISSION CODE ---
elif "Mission" in menu:
    st.header("🎮 Mission : Répare le Bug")
    st.code('print(Bonjour 1CA)')
    repa = st.text_input("Récupère les guillemets manquants :")
    if repa == 'print("Bonjour 1CA")': 
        st.balloons()
        st.success("✅ SYSTÈME DÉBLOQUÉ !")

# --- PAGE DUEL ---
elif "Duel" in menu:
    st.header("⚔️ Duel : Hacker vs Hacker")
    st.write(f"🏆 Score actuel : H1 [{st.session_state.score_multi['H1']}] | H2 [{st.session_state.score_multi['H2']}]")
    cp1, cp2 = st.columns(2)
    h1_g = cp1.number_input("Hacker 1 (1-20)", 1, 20, key="h1")
    if cp1.button("TESTER H1"):
        if h1_g == st.session_state.code_secret:
            st.session_state.score_multi['H1'] += 1; st.balloons(); st.success("H1 GAGNE !"); st.session_state.code_secret = random.randint(1, 20)
    h2_g = cp2.number_input("Hacker 2 (1-20)", 1, 20, key="h2")
    if cp2.button("TESTER H2"):
        if h2_g == st.session_state.code_secret:
            st.session_state.score_multi['H2'] += 1; st.balloons(); st.success("H2 GAGNE !"); st.session_state.code_secret = random.randint(1, 20)

# --- PAGE LABO SECRET (NOUVEAU) ---
elif "Labo" in menu:
    st.header("🔐 Labo Secret de Règne")
    
    st.subheader("📲 Générateur de QR Code")
    lien_qr = st.text_input("Entre un lien ou un texte :", "https://google.com")
    qr_api = f"https://qrserver.com{lien_qr}"
    st.image(qr_api, caption="Scanne ton code !")
    
    st.write("---")
    st.subheader("🤖 Traducteur Binaire")
    txt_bin = st.text_input("Entre un nombre :", value="42")
    if txt_bin.isdigit():
        st.code(bin(int(txt_bin)).replace("0b", ""), language="python")

# --- PAGE ESPACE ---
elif "Espace" in menu or "Espacio" in menu:
    st.header("🪐 Gravité dans le Givre")
    pds = st.number_input("Ton poids sur Terre (kg)", value=50.0)
    st.metric("Sur Mars 🔴", f"{pds * 0.37} kg")
    st.metric("Sur la Lune 🌑", f"{pds * 0.16} kg")

# --- PAGE MATRIX ---
elif "Matrix" in menu:
    st.header("🟢 Infiltration Matrix")
    if st.button("LANCER LE SCAN"):
        st.code("\n".join(["".join([random.choice("01") for _ in range(40)]) for _ in range(8)]))

# --- PAGE TERMINAL ---
elif "Terminal" in menu:
    st.header("🕒 Terminal de Bord")
    st.write(f"Heure locale : **{datetime.now().strftime('%H:%M:%S')}**")
    st.text_area("Notes de mission :", "Système Glacier sous contrôle total...")
