import streamlit as st
import random

# 1. Configuration
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="wide")

# --- DICTIONNAIRE DE LANGUES ---
languages = {
    "Français": {"t": "Calculateur Hacker Cosmic", "a": "Créé par Règne", "p": "Prix d'origine (€)", "r": "Réduction (%)", "tot": "Total", "ex": "Exercice Infini", "check": "Vérifier", "new": "Nouveau 🔄"},
    "English": {"t": "Hacker Cosmic Calculator", "a": "Created by Règne", "p": "Original Price (€)", "r": "Discount (%)", "tot": "Total", "ex": "Infinite Exercise", "check": "Check", "new": "New 🔄"},
    "Español": {"t": "Calculadora Hacker Cosmic", "a": "Creado por Règne", "p": "Precio original (€)", "r": "Descuento (%)", "tot": "Total", "ex": "Ejercicio Infinito", "check": "Verificar", "new": "Nuevo 🔄"}
}

# --- CERVEAU DU CHATBOT (RÉPONSE À TOUT) ---
def cerveau_ia(question):
    q = question.lower().strip()
    
    # Salutations
    if q in ["salut", "bonjour", "hello", "coucou", "hi"]:
        return random.choice([
            "Salut ! Comment vas-tu aujourd'hui ?",
            "Bonjour ! Prêt à faire des maths avec moi ?",
            "Hello ! C'est un plaisir de te voir sur le site de **Règne**."
        ])
    
    # Questions sur l'état
    elif "ca va" in q or "ça va" in q or "comment vas-tu" in q:
        return "Je vais super bien, je suis boosté à l'énergie cosmique ! Et toi, la forme ?"
    
    # Identité
    elif "qui" in q and ("es" in q or "tes" in q):
        return "Je suis l'IA officielle de **Règne**. Je suis là pour répondre à tes questions et t'aider avec les calculs !"
    
    # Créateur
    elif "cree" in q or "créé" in q:
        return "C'est **Règne** qui a tout programmé ici, du logo au chatbot ! Un vrai travail de pro. 👑"
    
    # Sujets divers (ex: bonbon)
    elif "bonbon" in q:
        return "Un bonbon est une sucrerie. C'est délicieux, mais attention aux dents ! 🍬"
    
    # Réponse par défaut "intelligente"
    else:
        return f"Je vois ce que tu veux dire par '{question}'. C'est super intéressant ! En tant qu'assistant de **Règne**, je dirais qu'il y a toujours quelque chose à apprendre."

# --- BARRE LATÉRALE : CHATBOT ---
with st.sidebar:
    st.title("🤖 Chatbot 1CA")
    st.write("Assistant de **Règne**")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Salut ! Je suis l'IA de **Règne**. Pose-moi n'importe quelle question !"}]
    
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    
    if prompt := st.chat_input("Dis-moi quelque chose..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        
        rep = cerveau_ia(prompt)
        with st.chat_message("assistant"): st.markdown(rep)
        st.session_state.messages.append({"role": "assistant", "content": rep})

# --- CORPS PRINCIPAL ---
col_main, col_lang = st.columns([0.8, 0.2])

with col_lang:
    sel = st.selectbox("🌐 Langue", list(languages.keys()))
    T = languages[sel]

with col_main:
    st.image("IMG_0956.png", width=150)
    st.title(T["t"] + " 2026")
    st.subheader(T["a"])
    st.write("---")

    p = st.number_input(T["p"], min_value=0.0, value=100.0)
    r = st.number_input(T["r"], min_value=0.0, max_value=100.0, value=10.0)
    st.header(f"{T['tot']} : {p * (1 - r / 100):.2f} €")

    st.write("---")
    st.header(T["ex"])
    if 'ex_p' not in st.session_state:
        st.session_state.ex_p = random.randint(10, 500)
        st.session_state.ex_r = random.randint(5, 50)
        st.session_state.sol = st.session_state.ex_p * (1 - st.session_state.ex_r / 100)

    st.write(f"Défi : {st.session_state.ex_p} € avec {st.session_state.ex_r} % de remise.")
    ans = st.number_input("Ta réponse :", key="ans")
    
    c1, c2 = st.columns(2)
    with c1:
        if st.button(T["check"]):
            if abs(ans - st.session_state.sol) < 0.1: st.success("✅ Bravo !")
            else: st.error(f"❌ La réponse était {st.session_state.sol:.2f} €")
    with c2:
        if st.button(T["new"]):
            del st.session_state['ex_p']
            st.rerun()
