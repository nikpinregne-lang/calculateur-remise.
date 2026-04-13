
import streamlit as st
import random
import re

# 1. Configuration de la page
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="wide")

# --- DICTIONNAIRE DES LANGUES ---
languages = {
    "🇫🇷 Français": {"t": "Calculateur Hacker Cosmic 1CA", "p": "Prix d'origine", "r": "Réduction", "check": "Vérifier", "new": "Nouveau 🔄", "author": "Créé par Règne"},
    "🇸🇦 Arabie Saoudite": {"t": "حاسبة هكر كوزميك 1CA", "p": "السعر الأصلي", "r": "خصم", "check": "تحقق", "new": "جديد 🔄", "author": "تم إنشاؤه بواسطة Règne"},
    "🇲🇦 Maroc": {"t": "حاسبة هكر كوزميك 1CA", "p": "السعر الأصلي", "r": "خصم", "check": "تحقق", "new": "جديد 🔄", "author": "تم إنشاؤه بواسطة Règne"},
    "🇷🇴 Română": {"t": "Calculator Hacker Cosmic 1CA", "p": "Preț original", "r": "Reducere", "check": "Verifică", "new": "Nou 🔄", "author": "Creat de Règne"},
    "🇺🇦 Українська": {"t": "Калькулятор Hacker Cosmic 1CA", "p": "Початкова ціна", "r": "Знижка", "check": "Перевірити", "new": "Новий 🔄", "author": "Створено Règne"}
}

# --- CERVEAU ILLIMITÉ DU CHATBOT ---
def cerveau_ia_illimite(question):
    q = question.lower().strip()
    
    # 1. Gestion des calculs automatiques (ex: 1+1, 15*3)
    if re.search(r'\d+', q) and any(op in q for op in ['+', '-', '*', '/']):
        try:
            calcul = "".join(re.findall(r'[0-9\+\-\*\/\.]', q))
            return f"Après analyse, **{calcul} est égal à {eval(calcul)}**. Pas mal, non ? 😎"
        except: pass

    # 2. Politesse et Salutations (Salut, Merci, Ça va)
    if any(word in q for word in ["salut", "bonjour", "hello", "coucou"]):
        return "Salut ! Je suis l'IA de **Règne**. Comment vas-tu en ce jour d'avril 2026 ? 😊"
    
    elif any(word in q for word in ["merci", "thanks", "bravo"]):
        return "Tout le plaisir est pour moi ! Je suis là pour t'aider à briller. ✨"
    
    elif "ça va" in q or "sava" in q or "comment tu vas" in q:
        return "Je vais super bien ! Je suis en pleine forme numérique. Et toi ?"

    # 3. Connaissances générales (Répond à tout)
    elif "bonbon" in q:
        return "Un bonbon est une confiserie sucrée. C'est bon, mais n'en abuse pas ! 🍬"
    elif "qui" in q and "tes" in q:
        return "Je suis l'assistant intelligent de **Règne**, spécialisé dans le projet Hacker Cosmic 1CA !"
    elif "cree" in q or "créé" in q:
        return "C'est **Règne** qui m'a donné vie et qui a conçu tout ce site. 👑"
    
    # 4. Réponse intelligente par défaut (ne dit plus "c'est intéressant")
    else:
        return f"Ta question sur '{question}' est très pertinente. En tant qu'IA, je dirais que c'est un sujet qui mérite réflexion. Tu veux que j'approfondisse ou on fait un calcul ?"

# --- INTERFACE ---
col_main, col_lang = st.columns([0.8, 0.2])

with col_lang:
    sel = st.selectbox("🌐 Pays & Langues", list(languages.keys()))
    T = languages[sel]

with col_main:
    # Barre latérale pour le Chatbot
    with st.sidebar:
        st.title("🤖 Chatbot 1CA")
        st.write("Assistant de **Règne**")
        if "messages" not in st.session_state:
            st.session_state.messages = [{"role": "assistant", "content": "Salut ! Je suis ton IA illimitée. Pose-moi n'importe quelle question !"}]
        for m in st.session_state.messages:
            with st.chat_message(m["role"]): st.markdown(m["content"])
        if prompt := st.chat_input("Écris-moi..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"): st.markdown(prompt)
            rep = cerveau_ia_illimite(prompt)
            with st.chat_message("assistant"): st.markdown(rep)
            st.session_state.messages.append({"role": "assistant", "content": rep})

    # Corps principal
    try: st.image("IMG_0956.png", width=130)
    except: st.info("Logo Hacker Cosmic")

    st.title(T["t"] + " 2026")
    st.write(f"### {T['author']}")
    st.write("---")

    # Calculateur de remise
    p = st.number_input(T["p"], min_value=0.0, value=100.0)
    r = st.number_input(T["r"], min_value=0.0, max_value=100.0, value=10.0)
    st.header(f"Total : {p * (1 - r / 100):.2f} €")

    st.write("---")
    # Exercice
    if 'ex_p' not in st.session_state:
        st.session_state.ex_p, st.session_state.ex_r = random.randint(10, 500), random.randint(5, 50)
        st.session_state.sol = st.session_state.ex_p * (1 - st.session_state.ex_r / 100)
    st.write(f"Défi : {st.session_state.ex_p}€ avec {st.session_state.ex_r}% de remise.")
    ans = st.number_input("Ta réponse :", key="ans")
    if st.button(T["check"]):
        if abs(ans - st.session_state.sol) < 0.1: st.success("✅ Bravo !")
        else: st.error(f"❌ La réponse était {st.session_state.sol:.2f}€")
