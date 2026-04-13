import streamlit as st
import random
import re

# 1. Configuration de la page
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="wide")

# --- DICTIONNAIRE DES LANGUES NATIONALES ---
languages = {
    "🇫🇷 Français": {"t": "Calculateur Hacker Cosmic", "p": "Prix d'origine", "r": "Réduction", "check": "Vérifier", "new": "Nouveau 🔄", "author": "Créé par Règne"},
    "🇸🇦 Arabie Saoudite (العربية)": {"t": "حاسبة هكر كوزميك", "p": "السعر الأصلي", "r": "خصم", "check": "تحقق", "new": "جديد 🔄", "author": "تم إنشاؤه بواسطة Règne"},
    "🇲🇦 Maroc (العربية)": {"t": "حاسبة هكر كوزميك", "p": "السعر الأصلي", "r": "خصم", "check": "تحقق", "new": "جديد 🔄", "author": "تم إنشاؤه بواسطة Règne"},
    "🇷🇴 Română": {"t": "Calculator Hacker Cosmic", "p": "Preț original", "r": "Reducere", "check": "Verifică", "new": "Nou 🔄", "author": "Creat de Règne"},
    "🇺🇦 Українська": {"t": "Калькулятор Hacker Cosmic", "p": "Початкова ціна", "r": "Знижка", "check": "Перевірити", "new": "Новий 🔄", "author": "Створено Règne"},
    "🇺🇸 English": {"t": "Hacker Cosmic Calculator", "p": "Original Price", "r": "Discount", "check": "Check", "new": "New 🔄", "author": "Created by Règne"},
    "🇪🇸 Español": {"t": "Calculadora Hacker Cosmic", "p": "Precio original", "r": "Descuento", "check": "Verificar", "new": "Nuevo 🔄", "author": "Creado por Règne"},
    "🇩🇿 Algérie": {"t": "حاسبة هكر كوزميك", "p": "السعر الأصلي", "r": "خصم", "check": "تحقق", "new": "جديد 🔄", "author": "تم إنشاؤه بواسطة Règne"},
    "🇵🇹 Português": {"t": "Calculadora Hacker Cosmic", "p": "Preço original", "r": "Desconto", "check": "Verificar", "new": "Novo 🔄", "author": "Criado por Règne"}
}

# --- CERVEAU DU CHATBOT (RÉPOND À TOUT) ---
def cerveau_ia(question):
    q = question.lower().strip()
    
    # CALCULS (ex: 1+1)
    if re.search(r'\d+', q) and any(op in q for op in ['+', '-', '*', '/']):
        try:
            calcul = "".join(re.findall(r'[0-9\+\-\*\/\.]', q))
            return f"Facile ! **{calcul} ça fait {eval(calcul)}**. Je suis un génie des maths grâce à **Règne** ! 😎"
        except: return "Oups, ce calcul est trop complexe pour moi !"

    # POLITESSE & SALUTATIONS
    if q in ["salut", "bonjour", "hello", "sava", "ça va"]:
        return "Salut ! Je vais super bien en ce mois d'avril 2026 ! Et toi ? 😊"
    
    # QUESTIONS GÉNÉRALES
    elif "bonbon" in q:
        return "Un bonbon est une sucrerie. Miam ! Mais attention aux dents. 🍬"
    elif "cree" in q or "créé" in q:
        return "Tout a été créé par **Règne**. C'est lui le patron ! 👑"
    else:
        return f"En tant qu'IA de **Règne**, je trouve que '{question}' est super intéressant !"

# --- INTERFACE ---
col_main, col_lang = st.columns([0.8, 0.2])

with col_lang:
    sel = st.selectbox("🌐 Pays & Langues", list(languages.keys()))
    T = languages[sel]

with col_main:
    # Sidebar Chatbot
    with st.sidebar:
        st.title("🤖 Chatbot 1CA")
        if "messages" not in st.session_state:
            st.session_state.messages = [{"role": "assistant", "content": "Salut ! Je réponds à tes calculs et tes questions !"}]
        for m in st.session_state.messages:
            with st.chat_message(m["role"]): st.markdown(m["content"])
        if prompt := st.chat_input("Pose-moi une question..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"): st.markdown(prompt)
            rep = cerveau_ia(prompt)
            with st.chat_message("assistant"): st.markdown(rep)
            st.session_state.messages.append({"role": "assistant", "content": rep})

    # Contenu principal
    try: st.image("IMG_0956.png", width=120)
    except: st.info("Logo Hacker Cosmic")

    st.title(T["t"] + " 2026")
    st.write(f"### {T['author']}")
    st.write("---")

    p = st.number_input(T["p"], min_value=0.0, value=100.0)
    r = st.number_input(T["r"], min_value=0.0, max_value=100.0, value=10.0)
    st.header(f"Total : {p * (1 - r / 100):.2f} €")

    st.write("---")
    st.header(T["new"])
    if 'ex_p' not in st.session_state:
        st.session_state.ex_p, st.session_state.ex_r = random.randint(10, 500), random.randint(5, 50)
        st.session_state.sol = st.session_state.ex_p * (1 - st.session_state.ex_r / 100)
    st.write(f"Défi : {st.session_state.ex_p}€ avec {st.session_state.ex_r}% de remise.")
    ans = st.number_input("Ta réponse :", key="ans")
    if st.button(T["check"]):
        if abs(ans - st.session_state.sol) < 0.1: st.success("✅ Bravo !")
        else: st.error(f"❌ C'était {st.session_state.sol:.2f}€")
