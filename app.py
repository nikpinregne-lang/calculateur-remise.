import streamlit as st
import random
from datetime import datetime
import time

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

# 3. MENU SIDEBAR
with st.sidebar:
    st.markdown('<p style="color:#FF00FF; font-weight:bold; border:2px solid #FF00FF; padding:10px; border-radius:15px; text-align:center;">👑 CRÉATEUR : RÈGNE</p>', unsafe_allow_html=True)
    st.title("🛰️ Navigation")
    menu = st.radio("Navigation :", ["💰 Calculateur", "📐 Zone Maths", "📚 Exposé Codage", "🎮 Mission : Codeur", "💎 Gamer Tool"])
    st.write("---")
    st.caption("🚀 Hacker Cosmic v8.0 | By Règne")

# 4. EN-TÊTE
col1, col2 = st.columns(2)
with col1: st.image("IMG_0956.png", width=200)
with col2:
    st.title("HACKER COSMIC 1CA")
    st.components.v1.html("""
        <script>function parler(){var m=new SpeechSynthesisUtterance("Alerte ! Système corrompu. Réparez le code pour entrer, Maître Règne.");m.lang='fr-FR';window.speechSynthesis.speak(m);}</script>
        <button onclick="parler()" style="background-color:transparent; color:#FF00FF; border:2px solid #FF00FF; padding:10px; border-radius:15px; cursor:pointer; font-weight:bold; width: 100%;">🔈 LANCER LA MISSION</button>
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
    st.header("📚 L'essentiel du Code")
    st.write("Le codage est le langage des machines. Apprends les bases pour devenir un pro !")

elif menu == "🎮 Mission : Codeur":
    st.header("👾 Mission de Hacking : Répare le Bug")
    st.write("Un virus a cassé le code. Trouve l'erreur pour débloquer le système !")

    # --- NIVEAU 1 ---
    st.subheader("Niveau 1 : L'Oubli de Texte")
    st.code('print(Hello World)')
    reponse1 = st.text_input("Réparer la ligne (indice : ajoute les guillemets) :")
    if st.button("Vérifier Niveau 1"):
        if reponse1 == 'print("Hello World")' or reponse1 == "print('Hello World')":
            st.success("✅ ACCÈS NIVEAU 1 AUTORISÉ !")
        else:
            st.error("❌ ERREUR SYNTAXE. Réessaie !")

    # --- NIVEAU 2 ---
    st.write("---")
    st.subheader("Niveau 2 : Le Calcul Mystère")
    st.write("Quelle est la valeur finale de `X` dans ce code ?")
    st.code("""
    A = 5
    B = 3
    X = A * B
    """)
    reponse2 = st.text_input("Valeur de X :")
    if st.button("Vérifier Niveau 2"):
        if reponse2 == "15":
            st.success("✅ CONNEXION RÉTABLIE !")
        else:
            st.error("❌ CALCUL INCORRECT. L'ordinateur ne se trompe jamais...")

    # --- NIVEAU 3 ---
    st.write("---")
    st.subheader("Niveau 3 : La Condition Fatale")
    st.write("Si `score = 10`, est-ce que ce code va afficher 'Gagné' ?")
    st.code("""
    score = 10
    if score > 20:
        print("Gagné")
    else:
        print("Perdu")
    """)
    reponse3 = st.radio("L'écran va afficher :", ["Gagné", "Perdu"])
    if st.button("Vérifier Niveau 3"):
        if reponse3 == "Perdu":
            st.balloons()
            st.success("🏆 FÉLICITATIONS HACKER ! Système infiltré avec succès.")
        else:
            st.error("❌ RÉPONSE FAUSSE. Observe bien le signe '>' !")

elif menu == "💎 Gamer Tool":
    st.header("💎 Gamer Zone")
    eu = st.number_input("Montant (€)", value=10)
    st.write(f"💎 **Robux :** {int(eu*80)} | 🔥 **V-Bucks :** {int(eu*110)}")
