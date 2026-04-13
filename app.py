import streamlit as st
import random
import re

# 1. Configuration de la page
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="wide")

# --- DICTIONNAIRE DES LANGUES NATIONALES ÉLARGI (LE PLUS COMPLET) ---
languages = {
    "🇫🇷 Français": {"t": "Mon calculateur de réduction", "st": "Hacker Cosmic 1CA 2026", "p": "Prix d'origine", "r": "Réduction", "check": "Vérifier", "new": "Nouveau 🔄", "author": "Créé par Règne"},
    "🇲🇦 Maroc": {"t": "آلة حاسبة الخصم الخاصة بي", "st": "Hacker Cosmic 1CA 2026", "p": "السعر الأصلي", "r": "خصم", "check": "تحقق", "new": "جديد 🔄", "author": "تم إنشاؤه بواسطة Règne"},
    "🇸🇦 Arabie Saoudite": {"t": "آلة حاسبة الخصم الخاصة بي", "st": "Hacker Cosmic 1CA 2026", "p": "السعر الأصلي", "r": "خصم", "check": "تحقق", "new": "جديد 🔄", "author": "تم إنشاؤه بواسطة Règne"},
    "🇩🇿 Algérie": {"t": "آلة حاسبة الخصم الخاصة بي", "st": "Hacker Cosmic 1CA 2026", "p": "السعر الأصلي", "r": "خصم", "check": "تحقق", "new": "جديد 🔄", "author": "تم إنشاؤه بواسطة Règne"},
    "🇹🇳 Tunisie": {"t": "آلة حاسبة الخصم الخاصة بي", "st": "Hacker Cosmic 1CA 2026", "p": "السعر الأصلي", "r": "خصم", "check": "تحقق", "new": "جديد 🔄", "author": "تم إنشاؤه بواسطة Règne"},
    "🇷🇴 Română": {"t": "Calculatorul meu de reduceri", "st": "Hacker Cosmic 1CA 2026", "p": "Preț original", "r": "Reducere", "check": "Verifică", "new": "Nou 🔄", "author": "Creat de Règne"},
    "🇺🇦 Українська": {"t": "Мій калькулятор знижок", "st": "Hacker Cosmic 1CA 2026", "p": "Початкова ціна", "r": "Знижка", "check": "Перевірити", "new": "Новий 🔄", "author": "Створено Règne"},
    "🇺🇸 English": {"t": "My discount calculator", "st": "Hacker Cosmic 1CA 2026", "p": "Original Price", "r": "Discount", "check": "Check", "new": "New 🔄", "author": "Created by Règne"},
    "🇪🇸 España": {"t": "Mi calculadora de descuentos", "st": "Hacker Cosmic 1CA 2026", "p": "Precio original", "r": "Descuento", "check": "Verificar", "new": "Nuevo 🔄", "author": "Creado por Règne"},
    "🇵🇹 Portugal": {"t": "Minha calculadora de descontos", "st": "Hacker Cosmic 1CA 2026", "p": "Preço original", "r": "Desconto", "check": "Verificar", "new": "Novo 🔄", "author": "Criado por Règne"},
    "🇧🇷 Brasil": {"t": "Minha calculadora de descontos", "st": "Hacker Cosmic 1CA 2026", "p": "Preço original", "r": "Desconto", "check": "Verificar", "new": "Novo 🔄", "author": "Criado por Règne"},
    "🇮🇹 Italia": {"t": "Il mio calcolatore di sconti", "st": "Hacker Cosmic 1CA 2026", "p": "Prezzo originale", "r": "Sconto", "check": "Verifica", "new": "Nuovo 🔄", "author": "Creato da Règne"},
    "🇩🇪 Deutschland": {"t": "Mein Rabattrechner", "st": "Hacker Cosmic 1CA 2026", "p": "Originalpreis", "r": "Rabatt", "check": "Prüfen", "new": "Neu 🔄", "author": "Erstellt von Règne"},
    "🇵🇱 Polska": {"t": "Mój kalkulator rabatowy", "st": "Hacker Cosmic 1CA 2026", "p": "Cena", "r": "Zniżka", "check": "Sprawdź", "new": "Nowy 🔄", "author": "Stworzone przez Règne"},
    "🇹🇷 Türkiye": {"t": "İndirim hesaplayıcım", "st": "Hacker Cosmic 1CA 2026", "p": "Fiyat", "r": "İndirim", "check": "Kontrol et", "new": "Yeni 🔄", "author": "Règne tarafından oluşturuldu"},
    "🇨🇳 中国 (中文)": {"t": "我的折扣计算器", "st": "Hacker Cosmic 1CA 2026", "p": "原价", "r": "折扣", "check": "检查", "new": "新 🔄", "author": "由 Règne 创建"},
    "🇯🇵 日本 (日本語)": {"t": "私の割引計算機", "st": "Hacker Cosmic 1CA 2026", "p": "元の価格", "r": "割引", "check": "チェック", "new": "新 🔄", "author": "Règne による作成"},
    "🇰🇷 대한민국 (한국어)": {"t": "나의 할인 계산기", "st": "Hacker Cosmic 1CA 2026", "p": "원래 가격", "r": "할인", "check": "확인", "new": "새로운 🔄", "author": "Règne 제작"},
    "🇷🇺 Россия": {"t": "Мой калькулятор скидок", "st": "Hacker Cosmic 1CA 2026", "p": "Цена", "r": "Скидка", "check": "Проверить", "new": "Новый 🔄", "author": "Создано Règne"},
    "🇮🇳 India (हिन्दी)": {"t": "मेरा डिस्काउंट कैलकुलेटर", "st": "Hacker Cosmic 1CA 2026", "p": "मूल कीमत", "r": "छूट", "check": "जांचें", "new": "नया 🔄", "author": "Règne द्वारा निर्मित"}
}

# --- CERVEAU DU CHATBOT ILLIMITÉ ---
def cerveau_ia(question):
    q = question.lower().strip()
    if re.search(r'\d+', q) and any(op in q for op in ['+', '-', '*', '/']):
        try:
            calcul = "".join(re.findall(r'[0-9\+\-\*\/\.]', q))
            return f"Après analyse, **{calcul} est égal à {eval(calcul)}**. Pas mal, non ? 😎"
        except: pass
    if any(word in q for word in ["salut", "bonjour", "hello"]):
        return "Salut ! Je suis ton ia illimité. pose moi nimporte quelle question 😊"
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
    
    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])

    if prompt := st.chat_input("Écris-moi..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        rep = cerveau_ia(prompt)
        st.session_state.messages.append({"role": "assistant", "content": rep})
        st.rerun()

with col_main:
    try: st.image("IMG_0956.png", width=130)
    except: st.info("Logo Hacker Cosmic")
    
    # TITRE SUR UNE SEULE LIGNE ET SOUS-TITRE
    st.markdown(f"# {T['t']}")
    st.subheader(T["st"])
    st.write(f"### {T['author']}")
    st.write("---")
    
    # CALCULATEUR
    p = st.number_input(T["p"], min_value=0.0, value=100.0)
    r = st.number_input(T["r"], min_value=0.0, max_value=100.0, value=10.0)
    st.header(f"Total : {p * (1 - r / 100):.2f} €")
    
    st.write("---")
    
    # DÉFI MATHÉMATIQUE
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
