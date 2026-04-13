import streamlit as st
import random

# 1. Configuration
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="wide")

# --- DICTIONNAIRE MULTILINGUE ---
languages = {
    "Français": {"title": "Calculateur", "price": "Prix d'origine", "promo": "Réduction", "check": "Vérifier", "new": "Nouveau", "author": "Créé par IEEM", "bot_hi": "Bonjour ! Je suis l'assistant de IEEM. Comment puis-je t'aider avec les mathématiques ?"},
    "English": {"title": "Calculator", "price": "Original Price", "promo": "Discount", "check": "Check", "new": "New", "author": "Created by IEEM", "bot_hi": "Hello! I am IEEM's assistant. How can I help you with math?"},
    "Español": {"title": "Calculadora", "price": "Precio original", "promo": "Descuento", "check": "Verificar", "new": "Nuevo", "author": "Creado por IEEM", "bot_hi": "¡Hola! Soy el asistente de IEEM. ¿Cómo puedo ayudarte con les matemáticas?"}
}

# --- BARRE LATÉRALE GAUCHE : CHATBOT INTELLIGENT ---
with st.sidebar:
    st.title("🤖 Chatbot 1CA")
    if "messages" not in st.session_state: 
        st.session_state.messages = [{"role": "assistant", "content": "Salut ! Je suis l'IA de IEEM. Pose-moi une question sur le site ou les remises !"}]
    
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    
    if prompt := st.chat_input("Pose-moi une question..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        
        # LOGIQUE DE RÉPONSE (On ne recopie plus, on répond !)
        p = prompt.lower()
        if "qui" in p and "cree" in p:
            reponse = "Ce site a été créé par le génie **IEEM** en 2026 ! 😎"
        elif "comment" in p and "calcul" in p:
            reponse = "C'est simple ! Tu prends le prix, tu le multiplies par la remise, et tu divises par 100. Puis tu soustrais ça au prix de départ."
        elif "ca va" in p:
            reponse = "Je vais super bien, je suis en pleine forme numérique ! Et toi ?"
        else:
            reponse = "C'est très intéressant ! Je suis encore en train d'apprendre, mais IEEM m'a configuré pour t'aider au mieux."

        with st.chat_message("assistant"): st.markdown(reponse)
        st.session_state.messages.append({"role": "assistant", "content": reponse})

# --- CORPS PRINCIPAL ---
col_main, col_lang = st.columns([0.8, 0.2])

with col_lang:
    selected_lang = st.selectbox("🌐 Language", list(languages.keys()))
    T = languages[selected_lang]

with col_main:
    try:
        st.image("IMG_0956.png", width=200)
    except:
        st.info("Logo Hacker Cosmic")

    st.title(f"{T['title']} Hacker Cosmic 1CA 2026")
    st.write(T["author"])
    st.write("---")

    # Calculateur
    prix_origine = st.number_input(f"{T['price']} (€)", min_value=0.0, value=100.0)
    reduction = st.number_input(f"{T['promo']} (%)", min_value=0.0, max_value=100.0, value=10.0)
    st.subheader(f"Total: {prix_origine * (1 - reduction / 100):.2f} €")

    st.write("---")

    # Exercice
    st.header(T["exo_title"] if "exo_title" in T else "📝 Exercice")
    if 'exo_prix' not in st.session_state:
        st.session_state.exo_prix = random.randint(10, 500)
        st.session_state.exo_remise = random.randint(5, 75)
        st.session_state.sol = st.session_state.exo_prix * (1 - st.session_state.exo_remise / 100)

    st.write(f"Prix: **{st.session_state.exo_prix} €** | Remise: **{st.session_state.exo_remise} %**")
    user_ans = st.number_input("Ta réponse :", key="ans")

    c1, c2 = st.columns(2)
    with c1:
        if st.button(T["check"]):
            if abs(user_ans - st.session_state.sol) < 0.05: st.success("✅ Bravo !")
            else: st.error("❌ Essaye encore !")
    with c2:
        if st.button(T["new"]):
            del st.session_state['exo_prix']
            st.rerun()

