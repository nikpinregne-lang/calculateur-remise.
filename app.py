import streamlit as st
import random
from datetime import datetime
import time

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="Hacker Cosmic Glacier", page_icon="❄️", layout="wide")

# 2. DESIGN NÉON GLACÉ (Bleu Givre, Blanc Diamant et Effets de Neige)
st.markdown("""
    <style>
    /* Fond Glace Sombre */
    .stApp { 
        background: radial-gradient(ellipse at bottom, #001f3f 0%, #00050a 100%); 
        color: #e0f7fa; 
    }
    
    /* Animation Neige Stellaire */
    @keyframes move-snow {
        from {background-position: 0px 0px;}
        to {background-position: 500px 1000px;}
    }
    .stApp::before {
        content: ""; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
        background: transparent url('https://transparenttextures.com') repeat;
        z-index: -1; opacity: 0.5; animation: move-snow 100s linear infinite;
    }

    /* Titres en Blanc Néon Glacé */
    h1 { 
        color: #ffffff !important; 
        text-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff, 0 0 40px #ffffff; 
        text-align: center; 
        font-family: 'Orbitron', sans-serif;
    }
    h2, h3, label, p, span { 
        color: #00ffff !important; 
        text-shadow: 0 0 5px #00ffff; 
    }
    
    /* Metrics en Vert Aurore Boréale */
    .stMetric div { 
        color: #b2ff59 !important; 
        text-shadow: 0 0 15px #b2ff59; 
    }

    /* Sidebar Style Banquise */
    [data-testid="stSidebar"] { 
        background-color: #000b1a !important; 
        border-right: 2px solid #00ffff; 
    }

    /* Boutons en Cristal Bleu */
    .stButton>button {
        background-color: rgba(0, 255, 255, 0.1);
        color: #ffffff;
        border: 2px solid #00ffff;
        border-radius: 20px;
        box-shadow: 0 0 10px #00ffff;
        transition: 0.4s;
    }
    .stButton>button:hover {
        background-color: #00ffff;
        color: #000000;
        box-shadow: 0 0 25px #ffffff;
        transform: scale(1.05);
    }
    
    /* Image de Logo avec Lueur de Glace */
    img { 
        border-radius: 50%; 
        border: 4px solid #ffffff; 
        box-shadow: 0 0 30px #00ffff; 
        transition: 0.8s; 
    }
    img:hover { transform: rotate(360deg) scale(1.1); }
    </style>
    """, unsafe_allow_html=True)

# 3. INITIALISATION DE LA MÉMOIRE SYSTÈME
if 'score_multi' not in st.session_state: st.session_state.score_multi = {"H1": 0, "H2": 0}
if 'code_secret' not in st.session_state: st.session_state.code_secret = random.randint(1, 20)
if 'msg_sys' not in st.session_state: st.session_state.msg_sys = "Système Glacier prêt."

# 4. SIDEBAR : POSTE DE CONTRÔLE POLAIRE
with st.sidebar:
    st.markdown('<p style="color:#00ffff; font-weight:bold; border:2px solid #ffffff; padding:10px; border-radius:15px; text-align:center; box-shadow: 0 0 15px #00ffff;">🧊 STATUS : FROZEN</p>', unsafe_allow_html=True)
    
    # MULTILANGUE
    langue = st.selectbox("🌐 Choix du Secteur (Langue)", ["Français", "English", "Español"])
    st.write("---")
    
    # MENU TOTAL (On garde TOUT)
    m_dict = {
        "Français": ["🤖 IA Cosmique", "💰 Calculateur Pro", "📐 Zone Maths", "📚 Encyclopédie", "🎮 Mission Code", "⚔️ Duel Multi", "🪐 Espace Givre", "🟢 Matrix Mode", "🕒 Terminal"],
        "English": ["🤖 Cosmic AI", "💰 Pro Calculator", "📐 Math Zone", "📚 Encyclopedia", "🎮 Code Mission", "⚔️ Multi Duel", "🪐 Ice Space", "🟢 Matrix Mode", "🕒 Terminal"],
        "Español": ["🤖 IA Cósmica", "💰 Calculadora Pro", "📐 Zona Mates", "📚 Enciclopedia", "🎮 Misión Code", "⚔️ Duelo Multi", "🪐 Espacio Hielo", "🟢 Matrix Mode", "🕒 Terminal"]
    }
    menu = st.radio("Navigation :", m_dict[langue])
    
    st.write("---")
    st.caption(f"❄️ Hacker Cosmic Glacier | By RÈGNE")
    st.write(f"📅 {datetime.now().strftime('%d/%m/%Y')}")

# 5. EN-TÊTE (LOGO + TITRE GIVRÉ + VOIX)
col1, col2 = st.columns(2)
with col1: st.image("IMG_0956.png", width=220)
with col2:
    st.title("HACKER COSMIC 1CA 2026")
    vocal_txt = {
        "Français": "Liaison cryogénique établie. Bienvenue dans le glacier de Hacker Cosmic Maître Règne.",
        "English": "Cryogenic link established. Welcome to the Hacker Cosmic glacier, Master Règne.",
        "Español": "Enlace criogénico establecido. Bienvenido al glaciar de Hacker Cósmico, Maestro Règne."
    }
    v_lang = {"Français": "fr-FR", "English": "en-US", "Español": "es-ES"}
    
    st.components.v1.html(f"""
        <script>function parler(){{var m=new SpeechSynthesisUtterance("{vocal_txt[langue]}");m.lang='{v_lang[langue]}';window.speechSynthesis.speak(m);}}</script>
        <button onclick="parler()" style="background-color:transparent; color:#ffffff; border:2px solid #00ffff; padding:10px; border-radius:15px; cursor:pointer; font-weight:bold; width:100%; box-shadow: 0 0 15px #00ffff;">🔈 INITIALISER LE FLUX GLACÉ</button>
    """, height=70)

