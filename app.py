import streamlit as st
import random
import re

# 1. Configuration
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="wide")

# --- SYSTÈME DE TRADUCTION ---
trads = {
    "FR": {
        "titre_calcul": "Mon calculateur de réduction",
        "prix_label": "Prix d'origine (€)",
        "remise_label": "Remise (%)",
        "total": "Total :",
        "defi": "🎯 Défi du Hacker",
        "score": "Score :",
        "votre_rep": "Ta réponse (€) :",
        "bouton_verif": "Vérifier",
        "chat_welcome": "Wesh ! Je suis l'IA de Hacker Cosmic. Demande-moi n'importe quoi.",
        "chat_input": "Écris-moi..."
    },
    "EN": {
        "titre_calcul": "My Discount Calculator",
        "prix_label": "Original Price ($)",
        "remise_label": "Discount (%)",
        "total": "Total:",
        "defi": "🎯 Hacker Challenge",
        "score": "Score:",
        "votre_rep": "Your answer ($):",
        "bouton_verif": "Check",
        "chat_welcome": "Yo! I'm the Hacker Cosmic AI. Ask me anything.",
        "chat_input": "Type here..."
    },
    "AR": {
        "titre_calcul": "حاسبة الخصم الخاصة بي",
        "prix_label": "السعر الأصلي",
        "remise_label": "خصم (%)",
        "total": "المجموع :",
        "defi": "🎯 تحدي الهكر",
        "score": "نتيجة :",
        "votre_rep": "إجابتك :",
        "bouton_verif": "تحقق",
        "chat_welcome": "مرحباً! أنا الذكاء الاصطناعي لـ Hacker Cosmic. اسألني أي شيء.",
        "chat_input": "اكتب هنا..."
    }
}

# --- LISTE DES PAYS ---
tous_les_pays = sorted([
    "🇫🇷 France", "🇦🇫 Afghanistan", "🇿🇦 Afrique du Sud", "🇩🇿 Algérie", "🇩🇪 Allemagne", 
    "🇸🇦 Arabie Saoudite", "🇦🇺 Australie", "🇧🇪 Belgique", "🇨🇦 Canada", "🇨🇳 Chine", 
    "🇪🇬 Égypte", "🇦🇪 Émirats Arabes Unis", "🇪🇸 Espagne", "🇺🇸 USA", "🇮🇹 Italie", 
    "🇲🇦 Maroc", "🇬🇧 Royaume-Uni", "🇨🇭 Suisse", "🇹🇳 Tunisie", "🇹🇷 Turquie"
])

# --- LE CERVEAU IA GOAT (VERSION COMPLÈTE) ---
def cerveau_ia_goat(question, langue):
    q = question.lower().strip()
    
    # Culture G & Réponses personnalisées
    connaissances = {
        "canada": "Ottawa 🇨🇦", "france": "Paris 🇫🇷", "maroc": "Rabat 🇲🇦", 
        "belgique": "Bruxelles 🇧🇪", "australie": "Canberra 🇦🇺", "usa": "Washington D.C. 🇺🇸",
        "allemagne": "Berlin 🇩🇪", "italie": "Rome 🇮🇹", "espagne": "Madrid 🇪🇸",
        "bonbon": "Une sucrerie délicieuse. Miam ! 🍬",
        "qui": "Le seul patron ici, c'est le GOAT **Hacker Cosmic**. 👑"
    }
    
    for mot, rep in connaissances.items():
        if mot in q: return f"La réponse est **{rep}**."

    # Calculs Maths Directs (1+1, etc.)
    if re.search(r'\d+', q) and any(op in q for op in ['+', '-', '*', '/']):
        try:
            # On nettoie la chaîne pour ne garder que les chiffres et opérateurs
            calc = "".join(re.findall(r'[0-9\+\-\*\/\.]', q))
            res = eval(calc)
            return f"Résultat : **{res}**. Trop facile pour un hacker ! 😎"
        except: pass

    # Réponses de style humain
    if any(s in q for s in ["wesh", "salut", "bonjour", "sava", "ça va"]):
        return "Wesh ! Je suis prêt. Pose-moi une colle !"
    
    return f"Pour '{question}', c'est une excellente question ! Je dirais que c'est captivant. 😉"

# --- INTERFACE ---
col_main, col_lang = st.columns([0.7, 0.3])

with col_lang:
    pays_selectionne = st.selectbox("🌐 Choisi ton pays / Choose country", tous_les_pays)
    
    # Choix de la langue du dictionnaire L
    if any(p in pays_selectionne for p in ["France", "Belgique", "Maroc", "Algérie", "Tunisie"]):
        L = trads["FR"]
        code_langue = "FR"
    elif any(p in pays_selectionne for p in ["Afghanistan", "Arabie", "Égypte", "Émirats"]):
        L = trads["AR"]
        code_langue = "AR"
    else:
        L = trads["EN"]
        code_langue = "EN"

with st.sidebar:
    st.title("🤖 Chatbot 1CA")
    st.write("Assistant de **Hacker Cosmic**")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": L["chat_welcome"]}]
    
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    
    if prompt := st.chat_input(L["chat_input"]):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        
        # L'IA répond en utilisant sa base de connaissances
        rep = cerveau_ia_goat(prompt, code_langue)
        
        with st.chat_message("assistant"): st.markdown(rep)
        st.session_state.messages.append({"role": "assistant", "content": rep})

with col_main:
    st.header(L["titre_calcul"])
    st.title("Hacker Cosmic 1CA 2026")
    st.write("---")

    # CALCULATEUR
    p = st.number_input(L["prix_label"], value=460.0)
    r = st.number_input(L["remise_label"], value=10.0)
    st.header(f"{L['total']} {p * (1 - r/100):.2f}")
    
    st.write("---")

    # DÉFI DU HACKER
    st.header(L["defi"])
    if 'score' not in st.session_state: st.session_state.score = 0
    if 'ex_p' not in st.session_state:
        st.session_state.ex_p, st.session_state.ex_r = random.randint(10, 500), random.randint(5, 50)
        st.session_state.sol = st.session_state.ex_p * (1 - st.session_state.ex_r / 100)

    st.write(f"**{L['score']} {st.session_state.score} ⭐**")
    st.write(f"Défi : **{st.session_state.ex_p}** avec **{st.session_state.ex_r}%** de remise.")
    ans = st.number_input(L["votre_rep"], key="ans_input", value=0.0)
    
    if st.button(L["bouton_verif"]):
        if abs(ans - st.session_state.sol) < 0.1:
            st.success("✅ GAGNÉ !")
            st.session_state.score += 1
            del st.session_state['ex_p']
            st.rerun()
        else:
            st.error(f"❌ FAUX ! C'était {st.session_state.sol:.2f}")
            st.session_state.score = 0

    st.write(f"🔥 **{random.randint(25, 60)} Hackers ont visité ce site !**")
