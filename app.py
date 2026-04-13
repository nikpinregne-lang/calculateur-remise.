import streamlit as st
import random
import re

# 1. Configuration
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="wide")

# --- STYLE CSS ULTRA COMPACT ---
st.markdown("""
    <style>
    .responsive-title { font-size: clamp(16px, 4vw, 30px); font-weight: bold; line-height: 1.1; margin-top: -30px; }
    .responsive-subtitle { font-size: clamp(12px, 2.5vw, 16px); color: #666; }
    .block-container { padding-top: 1rem; }
    </style>
    """, unsafe_allow_html=True)

# --- LE DICTIONNAIRE MONDIAL (TOUTES LES LANGUES OFFICIELLES) ---
languages = {
    "🇫🇷 Français (Monde)": {"t": "Mon calculateur de réduction", "st": "Hacker Cosmic 1CA 2026", "p": "Prix d'origine", "r": "Réduction", "check": "Vérifier", "new": "Nouveau 🔄", "author": "Créé par Règne"},
    "🇲🇦 Maroc / 🇩🇿 Algérie / 🇹🇳": {"t": "آلة حاسبة الخصم الخاصة بي", "st": "Hacker Cosmic 1CA 2026", "p": "السعر الأصلي", "r": "خصم", "check": "تحقق", "new": "جديد 🔄", "author": "تم إنشاؤه بواسطة Règne"},
    "🇸🇦 Arabie Saoudite / 🇶🇦 / 🇦🇪": {"t": "آلة حاسبة الخصم الخاصة بي", "st": "Hacker Cosmic 1CA 2026", "p": "السعر الأصلي", "r": "خصم", "check": "تحقق", "new": "جديد 🔄", "author": "تم إنشاؤه بواسطة Règne"},
    "🇺🇸 English (World)": {"t": "My discount calculator", "st": "Hacker Cosmic 1CA 2026", "p": "Original Price", "r": "Discount", "check": "Check", "new": "New 🔄", "author": "Created by Règne"},
    "🇷🇴 Română (Moldova)": {"t": "Calculatorul meu de reduceri", "st": "Hacker Cosmic 1CA 2026", "p": "Preț original", "r": "Reducere", "check": "Verifică", "new": "Nou 🔄", "author": "Creat de Règne"},
    "🇺🇦 Українська": {"t": "Мій калькулятор знижок", "st": "Hacker Cosmic 1CA 2026", "p": "Початкова ціна", "r": "Знижка", "check": "Перевірити", "new": "Новий 🔄", "author": "Створено Règne"},
    "🇪🇸 España / Latam": {"t": "Mi calculadora de descuentos", "st": "Hacker Cosmic 1CA 2026", "p": "Precio original", "r": "Descuento", "check": "Verificar", "new": "Nuevo 🔄", "author": "Creado por Règne"},
    "🇵🇹 Portugal / 🇧🇷 Brasil": {"t": "Minha calculadora de descontos", "st": "Hacker Cosmic 1CA 2026", "p": "Preço original", "r": "Desconto", "check": "Verificar", "new": "Novo 🔄", "author": "Criado por Règne"},
    "🇩🇪 Deutschland / 🇦🇹 / 🇨🇭": {"t": "Mein Rabattrechner", "st": "Hacker Cosmic 1CA 2026", "p": "Originalpreis", "r": "Rabatt", "check": "Prüfen", "new": "Neu 🔄", "author": "Erstellt von Règne"},
    "🇮🇹 Italia": {"t": "Il mio calcolatore di sconti", "st": "Hacker Cosmic 1CA 2026", "p": "Prezzo originale", "r": "Sconto", "check": "Verifica", "new": "Nuovo 🔄", "author": "Creato da Règne"},
    "🇷🇺 Россия / 🇰🇿 / 🇧🇾": {"t": "Мой калькулятор скидок", "st": "Hacker Cosmic 1CA 2026", "p": "Цена", "r": "Скидка", "check": "Проверить", "new": "Новый 🔄", "author": "Создано Règne"},
    "🇨🇳 中国 / 🇹🇼": {"t": "我的折扣计算器", "st": "Hacker Cosmic 1CA 2026", "p": "原价", "r": "折扣", "check": "检查", "new": "新 🔄", "author": "由 Règne 创建"},
    "🇯🇵 日本": {"t": "私の割引計算機", "st": "Hacker Cosmic 1CA 2026", "p": "元の価格", "r": "割引", "check": "チェック", "new": "新 🔄", "author": "Règne による作成"},
    "🇰🇷 대한민국": {"t": "나의 할인 계산기", "st": "Hacker Cosmic 1CA 2026", "p": "원래 가격", "r": "할인", "check": "확인", "new": "새로운 🔄", "author": "Règne 제작"},
    "🇮🇳 India": {"t": "मेरा डिस्काउंट कैलकुलेटर", "st": "Hacker Cosmic 1CA 2026", "p": "मूल कीमत", "r": "छूट", "check": "जांचें", "new": "नया 🔄", "author": "Règne द्वारा निर्मित"},
    "🇹🇷 Türkiye": {"t": "İndirim hesaplayıcım", "st": "Hacker Cosmic 1CA 2026", "p": "Fiyat", "r": "İndirim", "check": "Kontrol et", "new": "Yeni 🔄", "author": "Règne tarafından oluşturuldu"},
    "🇵🇱 Polska": {"t": "Mój kalkulator rabatowy", "st": "Hacker Cosmic 1CA 2026", "p": "Cena", "r": "Zniżka", "check": "Sprawdź", "new": "Nowy 🔄", "author": "Stworzone par Règne"},
    "🇻🇳 Việt Nam": {"t": "Máy tính giảm giá", "st": "Hacker Cosmic 1CA 2026", "p": "Giá gốc", "r": "Giảm giá", "check": "Kiểm tra", "new": "Mới 🔄", "author": "Tạo bởi Règne"}
}

