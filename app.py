import streamlit as st
import random
from datetime import datetime
import time

# 1. CONFIGURATION
st.set_page_config(page_title="Hacker Cosmic Ultimate", page_icon="🧠", layout="wide")

# 2. DESIGN NÉON & GALAXIE SUPRÊME
st.markdown("""
    <style>
    .stApp { background: radial-gradient(ellipse at bottom, #1B2735 0%, #050505 100%); color: white; }
    h1 { color: #FF00FF !important; text-shadow: 0 0 20px #FF00FF; text-align: center; font-family: 'Orbitron', sans-serif; }
    h2, h3, label, p, span { color: #00FFFF !important; text-shadow: 0 0 10px #00FFFF; }
    .stMetric div { color: #39FF14 !important; }
    img { border-radius: 50%; border: 3px solid #00FFFF; box-shadow: 0 0 25px #00FFFF; }
    [data-testid="stSidebar"] { background-color: #000000 !important; border-right: 2px solid #FF00FF; }
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR : TABLEAU DE BORD EN DIRECT
with st.sidebar:
    st.markdown('<p style="color:#39FF14; font-weight:bold; border:1px solid #39FF14; padding:10px; border-radius:15px; text-align:center;">🟢 SYSTÈME : ONLINE</p>', unsafe_allow_html=True)
    st.write(f"📅 **Date :** {datetime.now().strftime('%d/%m/%Y')}")
    st.write(f"📡 **Signal :** {random.randint(94, 99)}% (Stable)")
    st.write("---")
    menu = st.radio("Poste de Contrôle :", ["🤖 IA Intelligente", "💰 Calculateur Pro", "📐 Zone Scolaire", "🎮 Mission Solo", "⚔️ Duel Multi", "📚 Encyclopédie"])
    st.write("---")
    st.caption("🚀 Créé par RÈGNE | 1CA 2026")

# 4. EN-TÊTE
col1, col2 = st.columns(2)
with col1: st.image("IMG_0956.png", width=200)
with col2:
    st.title("HACKER COSMIC 1CA 2026")
    st.components.v1.html("""
        <script>function parler(){var m=new SpeechSynthesisUtterance("Intelligence artificielle v20 activée. Je suis prête à t'aider, Maître Règne.");m.lang='fr-FR';window.speechSynthesis.speak(m);}</script>
        <button onclick="parler()" style="background-color:transparent; color:#FF00FF; border:2px solid #FF00FF; padding:10px; border-radius:15px; cursor:pointer; font-weight:bold; width:100%;">🔈 INITIALISER L'IA</button>
    """, height=70)

# 5. LOGIQUE DES PAGES

if menu == "🤖 IA Intelligente":
    st.header("🤖 Centre de Recherche IA (Smarter)")
    user_q = st.text_input("Pose une question (météo, maths, code, salut...) :").lower()
    
    if st.button("Interroger l'IA"):
        if "salut" in user_q or "bonjour" in user_q:
            res = "Salut Hacker ! Mes circuits sont prêts pour l'action. ⚡"
        elif "qui es-tu" in user_q or "nom" in user_q:
            res = "Je suis l'IA Cosmique, le second cerveau de Maître Règne. 👑"
        elif "math" in user_q or "calcul" in user_q:
            res = "Les maths sont ma spécialité. Utilise la Zone Scolaire pour le produit en croix ! 📐"
        elif "meteo" in user_q or "temps" in user_q:
            res = "🛰️ Satellite : Grand soleil détecté sur ta base secrète à Bruxelles."
        elif "secret" in user_q:
            res = "🔓 ACCÈS SECRET : Tape '1CA_PEAK' pour voir ce qui se passe..."
        elif "1ca_peak" in user_q:
            st.balloons()
            res = "🏆 Tu as trouvé le code secret ! Tu es le roi de la 1CA !"
        else:
            res = "🔍 Analyse... Je n'ai pas encore de réponse précise, mais je demande à Maître Règne !"
        st.chat_message("assistant").write(res)

elif menu == "💰 Calculateur Pro":
    st.header("💰 Calculateur de Soldes")
    pi = st.number_input("Prix (€)", value=100.0)
    re = st.slider("Réduction (%)", 0, 100, 20)
    rf = pi * (1 - re/100)
    st.metric("Prix Final", f"{rf} €", delta=f"-{(pi*re)/100} €")
    st.info(f"✍️ **Détail :** {pi} € $\cdot$ ({re}/100) = {rf} €")

elif menu == "📐 Zone Scolaire":
    st.header("📐 Boîte à Outils 1CA")
    outil = st.selectbox("Choisir un outil :", ["Produit en Croix", "Convertisseur d'unités"])
    if outil == "Produit en Croix":
        ma, mb, mc = st.columns(3)
        res = (mb.number_input("Si A donne B", value=10.0) * mc.number_input("C donne ?", value=5.0)) / ma.number_input("Valeur A", value=1.0)
        st.success(f"Résultat : **{res}**")
    else:
        val = st.number_input("Valeur à convertir :", value=1.0)
        u = st.selectbox("Vers :", ["Km en Mètres", "Litres en ml", "Kg en Grammes"])
        if "Mètres" in u: st.success(f"{val*1000} m")
        elif "ml" in u: st.success(f"{val*1000} ml")
        else: st.success(f"{val*1000} g")

elif menu == "🎮 Mission Solo":
    st.header("👾 Répare le Bug")
    st.code('print(Hello World)')
    rep = st.text_input("Répare (guillemets) :")
    if rep == 'print("Hello World")': st.balloons(); st.success("ACCÈS AUTORISÉ !")

elif menu == "⚔️ Duel Multi":
    st.header("⚔️ Duel 1 vs 1")
    if 's' not in st.session_state: st.session_state.s = random.randint(1, 10)
    g = st.number_input("Devine (1-10) :", 1, 10)
    if st.button("Vérifier"):
        if g == st.session_state.s: 
            st.balloons(); st.success("GAGNÉ ! Nouveau code généré."); st.session_state.s = random.randint(1, 10)
        else: st.error("NON !")

elif menu == "📚 Encyclopédie":
    st.header("📚 L'Essentiel du Codage")
    st.write("Le codage est le langage des machines. Apprends-le pour créer le futur !")
