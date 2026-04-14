import streamlit as st
import random
import re

# 1. CONFIGURATION ET STYLE
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="wide")

# --- SYSTÈME DE TRADUCTION INTÉGRAL (Le cœur du site) ---
LANGS = {
    "Français": {
        "calc": "Mon calculateur de réduction", "orig": "Prix d'origine (€)", "rem": "Remise (%)", 
        "total": "Total après réduction", "defi": "🎯 Défi du Hacker", "score": "Score", 
        "check": "Vérifier", "win": "✅ GAGNÉ !", "lost": "❌ FAUX !", "visit": "Hackers ont visité !"
    },
    "English": {
        "calc": "My Discount Calculator", "orig": "Original Price (€)", "rem": "Discount (%)", 
        "total": "Total after discount", "defi": "🎯 Hacker Challenge", "score": "Score", 
        "check": "Check", "win": "✅ WON!", "lost": "❌ WRONG!", "visit": "Hackers visited!"
    },
    "Maroc (Arabe)": {
        "calc": "حاسبة الخصم الخاصة بي", "orig": "السعر الأصلي", "rem": "خصم (%)", 
        "total": "المجموع بعد الخصم", "defi": "🎯 تحدي الهكر", "score": "نتيجة", 
        "check": "تحقق", "win": "✅ فزت!", "lost": "❌ خطأ!", "visit": "هكر زاروا الموقع"
    },
    "Română": {
        "calc": "Calculatorul de reduceri", "orig": "Preț original", "rem": "Reducere", 
        "total": "Total după reducere", "defi": "🎯 Provocarea Hackerului", "score": "Scor", 
        "check": "Verifică", "win": "✅ CÂȘTIGAT!", "lost": "❌ GREȘIT!", "visit": "Hackeri au vizitat!"
    }
}

# --- CERVEAU IA GOAT (RÉPOND À TOUT SANS LIMITES) ---
def cerveau_ia_goat(question):
    q = question.lower().strip()
    
    # 1. Salutations et politesse (Le chatbot est cool)
    if q in ["salut", "bonjour", "wesh", "merhaba", "sava", "ça va"]:
        return random.choice(["Wesh ! Bien ou quoi ? Pose ta question, je gère. 😎", "Salut ! Je suis prêt pour tes défis.", "Hello ! On calcule quoi aujourd'hui ?"])
    
    if "bien" in q and ("et toi" in q or "et vous" in q):
        return "Moi je pète la forme numérique grâce au code de **Règne** ! 🚀"

    # 2. Logique Mathématique (ex: 1+1, 15*3)
    if re.search(r'\d+', q) and any(op in q for op in ['+', '-', '*', '/']):
        try:
            res = eval("".join(re.findall(r'[0-9\+\-\*\/\.]', q)))
            return f"Après calcul cosmique : **{res}**. Trop facile ! 🧠"
        except: pass

    # 3. Culture et Définitions (Répond à tout)
    connaissances = {
        "bonbon": "Une sucrerie délicieuse faite de sucre. Attention aux dents de hacker ! 🍬",
        "qui": "Le seul et unique créateur ici, c'est le GOAT **Règne**. 👑",
        "belgique": "La capitale est **Bruxelles** 🇧🇪.",
        "maroc": "La capitale est **Rabat** 🇲🇦.",
        "australie": "La capitale est **Canberra** 🇦🇺.",
        "france": "C'est **Paris** 🇫🇷."
    }
    for mot, rep in connaissances.items():
        if mot in q: return rep

    # 4. Réponse libre (Si l'IA ne sait pas, elle improvise avec style)
    return f"Franchement, '{question}' c'est un sujet stylé. Dis-m'en plus ou demande au patron **Règne** ! 😉"

# --- INTERFACE PRINCIPALE ---
col_main, col_lang = st.columns([0.8, 0.2])

with col_lang:
    # Menu des pays / langues (Le site change pour de vrai)
    pays_sel = st.selectbox("🌐 Pays / Language", list(LANGS.keys()))
    T = LANGS[pays_sel]

with st.sidebar:
    st.title("🤖 Chatbot 1CA")
    st.write("Assistant du GOAT : **Règne**")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Wesh ! Je suis l'IA de Règne. Je réponds à TOUT."}]
    
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    
    if prompt := st.chat_input("Demande-moi n'importe quoi..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        rep = cerveau_ia_goat(prompt)
        with st.chat_message("assistant"): st.markdown(rep)
        st.session_state.messages.append({"role": "assistant", "content": rep})

with col_main:
    # Logo et Titres
    try: st.image("IMG_0956.png", width=130)
    except: st.info("Logo Hacker Cosmic")
    
    st.header(T["calc"])
    st.title("Hacker Cosmic 1CA 2026")
    st.markdown("### Créé par **Règne**")
    st.write("---")

    # LE CALCULATEUR
    p_orig = st.number_input(T["orig"], value=460.0)
    remise = st.number_input(T["rem"], value=10.0)
    resultat = p_orig * (1 - remise / 100)
    st.header(f"{T['total']} : {resultat:.2f} €")
    
    st.write("---")

    # LE DÉFI HACKER (L'exercice est là !)
    st.header(T["defi"])
    if 'score' not in st.session_state: st.session_state.score = 0
    if 'ex_p' not in st.session_state:
        st.session_state.ex_p = random.randint(10, 500)
        st.session_state.ex_r = random.randint(5, 50)
        st.session_state.sol = st.session_state.ex_p * (1 - st.session_state.ex_r / 100)

    st.write(f"**{T['score']} : {st.session_state.score} ⭐**")
    st.write(f"Trouve le prix final : **{st.session_state.ex_p}€** avec **{st.session_state.ex_r}%** de remise.")
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

    # LE COMPTEUR DE VISITES
    if 'v' not in st.session_state: st.session_state.v = 13
    st.session_state.v += 1
    st.write(f"🔥 **{st.session_state.v} {T['visit']}**")
