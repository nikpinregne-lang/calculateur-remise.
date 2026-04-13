import streamlit as st
import random

# 1. Configuration de la page
st.set_page_config(page_title="Hacker Cosmic Calc", page_icon="💰")

# 2. Style Néon et Étoiles (CSS)
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(ellipse at bottom, #1B2735 0%, #090A0F 100%);
        color: white;
    }
    @keyframes move-twinkle-back {
        from {background-position:0 0;}
        to {background-position:-10000px 5000px;}
    }
    .stApp::before {
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: transparent url('https://transparenttextures.com') repeat;
        z-index: -1;
        opacity: 0.4;
        animation: move-twinkle-back 200s linear infinite;
    }
    h1 { color: #FF00FF !important; text-shadow: 0 0 10px #FF00FF; }
    h2, h3, label, p, span { color: #00FFFF !important; text-shadow: 0 0 5px #00FFFF; }
    .stMetric div { color: #39FF14 !important; text-shadow: 0 0 10px #39FF14; }
    img { border-radius: 20px; border: 3px solid #00FFFF; box-shadow: 0 0 20px #00FFFF; }
    </style>
    """, unsafe_allow_html=True)

# 3. En-tête (Logo + Titre + Voix)
col1, col2 = st.columns([1, 2])
with col1:
    st.image("IMG_0956.png")
with col2:
    st.title("Hacker Cosmic 1CA")
    st.components.v1.html("""
        <script>
            function parler() {
                var msg = new SpeechSynthesisUtterance("Bienvenue sur le site du Hacker Cosmic !");
                msg.lang = 'fr-FR'; window.speechSynthesis.speak(msg);
            }
        </script>
        <button onclick="parler()" style="background-color: #00BFFF; color: white; border: none; padding: 10px; border-radius: 5px; cursor: pointer; font-weight: bold;">
            🔈 Activer la voix
        </button>
    """, height=60)

# 4. Menu Sidebar
with st.sidebar:
    st.title("🚀 Menu")
    menu = st.radio("Aller vers :", ["💰 Calculateur", "📐 Maths & Géo", "🎮 Défi Jeu", "💎 Gamer"])
    st.write("---")
    st.caption("Créé par le Hacker Cosmic 2026")

# 5. Logique des pages
if menu == "💰 Calculateur":
    st.header("💰 Calculateur de Soldes")
    c1, c2 = st.columns(2)
    with c1:
        prix_i = st.number_input("Prix (€)", min_value=0.0, value=100.0)
    with c2:
        remise_p = st.slider("Réduction (%)", 0, 100, 20)
    
    montant_r = (prix_i * remise_p) / 100
    prix_f = prix_i - montant_r
    st.metric("Prix Final", f"{prix_f} €", delta=f"-{montant_r} €", delta_color="inverse")

elif menu == "📐 Maths & Géo":
    st.header("📐 Espace Mathématiques")
    forme = st.selectbox("Forme :", ["Rectangle", "Triangle", "Cercle"])
    if forme == "Rectangle":
        L = st.number_input("Longueur (L)", value=10.0); l = st.number_input("Largeur (l)", value=5.0)
        st.write(f"**Formule :** $L \cdot l$")
        st.success(f"Aire = {L * l}")
    elif forme == "Triangle":
        b = st.number_input("Base (b)", value=10.0); h = st.number_input("Hauteur (h)", value=5.0)
        st.write(f"**Formule :** $(b \cdot h) / 2$")
        st.success(f"Aire = {(b * h) / 2}")

elif menu == "🎮 Défi Jeu":
    st.header("🎮 Le Défi du Hacker")
    if 'score' not in st.session_state: st.session_state.score = 0
    if 'cible' not in st.session_state: st.session_state.cible = 25.0
    
    st.info(f"🏆 Score : {st.session_state.score} | Cible : {st.session_state.cible} €")
    if st.button("🎲 Nouveau défi"):
        st.session_state.cible = float(random.randint(10, 80))
        st.session_state.gagne = False
        st.rerun()

    p_jeu = st.slider("Ajuste la remise !", 0, 100, 10)
    test_jeu = round(100 * (1 - p_jeu / 100), 2)
    st.write(f"💵 Ton test (sur base 100€) : **{test_jeu} €**")
    
    if test_jeu == st.session_state.cible:
        if not st.session_state.get('gagne', False):
            st.session_state.score += 1; st.session_state.gagne = True
        st.balloons(); st.success("🏆 COMPTE EST BON !")

elif menu == "💎 Gamer":
    st.header("💎 Convertisseur Gamer")
    euros = st.number_input("Montant (€)", value=10.0)
    st.write(f"💎 **Robux :** {int(euros * 80)}")
    st.write(f"🔥 **V-Bucks :** {int(euros * 110)}")
