
import streamlit as st
import random

# 1. Configuration de la page
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="centered")

# --- BARRE LATÉRALE : CHATBOT ---
with st.sidebar:
    st.title("🤖 Chatbot 1CA")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Pose-moi une question..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        reponse = f"Salut, c'est l'IA Hacker Cosmic. Tu as dit : '{prompt}'. Je suis là pour t'aider avec IEEM !"
        with st.chat_message("assistant"):
            st.markdown(reponse)
        st.session_state.messages.append({"role": "assistant", "content": reponse})

# --- CORPS PRINCIPAL : CALCULATEUR ---

# Utilisation du fichier exact vu sur ta capture d'écran
try:
    st.image("IMG_0956.png", width=250)
except:
    st.error("⚠️ Fichier 'IMG_0956.png' introuvable. Vérifie qu'il est bien à côté de ton fichier app.py sur GitHub.")

st.title("Mon calculateur de réduction Hacker Cosmic 1CA 2026")
st.write("Créé par **IEEM**")
st.write("---")

prix_origine = st.number_input("Prix d'origine (€)", min_value=0.0, value=100.0, step=0.01)
reduction = st.number_input("Réduction (%)", min_value=0.0, max_value=100.0, value=10.0, step=0.1)

st.header("Prix après réduction")
prix_final = prix_origine * (1 - reduction / 100)
st.subheader(f"{prix_final:.2f} €")

st.write("---")

# --- SECTION : EXERCICE INFINI ---
st.header("📝 Exercice infini")

# Initialisation d'un exercice si vide
if 'exo_prix' not in st.session_state:
    st.session_state.exo_prix = random.randint(10, 500)
    st.session_state.exo_remise = random.randint(5, 75)
    st.session_state.reponse_correcte = st.session_state.exo_prix * (1 - st.session_state.exo_remise / 100)

st.write(f"**Énoncé :** Un produit coûte **{st.session_state.exo_prix} €**.")
st.write(f"On applique une remise de **{st.session_state.exo_remise} %**.")

user_ans = st.number_input("Quel est le prix final ?", key="user_ans", value=0.0)

col_check, col_new = st.columns(2)

with col_check:
    if st.button("Vérifier"):
        if abs(user_ans - st.session_state.reponse_correcte) < 0.05:
            st.success(f"✅ Bravo ! C'est bien {st.session_state.reponse_correcte:.2f} €")
        else:
            st.error("❌ Faux, réessaye !")

with col_new:
    if st.button("Nouvel exercice 🔄"):
        if 'exo_prix' in st.session_state:
            del st.session_state['exo_prix']
        st.rerun()
