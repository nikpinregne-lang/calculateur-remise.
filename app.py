import streamlit as st
import random

# 1. Configuration (Garde le style blanc par défaut de Streamlit)
st.set_page_config(page_title="Hacker Cosmic 1CA", layout="centered")

# --- BARRE LATÉRALE : CHATBOT ---
with st.sidebar:
    st.title("🤖 Chatbot 1CA")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Affichage des messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Entrée utilisateur
    if prompt := st.chat_input("Pose-moi une question..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Réponse simple (tu peux la personnaliser)
        reponse = f"Je suis l'IA Hacker Cosmic. Tu as dit : '{prompt}'. Comment puis-je t'aider en maths ?"
        with st.chat_message("assistant"):
            st.markdown(reponse)
        st.session_state.messages.append({"role": "assistant", "content": reponse})

# --- CORPS PRINCIPAL : CALCULATEUR (Ton code actuel) ---
# (Remplace 'logo.png' par ton lien d'image si besoin)
st.image("https://streamlit.io", width=100) # Remets ton logo ici
st.title("Mon calculateur de réduction Hacker Cosmic 1CA")
st.write("Créé par **RÈGNE**")
st.write("---")

prix_origine = st.number_input("Prix d'origine (€)", min_value=0.0, value=100.0, step=0.01)
reduction = st.number_input("Réduction (%)", min_value=0.0, max_value=100.0, value=10.0, step=0.1)

st.header("Prix après réduction")
prix_final = prix_origine * (1 - reduction / 100)
st.subheader(f"{prix_final:.2f} €")

st.write("---")

# --- SECTION : EXERCICE INFINI ---
st.header("📝 Entraîne-toi !")

# Initialisation d'un nouvel exercice
if 'exo_prix' not in st.session_state:
    st.session_state.exo_prix = random.randint(20, 200)
    st.session_state.exo_remise = random.choice([10, 20, 25, 50])
    st.session_state.reponse_correcte = st.session_state.exo_prix * (1 - st.session_state.exo_remise / 100)

st.write(f"**Exercice :** Un article coûte **{st.session_state.exo_prix} €**.")
st.write(f"Il y a une remise de **{st.session_state.exo_remise} %**.")

user_ans = st.number_input("Quel est le prix final ?", key="user_ans", step=0.01)

if st.button("Vérifier la réponse"):
    if round(user_ans, 2) == round(st.session_state.reponse_correcte, 2):
        st.success("✅ Bravo ! C'est la bonne réponse.")
        if st.button("Nouvel exercice"):
            # Reset pour générer un nouvel exercice au prochain clic
            for key in ['exo_prix', 'exo_remise', 'reponse_correcte']:
                del st.session_state[key]
            st.rerun()
    else:
        st.error(f"❌ Ce n'est pas ça. Indice : Calcule d'abord {st.session_state.exo_remise}% de {st.session_state.exo_prix} €.")
