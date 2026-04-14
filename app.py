import streamlit as st
import random
import re

# 1. Configuration GOAT
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="wide")

# --- DICTIONNAIRE DE TRADUCTION ET PAYS (195 Pays) ---
# J'ai configuré les langues principales. Les autres pays utiliseront l'anglais par défaut.
lang_data = {
    "Français": {"calc": "Mon calculateur de réduction", "orig": "Prix d'origine (€)", "rem": "Remise (%)", "defi": "🎯 Défi du Hacker", "score": "Score actuel", "win": "✅ GAGNÉ !", "lost": "❌ FAUX !"},
    "English": {"calc": "My Discount Calculator", "orig": "Original Price (€)", "rem": "Discount (%)", "defi": "🎯 Hacker Challenge", "score": "Current Score", "win": "✅ WON!", "lost": "❌ WRONG!"},
    "Español": {"calc": "Mi Calculadora de Descuento", "orig": "Precio original (€)", "rem": "Descuento (%)", "defi": "🎯 Desafío Hacker", "score": "Puntuación", "win": "✅ ¡GANADO!", "lost": "❌ ¡FALSO!"},
    "العربية": {"calc": "حاسبة الخصم الخاصة بي", "orig": "السعر الأصلي", "rem": "خصم (%)", "defi": "🎯 تحدي الهكر", "score": "النتيجة الحالية", "win": "✅ فزت!", "lost": "❌ خطأ!"}
}

tous_les_pays = [
    "🇫🇷 France", "🇲🇦 Maroc", "🇩🇿 Algérie", "🇹🇳 Tunisie", "🇸🇦 Arabie Saoudite", "🇧🇪 Belgique", "🇨🇦 Canada", "🇺🇸 USA", "🇷🇴 Roumanie", "🇺🇦 Ukraine", "🇹🇷 Turquie", "🇵🇹 Portugal", "🇪🇸 Espagne", "🇮🇹 Italie", "🇩🇪 Allemagne", "🇨🇭 Suisse", "🇬🇧 Royaume-Uni", "🇯🇵 Japon", "🇨🇳 Chine", "🇷🇺 Russie"
    # ... (Tu peux ajouter les 195 ici, la logique reste la même)
]

# --- CERVEAU IA ILLIMITÉ (RÉPOND À TOUT) ---
def cerveau_ia_ultime(question):
    q = question.lower().strip()
    
    # 1. Calculs (ex: 12*5)
    if re.search(r'\d+', q) and any(op in q for op in ['+', '-', '*', '/']):
        try:
            res = eval("".join(re.findall(r'[0-9\+\-\*\/\.]', q)))
            return f"Facile ! Ça fait **{res}**. Règne m'a donné un cerveau de génie. 😎"
        except: pass

    # 2. Réponses "Style Pote" (Wesh, etc.)
    if "wesh" in q or "wsh" in q: return "Wesh ! Bien ou quoi ? Je suis l'IA de **Règne**, on est ensemble. 🤝"
    if "bonbon" in q: return "Une sucrerie délicieuse ! Mais attention à tes dents de hacker. 🍬"
    if "qui" in q and "cree" in q: return "C'est le seul et unique **Règne** le GOAT ! 👑"
    if "ça va" in q or "sava" in q: return "Tranquille, je pète la forme numérique ! Et toi ?"
    
    # 3. Capitales (Dictionnaire intégré)
    capitales = {"australie": "Canberra 🇦🇺", "belgique": "Bruxelles 🇧🇪", "france": "Paris 🇫🇷", "maroc": "Rabat 🇲🇦", "turquie": "Ankara 🇹🇷"}
    for pays, cap in capitales.items():
        if pays in q: return f"La capitale c'est **{cap}** !"

    return f"Franchement, '{question}' c'est une bonne question. En vrai, demande à **Règne**, c'est lui le patron ! 😉"

# --- INTERFACE ---
# Menu des pays à droite
col_main, col_lang = st.columns([0.8, 0.2])

with col_lang:
    choix_pays = st.selectbox("🌐 Tous les Pays", tous_les_pays)
    # Détection de la langue selon le drapeau
    if "🇫🇷" in choix_pays or "🇲🇦" in choix_pays or "🇩🇿" in choix_pays or "🇹🇳" in choix_pays: L = lang_data["Français"]
    elif "🇸🇦" in choix_pays: L = lang_data["العربية"]
    elif "🇪🇸" in choix_pays: L = lang_data["Español"]
    else: L = lang_data["English"]

with st.sidebar:
    st.title("🤖 Chatbot 1CA")
    st.write("Assistant de **Règne**")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Wesh ! Pose ta question, je réponds à tout."}]
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    if prompt := st.chat_input("Demande-moi n'importe quoi..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        rep = cerveau_ia_ultime(prompt)
        with st.chat_message("assistant"): st.markdown(rep)
        st.session_state.messages.append({"role": "assistant", "content": rep})

with col_main:
    st.image("IMG_0956.png", width=120)
    st.header(L["calc"])
    st.title("Hacker Cosmic 1CA 2026")
    st.markdown("### Créé par **Règne**")
    st.write("---")

    # Calculateur
    p_orig = st.number_input(L["orig"], value=460.0)
    remise = st.number_input(L["rem"], value=10.0)
    st.header(f"Total : {p_orig * (1 - remise/100):.2f} €")
    
    st.write("---")

    # DÉFI DU HACKER
    st.header(L["defi"])
    if 'score' not in st.session_state: st.session_state.score = 0
    if 'ex_p' not in st.session_state:
        st.session_state.ex_p = random.randint(10, 500)
        st.session_state.ex_r = random.randint(5, 50)
        st.session_state.sol = st.session_state.ex_p * (1 - st.session_state.ex_r / 100)

    st.write(f"**{L['score']} : {st.session_state.score} ⭐**")
    st.write(f"{st.session_state.ex_p}€ avec {st.session_state.ex_r}% de remise.")
    ans = st.number_input("Ta réponse (€) :", key="ans_input")
    
    if st.button(L["calc"].split()[0]): # Bouton de validation
        if abs(ans - st.session_state.sol) < 0.1:
            st.success(L["win"])
            st.session_state.score += 1
            del st.session_state['ex_p']
            st.rerun()
        else:
            st.error(f"{L['lost']} ({st.session_state.sol:.2f}€)")
            st.session_state.score = 0

    # Compteur de visites
    if 'v' not in st.session_state: st.session_state.v = 11
    st.session_state.v += 1
    st.write(f"🔥 **{st.session_state.v} Hackers** ont visité ce site !")
