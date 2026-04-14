import streamlit as st
import random
import re

# 1. Configuration
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="wide")

# --- LISTE DES PAYS ET LANGUES ---
languages = {
    "🇫🇷 France": {"t": "Calculateur 1CA", "p": "Prix d'origine", "r": "Réduction", "author": "Créé par Règne"},
    "🇲🇦 Maroc": {"t": "حاسبة هكر كوزميك", "p": "السعر الأصلي", "r": "خصم", "author": "تم إنشاؤه بواسطة Règne"},
    "🇸🇦 Arabie Saoudite": {"t": "حاسبة هكر كوزميك", "p": "السعر الأصلي", "r": "خصم", "author": "تم إنشاؤه بواسطة Règne"},
    "🇧🇪 Belgique": {"t": "Calculateur 1CA", "p": "Prix d'origine", "r": "Réduction", "author": "Créé par Règne"},
    "🇷🇴 România": {"t": "Calculator Cosmic", "p": "Preț original", "r": "Reducere", "author": "Creat de Règne"},
    "🇺🇦 Україна": {"t": "Калькулятор Космік", "p": "Початкова ціна", "r": "Знижка", "author": "Створено Règne"},
    "🇩🇿 Algérie": {"t": "حاسبة الجزائر", "p": "السعر الأصلي", "r": "خصم", "author": "تم إنشاؤه بواسطة Règne"},
    "🇹🇳 Tunisie": {"t": "حاسبة تونس", "p": "السعر الأصلي", "r": "خصم", "author": "تم إنشاؤه بواسطة Règne"},
    "🇺🇸 USA / UK": {"t": "Cosmic Calculator", "p": "Original Price", "r": "Discount", "author": "Created by Règne"},
    "🇪🇸 España": {"t": "Calculadora Cósmica", "p": "Precio original", "r": "Descuento", "author": "Creado por Règne"},
    "🇮🇹 Italia": {"t": "Calcolatrice Cosmica", "p": "Prezzo originale", "r": "Sconto", "author": "Creato da Règne"},
    "🇵🇹 Portugal": {"t": "Calculadora Cósmica", "p": "Preço original", "r": "Desconto", "author": "Criado por Règne"}
}

# --- CERVEAU DU CHATBOT (RÉPONSE DIRECTE) ---
def cerveau_ia_goat(question):
    q = question.lower().strip()
    
    # Culture sur les pays (Capitales)
    infos_pays = {
        "belgique": "Bruxelles 🇧🇪.",
        "france": "Paris 🇫🇷.",
        "maroc": "Rabat 🇲🇦.",
        "arabie": "Riyad 🇸🇦.",
        "ukraine": "Kyiv 🇺🇦.",
        "roumanie": "Bucarest 🇷🇴.",
        "algérie": "Alger 🇩🇿.",
        "tunisie": "Tunis 🇹🇳.",
        "espagne": "Madrid 🇪🇸.",
        "italie": "Rome 🇮🇹."
    }

    if "qui" in q and "cree" in q: return "Le GOAT c'est **Règne** ! 👑"
    
    for pays, info in infos_pays.items():
        if pays in q: return f"La capitale c'est {info}"

    if re.search(r'\d+', q) and any(op in q for op in ['+', '-', '*', '/']):
        try:
            res = eval("".join(re.findall(r'[0-9\+\-\*\/\.]', q)))
            return f"Calcul fait : **{res}**. Facile pour l'IA de Règne ! 😎"
        except: return "Calcul trop bizarre pour moi."

    if q in ["salut", "bonjour", "wesh"]: return "Wesh ! Quoi de neuf ? Pose ta question."
    if "ca va" in q or "ça va" in q: return "Tranquille et toi ? Je suis prêt à tout calculer."
    
    return f"Je sais pas tout sur '{question}', mais demande à **Règne**, c'est lui qui sait tout ! 😉"

# --- INTERFACE ---
col_main, col_lang = st.columns([0.8, 0.2])

with col_lang:
    sel = st.selectbox("🌐 Pays / Langue", list(languages.keys()))
    T = languages[sel]

with st.sidebar:
    st.title("🤖 Chatbot 1CA")
    st.write("Assistant de **Règne**")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Wesh ! Pose ta question, je réponds direct."}]
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    if prompt := st.chat_input("Écris-moi..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        rep = cerveau_ia_goat(prompt)
        with st.chat_message("assistant"): st.markdown(rep)
        st.session_state.messages.append({"role": "assistant", "content": rep})

with col_main:
    st.image("IMG_0956.png", width=120)
    st.title(T["t"] + " 2026")
    st.write(f"### {T['author']}")
    st.write("---")
    
    prix = st.number_input(T["p"], value=100.0)
    taux = st.number_input(T["r"], value=10.0)
    st.header(f"Total : {prix * (1 - taux/100):.2f} €")
