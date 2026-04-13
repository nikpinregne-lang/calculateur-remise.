
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
    "🇪🇸 Español": {"t": "Calculadora Hacker Cosmic 1CA", "p": "Precio original", "r": "Descuento", "check": "Verificar", "new": "Nuevo 🔄", "author": "Creado por Règne"}
}

# --- FONCTION VOIX AUTOMATIQUE ---
def parler_auto(texte):
    st.components.v1.html(f"""
        <script>
        var msg = new SpeechSynthesisUtterance("{texte}");
        msg.lang = 'fr-FR';
        msg.volume = 1;
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
        parler_auto(accueil) # Parle tout seul au début
    
    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])

    if prompt := st.chat_input("Écris-moi..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        rep = cerveau_ia(prompt)
        st.session_state.messages.append({"role": "assistant", "content": rep})
        parler_auto(rep) # Parle tout seul à chaque réponse
        st.rerun()

with col_main:
    try: st.image("IMG_0956.png", width=130)
    except: st.info("Logo Hacker Cosmic")
    st.title(T["t"] + " 2026")
    st.write(f"### {T['author']}")
    st.write("---")
    
    # CALCULATEUR
    p = st.number_input(T["p"], min_value=0.0, value=100.0)
    r = st.number_input(T["r"], min_value=0.0, max_value=100.0, value=10.0)
    st.header(f"Total : {p * (1 - r / 100):.2f} €")
    
    st.write("---")
    
    # DÉFI (EXERCICE)
    st.header("🎯 Défi Mathématique")
    if 'ex_p' not in st.session_state:
        st.session_state.ex_p = random.randint(10, 500)
        st.session_state.ex_r = random.randint(5, 50)
        st.session_state.sol = st.session_state.ex_p * (1 - st.session_state.ex_r / 100)
    
    st.write(f"Article à **{st.session_state.ex_p} €** avec **{st.session_state.ex_r} %** de remise.")
    ans = st.number_input("Ta réponse (€) :", key="ans_input")
    
    c1, c2 = st.columns(2)
    with c1:
        if st.button(T["check"]):
            if abs(ans - st.session_state.sol) < 0.1: st.success("✅ Bravo ! C'est juste.")
            else: st.error(f"❌ Faux ! C'était {st.session_state.sol:.2f} €")
    with c2:
        if st.button(T["new"]):
            del st.session_state['ex_p']
            st.rerun()
