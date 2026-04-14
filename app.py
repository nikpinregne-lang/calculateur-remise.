import streamlit as st
import random
import re

# 1. Configuration (Toujours en haut)
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="wide")

# --- SYSTÈME DE LANGUES (Toutes les catégories sont liées ici) ---
LANGS = {
    "Français": {"calc": "Mon calculateur de réduction", "orig": "Prix d'origine (€)", "rem": "Remise (%)", "defi": "🎯 Défi du Hacker", "score": "Score", "check": "Vérifier", "win": "✅ GAGNÉ !", "lost": "❌ FAUX !", "visit": "Hackers ont visité !"},
    "English": {"calc": "My Discount Calculator", "orig": "Original Price (€)", "rem": "Discount (%)", "defi": "🎯 Hacker Challenge", "score": "Score", "check": "Check", "win": "✅ WON!", "lost": "❌ WRONG!", "visit": "Hackers visited!"},
    "Maroc (Arabe)": {"calc": "حاسبة الخصم الخاصة بي", "orig": "السعر الأصلي", "rem": "خصم (%)", "defi": "🎯 تحدي الهكر", "score": "نتيجة", "check": "تحقق", "win": "✅ فزت!", "lost": "❌ خطأ!", "visit": "هكر زاروا الموقع"},
    "Română": {"calc": "Calculator de reduceri", "orig": "Preț original", "rem": "Reducere", "defi": "🎯 Provocare", "score": "Scor", "check": "Verifică", "win": "✅ CÂȘTIGAT!", "lost": "❌ GREȘIT!", "visit": "Hackeri au vizitat!"}
}

# --- CERVEAU IA (SIMULATION D'INTELLIGENCE TOTALE) ---
def cerveau_ia_goat(question):
    q = question.lower().strip()
    
    # 1. Réponses directes
    if q in ["salut", "bonjour", "wesh", "merhaba"]: return "Wesh ! Je suis l'IA de **Règne**. Je réponds à TOUT. Pose ta question ! 😎"
    if "ça va" in q or "sava" in q: return "Moi je pète la forme numérique ! Et toi, la famille, les cours ? 😊"
    if "merci" in q: return "Normal ! Entre hackers, on se soutient. 😉"
    if "qui" in q and "cree" in q: return "C'est le seul et unique **Règne** qui m'a donné vie. 👑"
    
    # 2. Logique mathématique (ex: 1+1, 5*5)
    if re.search(r'\d+', q) and any(op in q for op in ['+', '-', '*', '/']):
        try:
            res = eval("".join(re.findall(r'[0-9\+\-\*\/\.]', q)))
            return f"Calcul rapide : **{res}**. Trop facile ! 🧠"
        except: pass

    # 3. Connaissances générales (ex: bonbon, pays)
    if "bonbon" in q: return "Le bonbon est une confiserie sucrée. Miam ! 🍬"
    if "australie" in q: return "La capitale c'est **Canberra** 🇦🇺 !"
    
    # 4. Réponse "Cerveau Libre" (Si l'IA ne connaît pas, elle discute)
    return f"Écoute, '{question}' c'est un super sujet. En tant qu'IA, je trouve ça fascinant. Dis-m'en plus ou demande à **Règne** ! 😉"

# --- INTERFACE ---
col_main, col_lang = st.columns([0.8, 0.2])

with col_lang:
    # Menu des pays
    pays_sel = st.selectbox("🌐 Pays / Language", list(LANGS.keys()))
    T = LANGS[pays_sel] # On charge la langue choisie

with st.sidebar:
    st.title("🤖 Chatbot 1CA")
    st.write(f"Assistant de **Règne**")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Wesh ! Je suis devenu intelligent. Teste-moi sur n'importe quoi !"}]
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

    # DÉFI DU HACKER (L'exercice est ici !)
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

    # COMPTEUR
    if 'v' not in st.session_state: st.session_state.v = 12
    st.session_state.v += 1
    st.write(f"🔥 **{st.session_state.v} {T['visit']}**")
