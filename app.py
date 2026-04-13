import streamlit as st
import random
from datetime import datetime

# 1. CONFIGURATION
st.set_page_config(page_title="Hacker Cosmic Academy", page_icon="👾", layout="wide")

# 2. DESIGN NÉON & GALAXIE
st.markdown("""
    <style>
    .stApp { background: radial-gradient(ellipse at bottom, #1B2735 0%, #090A0F 100%); color: white; }
    h1 { color: #FF00FF !important; text-shadow: 0 0 15px #FF00FF; text-align: center; }
    h2, h3, label, p, span { color: #00FFFF !important; text-shadow: 0 0 8px #00FFFF; }
    .stMetric div { color: #39FF14 !important; }
    img { border-radius: 50%; border: 4px solid #FF00FF; box-shadow: 0 0 20px #FF00FF; }
    [data-testid="stSidebar"] { background-color: rgba(10, 10, 30, 0.9); border-right: 3px solid #00FFFF; }
    </style>
    """, unsafe_allow_html=True)

# 3. MENU SIDEBAR (Signé Règne)
with st.sidebar:
    st.markdown('<p style="color:#FF00FF; font-weight:bold; border:2px solid #FF00FF; padding:10px; border-radius:15px; text-align:center;">👑 CRÉATEUR : RÈGNE</p>', unsafe_allow_html=True)
    st.title("🛰️ Navigation")
    menu = st.radio("Navigation :", ["💰 Calculateur", "📐 Zone Maths", "📚 Exposé Codage", "🎮 Mission : Codeur", "💎 Gamer Tool"])
    st.write("---")
    st.caption("🚀 Hacker Cosmic v9.0 | By Règne")

# 4. EN-TÊTE
col1, col2 = st.columns(2)
with col1: st.image("IMG_0956.png", width=200)
with col2:
    st.title("HACKER COSMIC 1CA")
    st.components.v1.html("""
        <script>function parler(){var m=new SpeechSynthesisUtterance("Initialisation du module éducatif. Prêt pour l'exposé, Maître Règne ?");m.lang='fr-FR';window.speechSynthesis.speak(m);}</script>
        <button onclick="parler()" style="background-color:transparent; color:#FF00FF; border:2px solid #FF00FF; padding:10px; border-radius:15px; cursor:pointer; font-weight:bold; width: 100%;">🔈 LANCER LA SESSION</button>
    """, height=70)

# 5. LOGIQUE DES PAGES
if menu == "💰 Calculateur":
    st.header("💰 Calculateur de Soldes")
    c1, c2 = st.columns(2)
    pi = c1.number_input("Prix (€)", value=100.0)
    re = c2.slider("Réduction (%)", 0, 100, 20)
    st.metric("Prix Final", f"{pi * (1 - re/100)} €")

elif menu == "📐 Zone Maths":
    st.header("📐 Zone Mathématiques")
    st.write("### Produit en Croix")
    ma, mb, mc = st.columns(3)
    res = (mb.number_input("B", value=10.0) * mc.number_input("C", value=5.0)) / ma.number_input("A", value=1.0)
    st.success(f"Résultat : **{res}**")

elif menu == "📚 Exposé Codage":
    st.header("📚 L'Essentiel du Codage")
    st.write("""
    ### 🤖 1. C'est quoi le codage ?
    Imagine que tu veux commander un robot pour qu'il te prépare un **chocolat chaud**. Tu ne peux pas lui dire simplement "fais-moi un chocolat". Il faut lui donner des **étapes ultra précises** : 
    1. Prends une tasse. 
    2. Verse le lait. 
    3. Ajoute le cacao.
    
    **Le codage, c'est ça :** c'est une liste d'instructions pour l'ordinateur.
    
    ### 🔢 2. Le langage des machines
    L'ordinateur ne connaît que le **Binaire** (des 0 et des 1). Python est le traducteur magique entre ton cerveau et la machine.
    
    ### 🧱 3. Les trois briques du Hacker
    *   **Les Variables :** La mémoire (ton score, ton nom).
    *   **Les Conditions (IF) :** L'intelligence (SI le code est bon ALORS ouvre).
    *   **Les Boucles :** La répétition rapide.
    
    ### 🚀 4. Pourquoi apprendre ?
    Le code est partout : iPad, fusées de SpaceX, jeux vidéo. Apprendre à coder, c'est **créer le futur** !
    """)
    st.info("💡 **Conseil :** Faire des erreurs (bugs) est normal. Les réparer, c'est ça être un pro !")

elif menu == "🎮 Mission : Codeur":
    st.header("👾 Mission : Répare le Bug")
    st.write("Trouve l'erreur pour infiltrer le système !")
    st.code('print(Hello World)')
    rep = st.text_input("Répare le code (ajoute les guillemets) :")
    if st.button("Vérifier"):
        if rep == 'print("Hello World")':
            st.balloons(); st.success("✅ ACCÈS AUTORISÉ !")

elif menu == "💎 Gamer Tool":
    st.header("💎 Gamer Zone")
    eu = st.number_input("Montant (€)", value=10)
    st.write(f"💎 **Robux :** {int(eu*80)} | 🔥 **V-Bucks :** {int(eu*110)}")
