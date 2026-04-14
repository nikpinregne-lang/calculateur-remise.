import streamlit as st
import random
import re

# 1. Configuration GOAT
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="wide")

# --- SYSTÈME DE TRADUCTION INTÉGRAL (Tout change selon le pays) ---
LANGS = {
    "FR": {"calc": "Mon calculateur de réduction", "orig": "Prix d'origine (€)", "rem": "Remise (%)", "defi": "🎯 Défi du Hacker", "score": "Score", "check": "Vérifier", "win": "✅ GAGNÉ !", "lost": "❌ FAUX !", "visit": "Hackers ont visité !"},
    "AR": {"calc": "حاسبة الخصم الخاصة بي", "orig": "السعر الأصلي", "rem": "خصم (%)", "defi": "🎯 تحدي الهكر", "score": "نتيجة", "check": "تحقق", "win": "✅ فزت!", "lost": "❌ خطأ!", "visit": "هكر زاروا الموقع"},
    "EN": {"calc": "My Discount Calculator", "orig": "Original Price (€)", "rem": "Discount (%)", "defi": "🎯 Hacker Challenge", "score": "Score", "check": "Check", "win": "✅ WON!", "lost": "❌ WRONG!", "visit": "Hackers visited!"},
    "RO": {"calc": "Calculator de reduceri", "orig": "Preț original", "rem": "Reducere", "defi": "🎯 Provocare", "score": "Scor", "check": "Verifică", "win": "✅ CÂȘTIGAT!", "lost": "❌ GREȘIT!", "visit": "Hackeri au vizitat!"},
    "UA": {"calc": "Калькулятор знижок", "orig": "Початкова ціна", "rem": "Знижка", "defi": "🎯 Виклик хакера", "score": "Рахунок", "check": "Перевірити", "win": "✅ ПЕРЕМОГА!", "lost": "❌ ПОМИЛКА!", "visit": "Хакери відвідали!"},
    "TR": {"calc": "İndirim Hesaplayıcı", "orig": "Orijinal Fiyat", "rem": "İndirim", "defi": "🎯 Hacker Meydan Okuması", "score": "Puan", "check": "Kontrol Et", "win": "✅ KAZANDIN!", "lost": "❌ YANLIŞ!", "visit": "Hacker ziyaret etti!"}
}

# --- LISTE GÉANTE DE TOUS LES PAYS ---
pays_complet = [
    "🇫🇷 France", "🇲🇦 Maroc", "🇩🇿 Algérie", "🇸🇦 Arabie Saoudite", "🇧🇪 Belgique", "🇷🇴 Roumanie", 
    "🇺🇦 Ukraine", "🇹🇷 Turquie", "🇺🇸 USA", "🇨🇦 Canada", "🇨🇭 Suisse", "🇮🇹 Italie", 
    "🇪🇸 Espagne", "🇵🇹 Portugal", "🇩🇪 Allemagne", "🇬🇧 UK", "🇧🇷 Brésil", "🇯🇵 Japon"
]

# --- CERVEAU IA ILLIMITÉ (RÉPOND À TOUT) ---
def cerveau_ia_goat(question):
    q = question.lower().strip()
    if q == "." or q == "?" or q == "!": return "Même un simple signe a du sens pour un Hacker. Dis-m'en plus ! 💻"
    if "wesh" in q: return "Wesh ! Bien ou quoi ? Je suis l'IA de **Règne**, on gère le game. 😎"
    if "qui" in q and "cree" in q: return "Le seul et unique patron ici, c'est **Règne**. 👑"
    
    # Calculs
    if re.search(r'\d+', q) and any(op in q for op in ['+', '-', '*', '/']):
        try: return f"Calcul direct : **{eval(''.join(re.findall(r'[0-9\+\-\*\/\.]', q)))}**. Simple. 🧠"
        except: pass
        
    return f"Écoute, '{question}', c'est un bon sujet. En tant qu'IA de **Règne**, je te dirais de foncer. T'as d'autres questions ?"

# --- INTERFACE ---
col_main, col_lang = st.columns([0.8, 0.2])

with col_lang:
    choix = st.selectbox("🌐 Pays / Language", pays_complet)
    if any(p in choix for p in ["France", "Maroc", "Algérie", "Belgique"]): T = LANGS["FR"]
    elif "Arabie" in choix: T = LANGS["AR"]
    elif "Roumanie" in choix: T = LANGS["RO"]
    elif "Ukraine" in choix: T = LANGS["UA"]
    elif "Turquie" in choix: T = LANGS["TR"]
    else: T = LANGS["EN"]

with st.sidebar:
    st.title("🤖 Chatbot 1CA")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Wesh ! Je réponds à TOUT. Teste-moi."}]
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    if prompt := st.chat_input("Dis-moi n'importe quoi..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        rep = cerveau_ia_goat(prompt)
        with st.chat_message("assistant"): st.markdown(rep)
        st.session_state.messages.append({"role": "assistant", "content": rep})

with col_main:
    st.image("IMG_0956.png", width=120)
    st.header(T["calc"])
    st.title("Hacker Cosmic 1CA 2026")
    st.markdown("### Créé par **Règne**")
    st.write("---")

    # CALCULATEUR
    p_orig = st.number_input(T["orig"], value=460.0)
    remise = st.number_input(T["rem"], value=10.0)
    st.header(f"{T['total']} : {p_orig * (1 - remise/100):.2f} €")
    
    st.write("---")

    # DÉFI (EXERCICE)
    st.header(T["defi"])
    if 'score' not in st.session_state: st.session_state.score = 0
    if 'ex_p' not in st.session_state:
        st.session_state.ex_p, st.session_state.ex_r = random.randint(10, 500), random.randint(5, 50)
        st.session_state.sol = st.session_state.ex_p * (1 - st.session_state.ex_r / 100)

    st.write(f"**{T['score']} : {st.session_state.score} ⭐**")
    st.write(f"DÉFI : {st.session_state.ex_p}€ avec {st.session_state.ex_r}% de remise.")
    ans = st.number_input(T["check"], key="ans_input", value=0.0)
    
    if st.button(T["check"]):
        if abs(ans - st.session_state.sol) < 0.1:
            st.success(T["win"])
            st.session_state.score += 1
            del st.session_state['ex_p']
            st.rerun()
        else:
            st.error(T["lost"])
            st.session_state.score = 0

    if 'v' not in st.session_state: st.session_state.v = 12
    st.session_state.v += 1
    st.write(f"🔥 **{st.session_state.v} {T['visit']}**")
