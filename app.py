import streamlit as st
import random
import re

# 1. CONFIGURATION ET STYLE
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="wide")

# --- DICTIONNAIRE DE TRADUCTION UNIVERSEL (TOUTES LES LANGUES) ---
# Chaque langue change les titres, le calculateur et le défi
LANGS = {
    "Français 🇫🇷": {"calc": "Mon calculateur de réduction", "orig": "Prix d'origine (€)", "rem": "Remise (%)", "defi": "🎯 Défi du Hacker", "score": "Score", "check": "Vérifier", "win": "✅ GAGNÉ !", "lost": "❌ FAUX !", "visit": "Hackers ont visité !"},
    "English 🇺🇸": {"calc": "My Discount Calculator", "orig": "Original Price (€)", "rem": "Discount (%)", "defi": "🎯 Hacker Challenge", "score": "Score", "check": "Check", "win": "✅ WON!", "lost": "❌ WRONG!", "visit": "Hackers visited!"},
    "Maroc 🇲🇦 (Arabe)": {"calc": "حاسبة الخصم الخاصة بي", "orig": "السعر الأصلي", "rem": "خصم (%)", "defi": "🎯 تحدي الهكر", "score": "نتيجة", "check": "تحقق", "win": "✅ فزت!", "lost": "❌ خطأ!", "visit": "هكر زاروا الموقع"},
    "Saudi Arabia 🇸🇦": {"calc": "حاسبة الخصم الخاصة بي", "orig": "السعر الأصلي", "rem": "خصم (%)", "defi": "🎯 تحدي الهكر", "score": "نتيجة", "check": "تحقق", "win": "✅ فزت!", "lost": "❌ خطأ!", "visit": "هكر زاروا الموقع"},
    "Română 🇷🇴": {"calc": "Calculator de reduceri", "orig": "Preț original", "rem": "Reducere", "defi": "🎯 Provocarea Hackerului", "score": "Scor", "check": "Verifică", "win": "✅ CÂȘTIGAT!", "lost": "❌ GREȘIT!", "visit": "Hackeri au vizitat!"},
    "Türkiye 🇹🇷": {"calc": "İndirim Hesaplayıcı", "orig": "Orijinal Fiyat", "rem": "İndirim", "defi": "🎯 Hacker Meydan Okuması", "score": "Puan", "check": "Kontrol Et", "win": "✅ KAZANDIN!", "lost": "❌ YANLIŞ!", "visit": "Hacker ziyaret etti!"},
    "Ukraine 🇺🇦": {"calc": "Калькулятор знижок", "orig": "Початкова ціна", "rem": "Знижка", "defi": "🎯 Виклик хакера", "score": "Рахунок", "check": "Перевірити", "win": "✅ ПЕРЕМОГА!", "lost": "❌ ПОМИЛКА!", "visit": "Хакери відвідали!"},
    "Belgique 🇧🇪": {"calc": "Mon calculateur de réduction", "orig": "Prix d'origine", "rem": "Remise", "defi": "🎯 Défi Hacker", "score": "Points", "check": "Vérifier", "win": "✅ BRAVO !", "lost": "❌ FAUX !", "visit": "Visiteurs !"}
}

