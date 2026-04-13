import streamlit as st
import random
import re

# 1. Configuration de la page
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="wide")

# --- STYLE CSS (TEXTES ADAPTATIFS ET ESPACEMENT) ---
st.markdown("""
    <style>
    .responsive-title { font-size: clamp(18px, 4vw, 34px); font-weight: bold; line-height: 1.1; margin-bottom: 5px; }
    .responsive-subtitle { font-size: clamp(14px, 2.5vw, 18px); color: #666; margin-bottom: 5px; }
    .block-container { padding-top: 1.5rem; }
    </style>
    """, unsafe_allow_html=True)

# --- DICTIONNAIRE MONDIAL (TOUTES LES LANGUES NATIONALES OFFICIELLES) ---
languages = {
    "🇫🇷 France / Monde": {"t": "Mon calculateur de réduction", "st": "Hacker Cosmic 1CA 2026", "p": "Prix d'origine", "r": "Réduction", "check": "Vérifier", "new": "Nouveau Défi 🔄", "author": "Créé par Règne"},
    "🇲🇦 Maroc / 🇩🇿 Algérie / 🇹🇳": {"t": "آلة حاسبة الخصم", "st": "Hacker Cosmic 1CA 2026", "p": "السعر الأصلي", "r": "خصم", "check": "تحقق", "new": "تحدي جديد 🔄", "author": "تم إنشاؤه بواسطة Règne"},
    "🇸🇦 Arabie Saoudite / 🇶🇦 / 🇦🇪": {"t": "آلة حاسبة الخصم", "st": "Hacker Cosmic 1CA 2026", "p": "السعر الأصلي", "r": "خصم", "check": "تحقق", "new": "تحدي جديد 🔄", "author": "تم إنشاؤه بواسطة Règne"},
    "🇺🇸 USA / UK / World": {"t": "My discount calculator", "st": "Hacker Cosmic 1CA 2026", "p": "Original Price", "r": "Discount", "check": "Check", "new": "New Challenge 🔄", "author": "Created by Règne"},
    "🇷🇴 România / 🇲🇩 Moldova": {"t": "Calculator de reduceri", "st": "Hacker Cosmic 1CA 2026", "p": "Preț original", "r": "Reducere", "check": "Verifică", "new": "Nou 🔄", "author": "Creat de Règne"},
    "🇺🇦 Україна (Ukraine)": {"t": "Калькулятор знижок", "st": "Hacker Cosmic 1CA 2026", "p": "Початкова ціна", "r": "Знижка", "check": "Перевірити", "new": "Новий 🔄", "author": "Створено Règne"},
    "🇪🇸 España / Latam": {"t": "Calculadora de descuentos", "st": "Hacker Cosmic 1CA 2026", "p": "Precio original", "r": "Descuento", "check": "Verificar", "new": "Nuevo 🔄", "author": "Creado por Règne"},
    "🇵🇹 Portugal / 🇧🇷 Brasil": {"t": "Calculadora de descontos", "st": "Hacker Cosmic 1CA 2026", "p": "Preço original", "r": "Desconto", "check": "Verificar", "new": "Novo 🔄", "author": "Criado por Règne"},
    "🇮🇹 Italia": {"t": "Calcolatore sconti", "st": "Hacker Cosmic 1CA 2026", "p": "Prezzo originale", "r": "Sconto", "check": "Verifica", "new": "Nuovo 🔄", "author": "Creato da Règne"},
    "🇩🇪 Deutschland / 🇦🇹 / 🇨🇭": {"t": "Rabattrechner", "st": "Hacker Cosmic 1CA 2026", "p": "Originalpreis", "r": "Rabatt", "check": "Prüfen", "new": "Neu 🔄", "author": "Erstellt von Règne"},
    "🇵🇱 Polska": {"t": "Mój kalkulator rabatowy", "st": "Hacker Cosmic 1CA 2026", "p": "Cena", "r": "Zniżka", "check": "Sprawdź", "new": "Nowy 🔄", "author": "Stworzone przez Règne"},
    "🇹🇷 Türkiye": {"t": "İndirim hesaplayıcı", "st": "Hacker Cosmic 1CA 2026", "p": "Fiyat", "r": "İndirim", "check": "Kontrol et", "new": "Yeni 🔄", "author": "Règne tarafından oluşturuldu"},
    "🇨🇳 中国 (Chine)": {"t": "折扣计算器", "st": "Hacker Cosmic 1CA 2026", "p": "原价", "r": "折扣", "check": "检查", "new": "新 🔄", "author": "由 Règne 创建"},
    "🇯🇵 日本 (Japon)": {"t": "割引計算機", "st": "Hacker Cosmic 1CA 2026", "p": "元の価格", "r": "割引", "check": "チェック", "new": "新 🔄", "author": "Règne による作成"},
    "🇰🇷 대한민국 (Corée)": {"t": "나의 할인 계산기", "st": "Hacker Cosmic 1CA 2026", "p": "원래 가격", "r": "할인", "check": "확인", "new": "새로운 🔄", "author": "Règne 제작"},
    "🇷🇺 Россия (Russie)": {"t": "Мой калькулятор скидок", "st": "Hacker Cosmic 1CA 2026", "p": "Цена", "r": "Скидка", "check": "Проверить", "new": "Новый 🔄", "author": "Создано Règne"},
    "🇮🇳 India (Hindi)": {"t": "डिस्काउंट कैलकुलेटर", "st": "Hacker Cosmic 1CA 2026", "p": "मूल कीमत", "r": "छूट", "check": "जांचें", "new": "नया 🔄", "author": "Règne द्वारा निर्मित"},
    "🇻🇳 Việt Nam": {"t": "Máy tính giảm giá", "st": "Hacker Cosmic 1CA 2026", "p": "Giá gốc", "r": "Giảm giá", "check": "Kiểm tra", "new": "Mới 🔄", "author": "Tạo bởi Règne"}
}

