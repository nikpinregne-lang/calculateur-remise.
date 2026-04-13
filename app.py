import streamlit as st
import random

# 1. Configuration
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="wide")

# --- DICTIONNAIRE DES LANGUES OFFICIELLES (Menu à droite) ---
languages = {
    "🇫🇷 Français": {"t": "Calculateur Hacker Cosmic", "p": "Prix d'origine", "r": "Réduction", "check": "Vérifier", "new": "Nouveau 🔄", "author": "Créé par Règne"},
    "🇺🇸 English": {"t": "Hacker Cosmic Calculator", "p": "Original Price", "r": "Discount", "check": "Check", "new": "New 🔄", "author": "Created by Règne"},
    "🇷🇴 Română": {"t": "Calculator Hacker Cosmic", "p": "Preț original", "r": "Reducere", "check": "Verifică", "new": "Nou 🔄", "author": "Creat de Règne"},
    "🇺🇦 Українська": {"t": "Калькулятор Hacker Cosmic", "p": "Початкова ціна", "r": "Знижка", "check": "Перевірити", "new": "Новий 🔄", "author": "Створено Règne"},
    "🇪🇸 Español": {"t": "Calculadora Hacker Cosmic", "p": "Precio original", "r": "Descuento", "check": "Verificar", "new": "Nuevo 🔄", "author": "Creado por Règne"},
    "🇵🇹 Português": {"t": "Calculadora Hacker Cosmic", "p": "Preço original", "r": "Desconto", "check": "Verificar", "new": "Novo 🔄", "author": "Criado por Règne"},
    "🇩🇪 Deutsch": {"t": "Hacker Cosmic Rechner", "p": "Originalpreis", "r": "Rabatt", "check": "Prüfen", "new": "Neu 🔄", "author": "Erstellt von Règne"},
    "🇮🇹 Italiano": {"t": "Calcolatrice Hacker Cosmic", "p": "Prezzo originale", "r": "Sconto", "check": "Verifica", "new": "Nuovo 🔄", "author": "Creato da Règne"},
    "🇵🇱 Polski": {"t": "Kalkulator Hacker Cosmic", "p": "Cena oryginalna", "r": "Zniżka", "check": "Sprawdź", "new": "Nowy 🔄", "author": "Stworzone przez Règne"},
    "🇹🇷 Türkçe": {"t": "Hacker Kozmik Hesaplayıcı", "p": "Orijinal Fiyat", "r": "İndirim", "check": "Kontrol Et", "new": "Yeni 🔄", "author": "Règne tarafından oluşturuldu"},
    "🇸🇦 العربية": {"t": "حاسبة هكر كوزميك", "p": "السعر الأصلي", "r": "خصم", "check": "تحقق", "new": "جديد 🔄", "author": "تم إنشاؤه بواسطة Règne"},
    "🇨🇳 中文": {"t": "黑客宇宙计算器", "p": "原价", "r": "折扣", "check": "检查", "new": "新 🔄", "author": "由 Règne 创建"},
    "🇯🇵 日本語": {"t": "ハッカー宇宙計算機", "p": "元の価格", "r": "割引", "check": "チェック", "new": "新 🔄", "author": "Règne による作成"}
}

# --- CERVEAU DU CHATBOT (Réponses à tout) ---
def cerveau_ia(question):
    q = question.lower().strip()
    
    if "langue" in q and ("combien" in q or "pays" in q):
        return "Il y a environ 180 langues officielles dans les pays du monde. L'anglais, le français, l'espagnol et l'arabe sont les plus répandues ! 🌍"
    elif "salut" in q or "bonjour" in q:
        return "Salut ! Je suis l'IA de **Règne**. Comment vas-tu ?"
    elif "bien" in q and "vous" in q:
        return "Je vais super bien, je suis programmé pour être toujours de bonne humeur ! 😊"
    elif "bonbon" in q:
        return "Un bonbon est une sucrerie. Miam ! Mais attention aux dents. 🍬"
    elif "cree" in q or "créé" in q:
        return "Tout ce que tu vois a été créé par **Règne**. C'est le patron ! 👑"
    else:
        return f"C'est super intéressant ! En tant qu'IA de **Règne**, j'apprends tous les jours grâce à tes questions sur '{question}'."

# --- INTERFACE ---
with st.sidebar:
    st.title("🤖 Chatbot 1CA")
    st.write("Assistant de **Règne**")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Salut ! Teste mes connaissances ou demande-moi de traduire !"}]
    
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    
    if prompt := st.chat_input("Dis-moi quelque chose..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        rep = cerveau_ia(prompt)
        with st.chat_message("assistant"): st.markdown(rep)
        st.session_state.messages.append({"role": "assistant", "content": rep})

# Corps principal (Colonnes)
col_main, col_lang = st.columns([0.8, 0.2])

with col_lang:
    sel = st.selectbox("🌐 Langue / Language", list(languages.keys()))
    T = languages[sel]

with col_main:
    # Affichage du logo
    try:
        st.image("IMG_0956.png", width=130)
    except:
        st.info("Logo Hacker Cosmic")

    st.title(T["t"] + " 2026")
    st.write(f"### {T['author']}")
    st.write("---")

    # Calculateur
    prix = st.number_input(T["p"], min_value=0.0, value=100.0)
    remise = st.number_input(T["r"], min_value=0.0, max_value=100.0, value=10.0)
    
    resultat = prix * (1 - remise / 100)
    st.header(f"Total : {resultat:.2f} €")

    st.write("---")

    # Exercice Infini
    st.header(T["new"])
    if 'ex_p' not in st.session_state:
        st.session_state.ex_p = random.randint(10, 500)
        st.session_state.ex_r = random.randint(5, 50)
        st.session_state.sol = st.session_state.ex_p * (1 - st.session_state.ex_r / 100)
    
    st.write(f"Défi : {st.session_state.ex_p}€ avec {st.session_state.ex_r}% de remise.")
    ans = st.number_input("Ta réponse :", key="ans")
    
    c1, c2 = st.columns(2)
    with c1:
        if st.button(T["check"]):
            if abs(ans - st.session_state.sol) < 0.1: st.success("✅ Bravo !")
            else: st.error(f"❌ La réponse était {st.session_state.sol:.2f}€")
    with c2:
        if st.button("🔄"):
            del st.session_state['ex_p']
            st.rerun()

