import streamlit as st

st.set_page_config(page_title="Double IA - Projet EMC", layout="wide")

# --- MÉMOIRE DES CHATS ---
if 'chat_cosmique' not in st.session_state:
    st.session_state.chat_cosmique = []
if 'chat_citoyen' not in st.session_state:
    st.session_state.chat_citoyen = []

st.title("🤖 Système Double IA : Cosmique & Citoyenne")

# --- BOUTON EFFACER ---
if st.sidebar.button("🗑️ EFFACER LES DISCUSSIONS"):
    st.session_state.chat_cosmique = []
    st.session_state.chat_citoyen = []
    st.rerun()

# --- EXPLICATION ---
st.info("Utilisez ces deux IA pour comparer la liberté d'expression et la manipulation algorithmique.")

col1, col2 = st.columns(2)

with col1:
    st.header("❄️ IA Cosmique")
    q1 = st.text_input("Pose ta question :", key="ia1")
    if st.button("ENVOYER (IA 1)"):
        if q1:
            st.session_state.chat_cosmique.append(f"👤: {q1}")
            st.session_state.chat_cosmique.append(f"🤖: L'espace est vaste, tout comme ta liberté !")
    for m in st.session_state.chat_cosmique: st.write(m)

with col2:
    st.header("📱 IA Citoyenne")
    q2 = st.text_input("Demande une analyse :", key="ia2")
    if st.button("ENVOYER (IA 2)"):
        if q2:
            st.session_state.chat_citoyen.append(f"👤: {q2}")
            st.session_state.chat_citoyen.append(f"🤖: Attention, cet avis est peut-être influencé par un algorithme.")
    for m in st.session_state.chat_citoyen: st.write(m)