# 6. LOGIQUE DES PAGES (TOUT, TOUT, TOUT)

# --- PAGE IA ---
if "IA" in menu:
    st.header(f"🤖 IA Chatbot {langue}")
    user_q = st.text_input("Pose ta question au cerveau glacé :").lower()
    if st.button("INTERROGER"):
        if "salut" in user_q or "hello" in user_q: st.write("❄️ Salut Hacker ! Prêt pour une mission givrée ?")
        elif "qui" in user_q: st.write("👑 Je suis l'IA créée par Règne pour dominer la 1CA.")
        else: st.write("🔍 Analyse du blizzard en cours... Question non répertoriée.")

# --- PAGE CALCULATEUR ---
elif "Calcul" in menu:
    st.header("💰 Calculateur de Soldes Élite")
    c1, c2 = st.columns(2)
    p_ini = c1.number_input("Prix d'achat (€)", min_value=0.0, value=100.0)
    p_rem = c2.slider("Réduction (%)", 0, 100, 20)
    final = p_ini * (1 - p_rem/100)
    st.metric("PRIX FINAL GIVRÉ", f"{final} €", delta=f"-{(p_ini*p_rem)/100} €", delta_color="inverse")
    st.info(f"✍️ Formule : {p_ini} . ({p_rem}/100) = {final} €")

# --- PAGE MATHS ---
elif "Math" in menu or "Mates" in menu:
    st.header("📐 Zone Mathématique 1CA")
    st.subheader("✖️ Produit en Croix")
    ma, mb, mc = st.columns(3)
    a_v = ma.number_input("Valeur A", value=1.0)
    b_v = mb.number_input("Valeur B", value=10.0)
    c_v = mc.number_input("Valeur C", value=5.0)
    if a_v != 0: st.success(f"Résultat : {(b_v * c_v) / a_v}")
    st.write("---")
    st.subheader("🏖️ Compte à rebours Vacances")
    v_reste = datetime(2026, 7, 1) - datetime.now()
    st.metric("Jours restants", f"{v_reste.days} Jours")

# --- PAGE ENCYCLOPÉDIE ---
elif "Ency" in menu:
    st.header("📚 Encyclopédie du Codage")
    st.write("### 🤖 C'est quoi le codage ?")
    st.write("C'est donner des ordres à une machine. Comme une recette : si tu oublies une étape, le programme bug !")
    st.write("### 🧱 Les 3 piliers :")
    st.markdown("- **Variables** : La mémoire.\n- **Conditions** : L'intelligence.\n- **Boucles** : La répétition.")
    st.video("https://youtube.com")

# --- PAGE MISSION CODE ---
elif "Mission" in menu:
    st.header("🎮 Mission : Répare le Bug")
    st.code('print(Hello 1CA)')
    repa = st.text_input("Répare la ligne :")
    if repa == 'print("Hello 1CA")': 
        st.balloons()
        st.success("✅ ACCÈS ACCORDÉ !")

# --- PAGE DUEL ---
elif "Duel" in menu:
    st.header("⚔️ Duel : Hacker vs Hacker")
    st.write(f"🏆 Score : H1 [{st.session_state.score_multi['H1']}] | H2 [{st.session_state.score_multi['H2']}]")
    cp1, cp2 = st.columns(2)
    h1_g = cp1.number_input("Hacker 1 (1-20)", 1, 20, key="h1")
    if cp1.button("Tester H1"):
        if h1_g == st.session_state.code_secret:
            st.session_state.score_multi['H1'] += 1; st.balloons(); st.success("H1 GAGNE !"); st.session_state.code_secret = random.randint(1, 20)
    h2_g = cp2.number_input("Hacker 2 (1-20)", 1, 20, key="h2")
    if cp2.button("Tester H2"):
        if h2_g == st.session_state.code_secret:
            st.session_state.score_multi['H2'] += 1; st.balloons(); st.success("H2 GAGNE !"); st.session_state.code_secret = random.randint(1, 20)

# --- PAGE ESPACE ---
elif "Espace" in menu or "Espacio" in menu:
    st.header("🪐 Gravité dans le Givre")
    pds = st.number_input("Ton poids (kg)", value=50.0)
    st.write(f"Sur Mars : {pds * 0.37} kg | Sur la Lune : {pds * 0.16} kg")

# --- PAGE MATRIX ---
elif "Matrix" in menu:
    st.header("🟢 Infiltration Glacée")
    if st.button("LANCER LE SCAN"):
        st.code("\n".join(["".join([random.choice("01") for _ in range(40)]) for _ in range(8)]))

# --- PAGE TERMINAL ---
elif "Terminal" in menu:
    st.header("🕒 Terminal de Bord")
    st.write(f"Heure actuelle : **{datetime.now().strftime('%H:%M:%S')}**")
    st.text_area("Journal de mission :", "L'iPad de l'école est sous contrôle...")