# --- CERVEAU DU CHATBOT ---
def cerveau_ia(question):
    q = question.lower().strip()
    if re.search(r'\d+', q) and any(op in q for op in ['+', '-', '*', '/']):
        try:
            res = eval("".join(re.findall(r'[0-9\+\-\*\/\.]', q)))
            return f"Après analyse : **{res}**. Je suis l'IA de Règne ! 😎"
        except: pass
    if any(w in q for w in ["salut", "bonjour"]): return "Salut ! Je suis ton ia illimité. pose moi nimporte quelle question 😊"
    return f"En tant qu'IA de **Règne**, je trouve que '{question}' est fascinant !"

# --- INTERFACE ---
c_main, c_lang = st.columns([0.75, 0.25])
with c_lang:
    sel_lang = st.selectbox("🌐 Choisi ton Pays / Langue", list(languages.keys()))
    T = languages[sel_lang]

with st.sidebar:
    st.title("🤖 Chatbot 1CA")
    st.write("Assistant de **Règne**")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Salut ! Je suis ton ia illimité. pose moi nimporte quelle question"}]
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    if p := st.chat_input("Écris-moi..."):
        st.session_state.messages.append({"role": "user", "content": p})
        rep = cerveau_ia(p)
        st.session_state.messages.append({"role": "assistant", "content": rep})
        st.rerun()

with c_main:
    # TITRES ET AUTEUR
    st.markdown(f'<div class="responsive-title">{T["t"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="responsive-subtitle">{T["st"]}</div>', unsafe_allow_html=True)
    st.write(f"**{T['author']}**")

    # LOGO DESCENDU (Bien visible au centre de la présentation)
    st.write("") 
    try: st.image("IMG_0956.png", width=100)
    except: st.write("📷")
    st.write("---")
    
    # CALCULATEUR
    val_p = st.number_input(T["p"] + " (€)", min_value=0.0, value=100.0, step=1.0)
    val_r = st.number_input(T["r"] + " (%)", min_value=0.0, max_value=100.0, value=10.0, step=1.0)
    st.header(f"Total : {val_p * (1 - val_r / 100):.2f} €")
    
    st.write("---")
    
    # SECTION DÉFI
    st.header("🎯 Défi")
    if 'ex_p' not in st.session_state:
        st.session_state.ex_p = random.randint(20, 500)
        st.session_state.ex_r = random.choice([5, 10, 15, 20, 25, 30, 40, 50])
        st.session_state.sol = st.session_state.ex_p * (1 - st.session_state.ex_r / 100)

    st.write(f"Prix : **{st.session_state.ex_p}€** | Remise : **{st.session_state.ex_r}%**")
    reponse_user = st.number_input("Ta réponse (€)", min_value=0.0, step=0.01, key="defi_input")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button(T["check"]):
            if abs(reponse_user - st.session_state.sol) < 0.1: st.success("✅ Bravo !")
            else: st.error(f"❌ Faux ! C'était {st.session_state.sol:.2f}€")
    with col2:
        if st.button(T["new"]):
            del st.session_state['ex_p']
            st.rerun()
