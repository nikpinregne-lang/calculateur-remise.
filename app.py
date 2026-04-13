
import streamlit as st
import random
import re

# 1. Configuration
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="wide")

# --- DICTIONNAIRE COMPLET DES LANGUES ---
languages = {
    "🇫🇷 Français": {"t": "Calculateur Hacker Cosmic 1CA", "p": "Prix d'origine", "r": "Réduction", "check": "Vérifier", "new": "Nouveau 🔄", "author": "Créé par Règne"},
    "🇸🇦 Arabie Saoudite": {"t": "حاسبة هكر كوزميك 1CA", "p": "السعر الأصلي", "r": "خصم", "check": "تحقق", "new": "جديد 🔄", "author": "تم إنشاؤه بواسطة Règne"},
    "🇲🇦 Maroc": {"t": "حاسبة هكر كوزميك 1CA", "p": "السعر الأصلي", "r": "خصم", "check": "تحقق", "new": "جديد 🔄", "author": "تم إنشاؤه بواسطة Règne"},
    "🇷🇴 Română": {"t": "Calculator Hacker Cosmic 1CA", "p": "Preț original", "r": "Reducere", "check": "Verifică", "new": "Nou 🔄", "author": "Creat de Règne"},
    "🇺🇦 Українська": {"t": "Калькулятор Hacker Cosmic 1CA", "p": "Початкова ціна", "r": "Знижка", "check": "Перевірити", "new": "Новий 🔄", "author": "Створено Règne"},
    "🇺🇸 English": {"t": "Hacker Cosmic Calculator 1CA", "p": "Original Price", "r": "Discount", "check": "Check", "new": "New 🔄", "author": "Created by Règne"},
    "🇪🇸 Español": {"t": "Calculadora Hacker Cosmic 1CA", "p": "Precio original", "r": "Descuento", "check": "Verificar", "new": "Nuevo 🔄", "author": "Creado por Règne"},
    "🇵🇹 Português": {"t": "Calculadora Hacker Cosmic 1CA", "p": "Preço original", "r": "Desconto", "check": "Verificar", "new": "Novo 🔄", "author": "Criado por Règne"}
}

# --- FONCTION VOIX ---
def parler(texte):
    st.components.v1.html(f"""
        <script>
        var msg = new SpeechSynthesisUtterance("{texte}");
        msg.lang = 'fr-FR';
        window.speechSynthesis.speak(msg);
        </script>
    """, height=0)

# --- CERVEAU DU CHATBOT ---
def cerveau_ia(question):
    q = question.lower().strip()
    if re.search(r'\d+', q) and any(op in q for op in ['+', '-', '*', '/']):
        try:
            calcul = "".join(re.findall(r'[0-9\+\-\*\/\.]', q))
            return f"Après analyse, **{calcul} est égal à {eval(calcul)}**. Pas mal, non ? 😎"
        except: pass
    if any(word in q for word in ["salut", "bonjour", "hello"]):
        return "Salut ! Comment vas-tu aujourd'hui ? 😊"
    elif "ça va" in q or "sava" in q:
        return "Je vais super bien ! Je suis en pleine forme numérique grâce à **Règne**. Et toi ?"
    elif "qui" in q and "tes" in q:
        return "Je suis l'assistant intelligent de **Règne**, le GOAT du projet 1CA !"
    return f"Ta question sur '{question}' est très pertinente. En tant qu'IA de **Règne**, je dirais que c'est un sujet qui mérite réflexion."

# --- INTERFACE ---
col_main, col_lang = st.columns([0.8, 0.2])

with col_lang:
    sel = st.selectbox("🌐 Pays & Langues", list(languages.keys()))
    T = languages[sel]

with st.sidebar:
    st.title("🤖 Chatbot 1CA")
    st.write("Assistant de **Règne**")
    
    accueil = "Salut ! Je suis ton ia illimité. pose moi nimporte quelle question"
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": accueil}]
        parler(accueil) # La voix parle au début
    
    for i, m in enumerate(st.session_state.messages):
        with st.chat_message(m["role"]):
            st.markdown(m["content"])
            if m["role"] == "assistant":
                if st.button("🔊 Écouter", key=f"btn_{i}"):
                    parler(m["content"])

    if prompt := st.chat_input("Écris-moi..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        rep = cerveau_ia(prompt)
        st.session_state.messages.append({"role": "assistant", "content": rep})
        parler(rep) # Parle aussi pour les réponses
        st.rerun()

with col_main:
    try: st.image("IMG_0956.png", width=130)
    except: st.info("Logo Hacker Cosmic")
    st.title(T["t"] + " 2026")
    st.write(f"### {T['author']}")
    st.write("---")
    p = st.number_input(T["p"], min_value=0.0, value=100.0)
    r = st.number_input(T["r"], min_value=0.0, max_value=100.0, value=10.0)
    st.header(f"Total : {p * (1 - r / 100):.2f} €")
