import streamlit as st
import random
import time

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="Hacker Cosmic App", page_icon="🚀", layout="wide")

# 2. STYLE NÉON & GALAXIE (Le design complet)
st.markdown("""
    <style>
    /* Fond galaxie animé */
    .stApp {
        background: radial-gradient(ellipse at bottom, #1B2735 0%, #090A0F 100%);
        color: white;
    }
    @keyframes move-twinkle-back {
        from {background-position:0 0;}
        to {background-position:-10000px 5000px;}
    }
    .stApp::before {
        content: ""; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
        background: transparent url('https://transparenttextures.com') repeat;
        z-index: -1; opacity: 0.4; animation: move-twinkle-back 200s linear infinite;
    }
    /* Effets Néon */
    h1 { color: #FF00FF !important; text-shadow: 0 0 15px #FF00FF, 0 0 30px #FF00FF; text-align: center; }
    h2, h3, label, p, span { color: #00FFFF !important; text-shadow: 0 0 5px #00FFFF; }
    .stMetric div { color: #39FF14 !important; text-shadow: 0 0 10px #39FF14; }
    
    /* Logo brillant */
    img { 
        border-radius: 20px; border: 3px solid #00FFFF; 
        box-shadow: 0 0 20px #00FFFF; transition: 0.4s; 
    }
    img:hover { transform: scale(1.05) rotate(2deg); }

    /* Sidebar stylée */
    [data-testid="stSidebar"] {
        background-color: rgba(0, 15, 15, 0.9);
        border-right: 2px solid #00FFFF;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRE LATÉRALE (SIDEBAR) - Améliorée
with st.sidebar:
    st.markdown('<p style="color:#39FF14; font-weight:bold; border:2px solid #39FF14; padding:10px; border-radius:15px; text-align:center; box-shadow: 0 0 10px #39FF14;">🟢 SYSTEM ONLINE</p>', unsafe_allow_html=True)
    st.title("🛰️ Navigation")
    menu = st.radio("Outils disponibles :", ["💰 Calculateur", "📐 Zone Maths", "🎮 Défi Jeu", "💎 Gamer Tool", "🔐 Sécurité"])
    
    st.write("---")
    st.subheader("🎵 Ambiance")
    # Petite vidéo lo-fi pour l'ambiance
    st.video("https://youtube.com")
    
    st.write("---")
    st.caption("🚀 Développé par Hacker Cosmic | 2026")
    st.markdown("[🔗 Partager le site](https://streamlit.app)")

# 4. EN-TÊTE DU SITE (LOGO + TITRE + VOIX)
col_header1, col_header2 = st.columns([1, 2])
with col_header1:
    st.image("IMG_0956.png")
with col_header2:
    st.title("HACKER COSMIC 1CA")
    st.components.v1.html("""
        <script>
            function parler() {
                var m = new SpeechSynthesisUtterance("Accès autorisé. Bienvenue dans la base de données du Hacker Cosmic.");
                m.lang = 'fr-FR'; m.pitch = 1.1; window.speechSynthesis.speak(m);
            }
        </script>
        <button onclick="parler()" style="background-color:transparent; color:#00FFFF; border:2px solid #00FFFF; padding:10px 20px; border-radius:15px; cursor:pointer; font-weight:bold; box-shadow: 0 0 10px #00FFFF;">
            🔈 ACTIVER L'IA VOCALE
        </button>
    """, height=70)

# 5. LOGIQUE DES PAGES
if menu == "💰 Calculateur":
    st.header("💰 Calculateur de Soldes de Pro")
    ca, cb = st.columns(2)
    with ca:
        prix_i = st.number_input("Prix d'origine (€)", min_value=0.0, value=100.0)
    with cb:
        remise_p = st.slider("Réduction souhaitée (%)", 0, 100, 20)
    
    montant_r = (prix_i * remise_p) / 100
    prix_f = prix_i - montant_r
    
    st.metric("Prix Final", f"{prix_f} €", delta=f"-{montant_r} €", delta_color="inverse")
    
    # Détail pour le prof de math
    st.info(f"✍️ **Détail du calcul :** {prix_i} € - ({prix_i} € $\cdot$ {remise_p}/100) = {prix_f} €")

elif menu == "📐 Zone Maths":
    st.header("📐 Assistant Mathématiques (Spécial Prof)")
    outil_math = st.selectbox("Choisis ton outil :", ["Géométrie", "Produit en Croix", "Nombre Premier"])
    
    if outil_math == "Géométrie":
        f = st.selectbox("Forme :", ["Rectangle", "Triangle", "Cercle"])
        if f == "Rectangle":
            L = st.number_input("Longueur (L)", value=10.0)
            l = st.number_input("Largeur (l)", value=5.0)
            st.write("**Formule :** $L \cdot l$")
            st.success(f"Aire du rectangle = **{L*l}**")
        elif f == "Triangle":
            b = st.number_input("Base (b)", value=10.0)
            h = st.number_input("Hauteur (h)", value=5.0)
            st.write("**Formule :** $(b \cdot h) / 2$")
            st.success(f"Aire du triangle = **{(b*h)/2}**")
            
    elif outil_math == "Produit en Croix":
        st.write("Si **A** $\\rightarrow$ **B**, alors **C** $\\rightarrow$ **?**")
        ma, mb, mc = st.columns(3)
        with ma: val_a = st.number_input("A", value=1.0)
        with mb: val_b = st.number_input("B", value=10.0)
        with mc: val_c = st.number_input("C", value=5.0)
        st.success(f"Résultat : **{(val_b * val_c) / val_a}**")

elif menu == "🎮 Défi Jeu":
    st.header("🎮 Mission : Le Juste Prix")
    if 'score' not in st.session_state: st.session_state.score = 0
    if 'best' not in st.session_state: st.session_state.best = 0
    if 'cible' not in st.session_state: st.session_state.cible = 25.0

    col_score1, col_score2 = st.columns(2)
    with col_score1: st.metric("🏆 Score Actuel", st.session_state.score)
    with col_score2: st.metric("🥇 Record Personnel", st.session_state.best)
    
    st.warning(f"🎯 **Objectif :** Trouve la réduction pour arriver pile à **{st.session_state.cible} €**")
    
    if st.button("🎲 GÉNÉRER UN NOUVEAU DÉFI"):
        st.session_state.cible = float(random.randint(10, 85))
        st.session_state.gagne = False
        st.rerun()

    p_j = st.slider("Ajuste la remise (sur base 100€)", 0, 100, 50)
    test_j = round(100 * (1 - p_j/100), 2)
    st.write(f"💵 Ton test : **{test_j} €**")
    
    if test_j == st.session_state.cible:
        if not st.session_state.get('gagne', False):
            st.session_state.score += 1
            st.session_state.gagne = True
            if st.session_state.score > st.session_state.best:
                st.session_state.best = st.session_state.score
        st.balloons()
        st.success(f"🏆 COMPTE EST BON ! Score : {st.session_state.score}")

elif menu == "💎 Gamer Tool":
    st.header("💎 Convertisseur de Monnaie Virtuelle")
    montant_eu = st.number_input("Montant en Euros (€)", min_value=0, value=10)
    g1, g2 = st.columns(2)
    with g1: st.metric("💎 Robux", int(montant_eu * 80))
    with g2: st.metric("🔥 V-Bucks", int(montant_eu * 110))

elif menu == "🔐 Sécurité":
    st.header("🔐 Outils de Hacker")
    long = st.slider("Longueur du mot de passe", 8, 30, 12)
    if st.button("🚀 GÉNÉRER UN MOT DE PASSE"):
        carac = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
        mdp = "".join(random.sample(carac, long))
        st.code(mdp)
        st.success("Mot de passe crypté généré !")
