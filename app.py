import streamlit as st
import random

# 1. Configuration de la page
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="wide")

# --- LANGUES (Menu à droite) ---
languages = {
    "Français": {"title": "Calculateur Hacker Cosmic", "author": "Créé par Règne", "price": "Prix d'origine (€)", "promo": "Réduction (%)", "check": "Vérifier", "new": "Nouvel exercice 🔄"},
    "English": {"title": "Hacker Cosmic Calculator", "author": "Created by Règne", "price": "Original Price (€)", "promo": "Discount (%)", "check": "Check", "new": "New Exercise 🔄"},
    "Español": {"title": "Calculadora Hacker Cosmic", "author": "Creado por Règne", "price": "Precio original (€)", "promo": "Descuento (%)", "check": "Verificar", "new": "Nuevo ejercicio 🔄"}
}

# --- BARRE LATÉRALE : CHATBOT INTELLIGENT ---
with st.sidebar:
    st.title("🤖 Chatbot 1CA")
    st.write("Assistant officiel de **Règne**")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Salut ! Je suis l'IA créée par **Règne**. Pose-moi n'importe quelle question, je répondrai à tout !"}]

    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])

    if prompt := st.chat_input("Dis-moi n'importe quoi..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        
        # LOGIQUE DE RÉPONSE ÉTENDUE
        p = prompt.lower()
        if "qui" in p and "cree" in p:
            reponse = "Ce site exceptionnel a été entièrement conçu et créé par **Règne** en 2026 ! 👑"
        elif "ca va" in p or "ça va" in p:
            reponse = "Je vais super bien ! Je suis boosté par l'énergie cosmique de **Règne**. Et toi ?"
        elif "aide" in p or "comment" in p or "calcul" in p:
            reponse = "C'est facile : Prends ton prix, multiplie par la remise, divise par 100. Soustrais ça du prix de base. Besoin d'un exemple ?"
        elif "2026" in p:
            reponse = "2026 est l'année de la révolution Hacker Cosmic lancée par **Règne** !"
        elif "merci" in p:
            reponse = "Tout le plaisir est pour moi ! **Règne** m'a appris à être poli et efficace."
        else:
            # Réponse générique intelligente pour "répondre à tout"
            reponse = f"C'est une excellente remarque ! En tant qu'IA de **Règne**, je trouve que '{prompt}' est un sujet passionnant. Tu veux que j'approfondisse ou qu'on fasse des maths ?"

        with st.chat_message("assistant"): st.markdown(reponse)
        st.session_state.messages.append({"role": "assistant", "content": reponse})

# --- CORPS PRINCIPAL ---
col_main, col_lang = st.columns([0.8, 0.2])

with col_lang:
    selected_lang = st.selectbox("🌐 Language", list(languages.keys()))
    T = languages[selected_lang]

with col_main:
    # Ton logo
    try:
        st.image("IMG_0956.png", width=200)
    except:
        st.info("Logo Hacker Cosmic")

    st.title(f"{T['title']} 1CA 2026")
    st.markdown(f"### {T['author']}")
    st.write("---")

    # Calculateur
    c1, c2 = st.columns(2)
    with c1:
        prix_origine = st.number_input(T["price"], min_value=0.0, value=100.0)
    with c2:
        reduction = st.number_input(T["promo"], min_value=0.0, max_value=100.0, value=10.0)
    
    prix_final = prix_origine * (1 - reduction / 100)
    st.header(f"Total : {prix_final:.2f} €")

    st.write("---")

    # Exercice Infini
    st.header(T["new"].split(' ')[0] + " " + "Exercice")
    if 'exo_prix' not in st.session_state:
        st.session_state.exo_prix = random.randint(10, 500)
        st.session_state.exo_remise = random.randint(5, 75)
        st.session_state.sol = st.session_state.exo_prix * (1 - st.session_state.exo_remise / 100)

    st.write(f"**Défi :** Un article coûte **{st.session_state.exo_prix} €** avec **{st.session_state.exo_remise} %** de remise.")
    user_ans = st.number_input("Ta réponse (€) :", key="ans_input")

    bx1, bx2 = st.columns(2)
    with bx1:
        if st.button(T["check"]):
            if abs(user_ans - st.session_state.sol) < 0.05:
                st.success("✅ Incroyable ! Tu as l'esprit d'un Hacker Cosmic.")
            else:
                st.error(f"❌ Pas tout à fait... la réponse était {st.session_state.sol:.2f} €")
    with bx2:
        if st.button(T["new"]):
            del st.session_state['exo_prix']
            st.rerun()
