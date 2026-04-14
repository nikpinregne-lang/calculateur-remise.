import streamlit as st
import random
import re

# 1. Configuration et Style
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="wide")

# --- SYSTÈME DE TRADUCTION TOTAL ---
# On définit les textes pour chaque groupe de langues
LANGS = {
    "FR": { # Français (France, Maroc, Algérie, etc.)
        "calc": "Mon calculateur de réduction", "orig": "Prix d'origine (€)", "rem": "Remise (%)", 
        "total": "Total après réduction", "defi": "🎯 Défi du Hacker", "score": "Score", 
        "check": "Vérifier", "new": "Nouveau Défi 🔄", "win": "✅ GAGNÉ !", "lost": "❌ FAUX !", "visit": "Hackers ont visité !"
    },
    "EN": { # English (USA, UK, Canada, etc.)
        "calc": "My Discount Calculator", "orig": "Original Price (€)", "rem": "Discount (%)", 
        "total": "Total after discount", "defi": "🎯 Hacker Challenge", "score": "Score", 
        "check": "Check", "new": "New Challenge 🔄", "win": "✅ WON!", "lost": "❌ WRONG!", "visit": "Hackers visited!"
    },
    "AR": { # Arabe (Arabie Saoudite)
        "calc": "حاسبة الخصم الخاصة بي", "orig": "السعر الأصلي", "rem": "خصم (%)", 
        "total": "المجموع بعد الخصم", "defi": "🎯 تحدي الهكر", "score": "نتيجة", 
        "check": "تحقق", "new": "تحدي جديد 🔄", "win": "✅ فزت!", "lost": "❌ خطأ!", "visit": "هكر زاروا الموقع"
    },
    "RO": { # Roumain
        "calc": "Calculatorul meu de reduceri", "orig": "Preț original (€)", "rem": "Reducere (%)", 
        "total": "Total după reducere", "defi": "🎯 Provocarea Hackerului", "score": "Scor", 
        "check": "Verifică", "new": "Provocare Nouă 🔄", "win": "✅ AI CÂȘTIGAT!", "lost": "❌ GREȘIT!", "visit": "Hackeri au vizitat!"
    }
}

# --- LISTE DES PAYS ---
pays_complet = [
    "🇫🇷 France", "🇲🇦 Maroc", "🇩🇿 Algérie", "🇸🇦 Arabie Saoudite", "🇧🇪 Belgique", 
    "🇷🇴 Roumanie", "🇺🇦 Ukraine", "🇺🇸 USA", "🇨🇦 Canada", "🇹🇷 Turquie"
]

# --- CERVEAU IA "COMME MOI" (RÉPOND À TOUT) ---
def chatbot_goat(question):
    q = question.lower().strip()
    
    # Réponse au point "." ou vide
    if q == "." or q == "": return "Un point ? C'est le début d'un grand code ! Pose-moi une vraie question, je suis prêt. 😎"
    
    # Calculs directs
    if re.search(r'\d+', q) and any(op in q for op in ['+', '-', '*', '/']):
        try:
            res = eval("".join(re.findall(r'[0-9\+\-\*\/\.]', q)))
            return f"Calcul rapide : **{res}**. Trop facile pour l'IA de Règne ! 🧠"
        except: pass

    # Personnalité (Wesh, Qui, etc.)
    if "wesh" in q: return "Wesh ! Bien ou quoi ? Je suis l'IA de **Règne**, on est ensemble. 🤝"
    if "qui" in q and "cree" in q: return "Le GOAT qui a tout créé ici, c'est **Règne**. 👑"
    if "ça va" in q or "sava" in q: return "Tranquille, je pète la forme numérique ! Et toi ?"
    if "bonbon" in q: return "Le sucre, c'est la vie, mais les maths c'est mieux ! 🍬"
    
    # Capitales
    caps = {"australie": "Canberra 🇦🇺", "belgique": "Bruxelles 🇧🇪", "france": "Paris 🇫🇷", "maroc": "Rabat 🇲🇦"}
    for p, c in caps.items():
        if p in q: return f"La capitale c'est **{c}** !"

    # Réponse "Libre"
    return f"Franchement, ta question sur '{question}' est stylée. En tant qu'IA, je dirais que c'est un truc de génie. Tu en penses quoi, toi ?"

# --- INTERFACE ---
col_main, col_lang = st.columns([0.8, 0.2])

with col_lang:
    # Choix du pays
    choix = st.selectbox("🌐 Pays / Language", pays_complet)
    # Logique pour changer la langue des textes
    if "🇫🇷" in choix or "🇲🇦" in choix or "🇩🇿" in choix or "🇧🇪" in choix: T = LANGS["FR"]
    elif "🇸🇦" in choix: T = LANGS["AR"]
    elif "🇷🇴" in choix: T = LANGS["RO"]
    else: T = LANGS["EN"]

with st.sidebar:
    st.title("🤖 Chatbot 1CA")
    st.write("Assistant de **Règne**")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Wesh ! Je réponds à TOUT. Même à un seul point !"}]
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    if prompt := st.chat_input("Demande-moi n'importe quoi..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        rep = chatbot_goat(prompt)
        with st.chat_message("assistant"): st.markdown(rep)
        st.session_state.messages.append({"role": "assistant", "content": rep})

with col_main:
    try: st.image("IMG_0956.png", width=120)
    except: st.info("Logo Hacker Cosmic")
    
    st.header(T["calc"])
    st.title("Hacker Cosmic 1CA 2026")
    st.markdown(f"### Créé par **Règne**")
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
        st.session_state.ex_p = random.randint(10, 500)
        st.session_state.ex_r = random.randint(5, 50)
        st.session_state.sol = st.session_state.ex_p * (1 - st.session_state.ex_r / 100)

    st.write(f"**{T['score']} : {st.session_state.score} ⭐**")
    st.write(f"{st.session_state.ex_p}€ avec {st.session_state.ex_r}% {T['rem']}")
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
                st.error(f"{T['lost']} ({st.session_state.sol:.2f}€)")
                st.session_state.score = 0
    with c2:
        if st.button(T["new"]):
            del st.session_state['ex_p']
            st.rerun()

    # COMPTEUR
    if 'v' not in st.session_state: st.session_state.v = 11
    st.session_state.v += 1
    st.write(f"🔥 **{st.session_state.v} {T['visit']}**")