# --- CERVEAU IA ILLIMITÉ (RÉPOND À TOUT COMME UN GOAT) ---
def cerveau_ia_goat(question):
    q = question.lower().strip()
    
    # 1. Réponse aux signes ( . ? ! )
    if q in [".", "?", "!"]: return "Même un signe a du style ici ! Pose-moi une vraie question, je suis prêt. 😎"
    
    # 2. Salutations et politesse
    if any(s in q for s in ["wesh", "wsh", "bien ou quoi"]): return "Wesh ! Bien ou quoi ? Je suis l'IA de **Règne**, on gère le système ensemble. 🤝"
    if any(s in q for s in ["salut", "bonjour", "hello", "sava", "ça va"]): return "Salut ! Je vais super bien, boosté à l'énergie de **Règne**. Et toi ? 😊"
    if "merci" in q: return "Normal ! Entre légendes, on s'entraide. 😉"

    # 3. Calculs directs (1+1, 5*5, etc.)
    if re.search(r'\d+', q) and any(op in q for op in ['+', '-', '*', '/']):
        try:
            calcul = "".join(re.findall(r'[0-9\+\-\*\/\.]', q))
            return f"Après analyse : **{calcul} = {eval(calcul)}**. Trop facile ! 🧠"
        except: pass

    # 4. Culture G (Capitales, Définitions)
    if "bonbon" in q: return "Le bonbon est une confiserie sucrée. Miam, mais attention aux dents ! 🍬"
    if "qui" in q and "cree" in q: return "Le seul et unique créateur, c'est le GOAT **Règne**. 👑"
    if "australie" in q: return "La capitale c'est **Canberra** 🇦🇺 !"
    if "belgique" in q: return "La capitale c'est **Bruxelles** 🇧🇪 !"

    # 5. Réponse Libre (Si l'IA ne sait pas, elle discute vraiment)
    return f"Franchement, ta question sur '{question}' est super stylée. En tant qu'IA, je trouve ça fascinant. Dis-m'en plus ! 😉"

# --- INTERFACE ---
col_main, col_lang = st.columns([0.8, 0.2])

with col_lang:
    # Menu des pays qui traduit TOUT le site
    choix_pays = st.selectbox("🌐 Pays / Language", list(LANGS.keys()))
    T = LANGS[choix_pays]

with st.sidebar:
    st.title("🤖 Chatbot 1CA")
    st.write(f"Assistant du GOAT : **Règne**")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Wesh ! Pose-moi n'importe quelle question, je réponds à TOUT."}]
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    if prompt := st.chat_input("Demande-moi n'importe quoi..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        rep = cerveau_ia_goat(prompt)
        with st.chat_message("assistant"): st.markdown(rep)
        st.session_state.messages.append({"role": "assistant", "content": rep})

with col_main:
    # LOGO ET TITRES
    try: st.image("IMG_0956.png", width=120)
    except: st.info("Logo Hacker Cosmic")
    
    st.header(T["calc"])
    st.title("Hacker Cosmic 1CA 2026")
    st.markdown("### Créé par **Règne**")
    st.write("---")

    # CALCULATEUR
    p_orig = st.number_input(T["orig"], value=460.0)
    remise = st.number_input(T["rem"], value=10.0)
    st.header(f"{T['total']} : {p_orig * (1 - remise/100):.2f} €")
    
    st.write("---")

    # DÉFI HACKER (L'EXERCICE AVEC SCORE)
    st.header(T["defi"])
    if 'score' not in st.session_state: st.session_state.score = 0
    if 'ex_p' not in st.session_state:
        st.session_state.ex_p = random.randint(10, 500)
        st.session_state.ex_r = random.randint(5, 50)
        st.session_state.sol = st.session_state.ex_p * (1 - st.session_state.ex_r / 100)

    st.write(f"**{T['score']} : {st.session_state.score} ⭐**")
    st.write(f"DÉFI : {st.session_state.ex_p}€ avec {st.session_state.ex_r}% de remise.")
    ans = st.number_input(T["check"], key="ans_input", value=0.0)
    
    c1, c2 = st.columns(2)
    with c1:
        if st.button(T["check"]):
            if abs(ans - st.session_state.sol) < 0.1:
                st.success(T["win"])
                st.session_state.score += 1
                del st.session_state['ex_p']
                st.rerun()
            else:
                st.error(f"{T['lost']} (Réponse: {st.session_state.sol:.2f}€)")
                st.session_state.score = 0
    with c2:
        if st.button("🔄"):
            del st.session_state['ex_p']
            st.rerun()

    # COMPTEUR DE VISITES
    if 'v' not in st.session_state: st.session_state.v = 15
    st.session_state.v += 1
    st.write(f"🔥 **{st.session_state.v} {T['visit']}**")