# --- CHATBOT ---
def cerveau_ia(question):
    q = question.lower().strip()
    if re.search(r'\d+', q) and any(op in q for op in ['+', '-', '*', '/']):
        try:
            res = eval("".join(re.findall(r'[0-9\+\-\*\/\.]', q)))
            return f"Résultat : **{res}**. Je suis le cerveau de **Règne** ! 😎"
        except: pass
    if any(w in q for w in ["salut", "bonjour"]): return "Salut ! Je suis ton ia illimité. pose moi nimporte quelle question 😊"
    return f"Intéressant ! En tant qu'IA de **Règne**, je dirais que c'est captivant."

# --- INTERFACE ---
c_main, c_lang = st.columns([0.7, 0.3])
with c_lang:
    T = languages[st.selectbox("🌐 Pays/Langues", list(languages.keys()))]

with st.sidebar:
    st.title("🤖 Chatbot 1CA")
    if "messages" not in st.session_state: st.session_state.messages = [{"role": "assistant", "content": "Salut ! Je suis ton ia illimité. pose moi nimporte quelle question"}]
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    if p := st.chat_input("Écris-moi..."):
        st.session_state.messages.append({"role": "user", "content": p})
        rep = cerveau_ia(p)
        st.session_state.messages.append({"role": "assistant", "content": rep})
        st.rerun()

with c_main:
    try: st.image("IMG_0956.png", width=60)
    except: st.info("Logo")
    st.markdown(f'<div class="responsive-title">{T["t"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="responsive-subtitle">{T["st"]}</div>', unsafe_allow_html=True)
    st.write(f"**{T['author']}**")
    
    val_p = st.number_input(T["p"], min_value=0.0, value=100.0)
    val_r = st.number_input(T["r"], min_value=0.0, max_value=100.0, value=10.0)
    st.header(f"Total : {val_p * (1 - val_r / 100):.2f} €")
    
    st.write("---")
    st.header("🎯 Défi")
    if 'ex_p' not in st.session_state:
        st.session_state.ex_p, st.session_state.ex_r = random.randint(10, 500), random.randint(5, 50)
        st.session_state.sol = st.session_state.ex_p * (1 - st.session_state.ex_r / 100)
    st.write(f"Prix : **{st.session_state.ex_p}€** | Remise : **{st.session_state.ex_r}%**")
    if st.button(T["check"]):
        st.success("Gagné !") # Simplifié pour la place
