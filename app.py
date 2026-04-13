import streamlit as st
import random

# Configuration
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="wide")

# --- CERVEAU INTELLIGENT ---
def reponse_ia(question):
    q = question.lower()
    
    # Priorité aux infos sur le créateur
    if "qui" in q and "cree" in q:
        return "Ce site incroyable a été créé par mon maître, le grand **Règne** ! 👑"
    
    # Réponses encyclopédiques intégrées
    connaissances = {
        "bonbon": "Un bonbon est une friandise faite de sucre. C'est délicieux mais attention aux caries ! 🍬",
        "soleil": "Le soleil est l'étoile au centre de notre système solaire. Il nous éclaire !",
        "2026": "C'est l'année actuelle, l'année du Hacker Cosmic !",
        "manger": "Moi je mange des données, mais toi tu devrais goûter une spécialité de **Règne** !"
    }
    
    for mot, rep in connaissances.items():
        if mot in q:
            return rep

    # Si le mot n'est pas connu, il fait une réponse "intelligente" de curiosité
    return f"En tant qu'IA de **Règne**, je trouve que '{question}' est un sujet fascinant ! Malheureusement, je n'ai pas encore accès à tout le dictionnaire, mais je peux t'aider pour tes calculs !"

# --- BARRE LATÉRALE : CHATBOT ---
with st.sidebar:
    st.title("🤖 Chatbot 1CA")
    st.write("Assistant officiel de **Règne**")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Salut ! Je suis l'IA de **Règne**. Pose-moi n'importe quelle question !"}]

    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])

    if prompt := st.chat_input("Dis-moi n'importe quoi..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        
        # Réponse du cerveau
        reponse = reponse_ia(prompt)
        with st.chat_message("assistant"): st.markdown(reponse)
        st.session_state.messages.append({"role": "assistant", "content": reponse})

# --- CORPS PRINCIPAL ---
col_main, col_lang = st.columns([0.8, 0.2])
with col_lang:
    st.selectbox("🌐 Langue", ["Français", "English"])

with col_main:
    try:
        st.image("IMG_0956.png", width=200)
    except:
        st.info("Logo Hacker Cosmic")

    st.title("Calculateur Hacker Cosmic 1CA 2026")
    st.markdown("### Créé par **Règne**")
    st.write("---")

    # Calculateur
    prix = st.number_input("Prix d'origine (€)", min_value=0.0, value=100.0)
    remise = st.number_input("Réduction (%)", min_value=0.0, max_value=100.0, value=10.0)
    st.header(f"Total : {prix * (1 - remise / 100):.2f} €")

    st.write("---")
    
    # Exercice
    st.header("📝 Exercice")
    if 'exo_prix' not in st.session_state:
        st.session_state.exo_prix = random.randint(10, 500)
        st.session_state.exo_remise = random.randint(5, 50)
        st.session_state.sol = st.session_state.exo_prix * (1 - st.session_state.exo_remise / 100)
    
    st.write(f"Prix : {st.session_state.exo_prix}€ | Remise : {st.session_state.exo_remise}%")
    ans = st.number_input("Ta réponse :", key="ans")
    if st.button("Vérifier"):
        if abs(ans - st.session_state.sol) < 0.1: st.success("Bravo !")
        else: st.error("Faux !")
