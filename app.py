import streamlit as st

st.set_page_config(page_title="Hacker Cosmic - Double IA", layout="wide")

st.title("🤖 Système Double IA : Cosmique & Citoyenne")

# --- PREMIER CHATBOT : IA COSMIQUE (Général) ---
st.header("❄️ IA Chatbot Cosmique")
question_1 = st.text_input("Pose ta question au cerveau de glace :", key="IA1")
if st.button("INTERROGER L'IA COSMIQUE"):
    if question_1:
        st.info(f"Analyse du blizzard en cours... Ta question sur '{question_1}' est très pertinente !")

st.divider()

# --- DEUXIÈME CHATBOT : IA CITOYENNE (Spécial EMC) ---
st.header("📱 IA Chatbot Citoyenne")
st.write("Spécialiste de l'influence et des réseaux sociaux.")
question_2 = st.text_input("Demande-moi si un contenu est une manipulation :", key="IA2")
if st.button("INTERROGER L'IA CITOYENNE"):
    if question_2:
        st.warning(f"Analyse algorithmique... Attention, le sujet '{question_2}' utilise souvent des bulles de filtres !")

# --- TES IMAGES EN BAS ---
st.header("📸 Galerie de preuves")
col1, col2 = st.columns(2)
with col1:
    st.image("IMG_0818.png")
with col2:
    st.image("IMG_0819.png")
