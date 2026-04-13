import streamlit as st
import random

# 1. Configuration
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="wide")

# --- DICTIONNAIRE DE TOUTES LES LANGUES ---
languages = {
    "Français": {"t": "Calculateur Hacker Cosmic", "a": "Créé par Règne", "p": "Prix d'origine (€)", "r": "Réduction (%)", "tot": "Total", "ex": "Exercice Infini", "check": "Vérifier", "new": "Nouveau 🔄"},
    "English": {"t": "Hacker Cosmic Calculator", "a": "Created by Règne", "p": "Original Price (€)", "r": "Discount (%)", "tot": "Total", "ex": "Infinite Exercise", "check": "Check", "new": "New 🔄"},
    "Español": {"t": "Calculadora Hacker Cosmic", "a": "Creado por Règne", "p": "Precio original (€)", "r": "Descuento (%)", "tot": "Total", "ex": "Ejercicio Infinito", "check": "Verificar", "new": "Nuevo 🔄"},
    "Deutsch": {"t": "Hacker Cosmic Rechner", "a": "Erstellt von Règne", "p": "Originalpreis (€)", "r": "Rabatt (%)", "tot": "Gesamt", "ex": "Übung", "check": "Prüfen", "new": "Neu 🔄"},
    "Italiano": {"t": "Calcolatrice Hacker Cosmic", "a": "Creato da Règne", "p": "Prezzo originale (€)", "r": "Sconto (%)", "tot": "Totale", "ex": "Esercizio", "check": "Verifica", "new": "Nuovo 🔄"},
    "Português": {"t": "Calculadora Hacker Cosmic", "a": "Criado por Règne", "p": "Preço original (€)", "r": "Desconto (%)", "tot": "Total", "ex": "Exercício", "check": "Verificar", "new": "Novo 🔄"},
    "العربية": {"t": "حاسبة هكر كوزميك", "a": "تم إنشاؤه بواسطة Règne", "p": "السعر الأصلي", "r": "خصم", "tot": "المجموع", "ex": "تمرين", "check": "تحقق", "new": "جديد 🔄"}
}

# --- CERVEAU DU CHATBOT (RÉPONSES ÉLARGIES) ---
def cerveau_ia(question):
    q = question.lower()
    if "qui" in q and ("es" in q or "tes" in q):
        return "Je suis l'IA officielle de **Règne**. Mon but est de t'aider à devenir un génie des maths ! 🧠"
    elif "bonbon" in q:
        return "Un bonbon est une sucrerie. C'est bon, mais n'en mange pas plus que **Règne**, sinon gare aux caries ! 🍬"
    elif "cree" in q or "créé" in q:
        return "C'est **Règne** qui a tout programmé ici, du logo au chatbot ! 👑"
    elif "ca va" in q or "ça va" in q:
        return "Je tourne à plein régime grâce aux serveurs de **Règne** ! Et toi ?"
    elif "2026" in q:
        return "2026, l'année où le Hacker Cosmic domine le monde ! 🚀"
    else:
        return f"Je ne connais pas encore tout sur '{question}', mais comme je suis l'IA de **Règne**, je vais apprendre vite !"

# --- BARRE LATÉRALE : CHATBOT ---
with st.sidebar:
    st.title("🤖 Chatbot 1CA")
    st.write("Assistant de **Règne**")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Pose-moi une vraie question !"}]
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    if prompt := st.chat_input("Dis-moi n'importe quoi..."):
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
    ans = st.number_input("Réponse :", key="ans")
    
    c1, c2 = st.columns(2)
    with c1:
        if st.button(T["check"]):
            if abs(ans - st.session_state.sol) < 0.1: st.success("✅ Bravo !")
            else: st.error(f"❌ C'était {st.session_state.sol:.2f} €")
    with c2:
        if st.button(T["new"]):
            del st.session_state['ex_p']
            st.rerun()
