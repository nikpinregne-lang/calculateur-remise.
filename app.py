import streamlit as st
import random
from datetime import datetime

# 1. CONFIGURATION
st.set_page_config(page_title="Hacker Cosmic IA", page_icon="🤖", layout="wide")

# 2. DESIGN NÉON & GALAXIE
st.markdown("""
    <style>
    .stApp { background: radial-gradient(ellipse at bottom, #1B2735 0%, #050505 100%); color: white; }
    h1 { color: #FF00FF !important; text-shadow: 0 0 20px #FF00FF; text-align: center; font-family: 'Orbitron', sans-serif; }
    h2, h3, label, p, span { color: #00FFFF !important; text-shadow: 0 0 10px #00FFFF; }
    .stMetric div { color: #39FF14 !important; }
    [data-testid="stSidebar"] { background-color: #000000 !important; border-right: 2px solid #FF00FF; }
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    st.markdown('<p style="color:#FF00FF; font-weight:bold; border:2px solid #FF00FF; padding:10px; border-radius:15px; text-align:center;">👑 CRÉATEUR : RÈGNE</p>', unsafe_allow_html=True)
    st.title("🛰️ Système")
    menu = st.radio("Navigation :", ["💰 Calculateur", "🤖 IA Chatbots", "📚 Exposé Code", "🔐 Labo Crypto", "🎮 Duel Multi", "🟢 Matrix"])
    st.write("---")
    st.caption("🚀 Hacker Cosmic 2026 | v19.0")

# 4. EN-TÊTE
c1, c2 = st.columns(2)
with c1: st.image("IMG_0956.png", width=200)
with c2:
    st.title("HACKER COSMIC 1CA 2026")
    st.components.v1.html("""
        <script>function parler(){var m=new SpeechSynthesisUtterance("Double intelligence artificielle activée. Maître Règne, les cerveaux sont prêts.");m.lang='fr-FR';window.speechSynthesis.speak(m);}</script>
        <button onclick="parler()" style="background-color:transparent; color:#FF00FF; border:2px solid #FF00FF; padding:10px; border-radius:15px; cursor:pointer; font-weight:bold; width:100%;">🔈 INITIALISER LES IA</button>
    """, height=70)

# 5. PAGES
if menu == "🤖 IA Chatbots":
    st.header("🤖 Centre de Recherche IA")
    tab1, tab2 = st.tabs(["🌌 IA Cosmique (Générale)", "🐍 IA Master-Code (Spécialiste)"])

    with tab1:
        st.subheader("Discute avec l'IA du système")
        user_q = st.text_input("Pose une question (ex: Qui es-tu ?, Salut, Quel jour ?) :", key="gen")
        if st.button("Envoyer à l'IA Cosmique"):
            responses = {
                "salut": "Salut à toi, jeune Hacker de la 1CA !",
                "qui es-tu ?": "Je suis l'IA de bord créée par le Maître Règne.",
                "quel jour ?": f"Nous sommes le {datetime.now().strftime('%d/%m/%Y')}.",
                "aide": "Utilise le menu à gauche pour explorer mes modules.",
                "recompense": "Tiens, un cadeau ! 🎁"
            }
            res = responses.get(user_q.lower(), "Analyse en cours... Je ne connais pas encore la réponse à tout, mais j'apprends !")
            st.chat_message("assistant").write(res)

    with tab2:
        st.subheader("Pose tes questions de codage")
        code_q = st.text_input("Question technique (ex: Python, Variable, Bug, If) :", key="code")
        if st.button("Demander au Spécialiste"):
            coding_responses = {
                "python": "C'est le langage de ce site ! Il est super puissant pour l'IA.",
                "variable": "Une variable est une boîte pour stocker des données (ex: score = 10).",
                "bug": "Un bug est une erreur dans le code. Les réparer fait de toi un pro !",
                "if": "Le 'IF' est une condition. Il permet à l'ordi de faire des choix.",
                "print": "La fonction print() sert à afficher du texte sur l'écran."
            }
            res = coding_responses.get(code_q.lower(), "Désolé, je ne parle que de codage. Pour le reste, demande à l'IA Cosmique !")
            st.chat_message("assistant").write(f"🐍 **Master-Code dit :** {res}")

elif menu == "💰 Calculateur":
    st.header("💰 Calculateur de Soldes")
    pi = st.number_input("Prix (€)", value=100.0)
    re = st.slider("Réduction (%)", 0, 100, 20)
    st.metric("Prix Final", f"{pi*(1-re/100)} €")

elif menu == "📚 Exposé Code":
    st.header("📚 L'Encyclopédie du Code")
    st.write("Le codage est l'art de parler aux machines.")
    url_v = "https://youtube.com"
    st.video(url_v)
    st.link_button("🚀 Ouvrir la vidéo proprement", url_v)

elif menu == "🔐 Labo Crypto":
    st.header("🔐 Labo de Cryptage")
    msg = st.text_input("Message à crypter :", "HACKER")
    st.code(f"Code : {msg.upper()[::-1]}") # Inversion simple pour l'exemple

elif menu == "🟢 Matrix":
    if st.button("RUN"):
        st.code("\n".join(["".join([random.choice("01") for _ in range(40)]) for _ in range(5)]))
