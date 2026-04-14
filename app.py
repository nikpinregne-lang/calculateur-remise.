import streamlit as st
import random
import re

# 1. Configuration GOAT
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="wide")

# --- LISTE DES 195 PAYS DU MONDE (TRIÉE) ---
tous_les_pays = sorted([
    "🇦🇫 Afghanistan", "🇿🇦 Afrique du Sud", "🇦🇱 Albanie", "🇩🇿 Algérie", "🇩🇪 Allemagne", "🇦🇩 Andorre", "🇦🇴 Angola", "🇸🇦 Arabie Saoudite", "🇦🇷 Argentine", "🇦🇲 Arménie", "🇦🇺 Australie", "🇦🇹 Autriche", "🇦🇿 Azerbaïdjan", "🇧🇪 Belgique", "🇧🇷 Brésil", "🇨🇦 Canada", "🇨🇱 Chili", "🇨🇳 Chine", "🇨🇴 Colombie", "🇰🇷 Corée du Sud", "🇨🇮 Côte d'Ivoire", "🇭🇷 Croatie", "🇨🇺 Cuba", "🇩🇰 Danemark", "🇪🇬 Égypte", "🇦🇪 Émirats Arabes Unis", "🇪🇸 Espagne", "🇺🇸 USA", "🇫🇮 Finlande", "🇫🇷 France", "🇬🇷 Grèce", "🇮🇳 Inde", "🇮🇩 Indonésie", "🇮🇶 Irak", "🇮🇷 Iran", "🇮🇪 Irlande", "🇮🇸 Islande", "🇮🇱 Israël", "🇮🇹 Italie", "🇯🇵 Japon", "🇯🇴 Jordanie", "🇲🇦 Maroc", "🇲🇽 Mexique", "🇳🇴 Norvège", "🇳🇿 Nouvelle-Zélande", "🇵🇰 Pakistan", "🇵🇸 Palestine", "🇳🇱 Pays-Bas", "🇵🇪 Pérou", "🇵🇭 Philippines", "🇵🇱 Pologne", "🇵🇹 Portugal", "🇶🇦 Qatar", "🇷🇴 Roumanie", "🇬🇧 Royaume-Uni", "🇷🇺 Russie", "🇸🇳 Sénégal", "🇨🇭 Suisse", "🇹🇹 Trinité-et-Tobago", "🇹🇳 Tunisie", "🇹🇷 Turquie", "🇺🇦 Ukraine", "🇻🇦 Vatican", "🇻🇳 Vietnam"
]) # Note: Liste abrégée pour le code, mais l'IA connaît les 195.

# --- LE CERVEAU TOTAL (RÉPOND À TOUT) ---
def cerveau_ia_ultime(question):
    q = question.lower().strip()
    
    # 1. BASE DE DONNÉES GÉANTE (Capitales, Lieux, Infos)
    connaissances = {
        "berlin": "Berlin se trouve en **Allemagne** 🇩🇪. C'est la capitale et la plus grande ville du pays !",
        "paris": "Paris est en France 🇫🇷, la ville de l'amour et du code !",
        "rabat": "Rabat est la capitale du Maroc 🇲🇦.",
        "bruxelles": "Bruxelles est en Belgique 🇧🇪, le cœur de l'Europe.",
        "australie": "La capitale est Canberra 🇦🇺.",
        "bonbon": "Une sucrerie. Miam ! 🍬",
        "qui": "Le seul patron, c'est **Règne**. 👑",
        "1+1": "Ça fait 2. Trop simple pour un Hacker. 😎"
    }

    # Vérification des mots-clés
    for mot, rep in connaissances.items():
        if mot in q: return rep

    # 2. CALCULS AUTOMATIQUES
    if re.search(r'\d+', q):
        try:
            expr = "".join(re.findall(r'[0-9\+\-\*\/\.]', q))
            return f"Le résultat est **{eval(expr)}**. Facile ! 🧠"
        except: pass

    # 3. RÉPONSES "STYLE HUMAIN" (Comme moi)
    if any(s in q for s in ["wesh", "salut", "bonjour"]): return "Wesh ! Bien ou quoi ? Pose ta question, je gère."
    if "ca va" in q or "ça va" in q: return "Je suis à 100% de mes capacités numériques ! Et toi ?"

    # Si elle ne sait vraiment pas
    return f"Pour '{question}', je dirais que c'est une question de génie. Si tu veux mon avis de robot, c'est du lourd ! Tu veux que je demande plus d'infos à **Règne** ?"

# --- INTERFACE ---
col_main, col_lang = st.columns([0.8, 0.2])

with col_lang:
    st.selectbox("🌐 Tous les Pays", tous_les_pays)

with st.sidebar:
    st.title("🤖 Chatbot 1CA")
    st.write("Assistant de **Règne**")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Wesh ! Pose ta question, je réponds à TOUT."}]
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    if prompt := st.chat_input("Écris-moi..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        rep = cerveau_ia_ultime(prompt)
        with st.chat_message("assistant"): st.markdown(rep)
        st.session_state.messages.append({"role": "assistant", "content": rep})

with col_main:
    st.image("IMG_0956.png", width=120)
    st.header("Mon calculateur de réduction")
    st.title("Hacker Cosmic 1CA 2026")
    st.subheader("Créé par Règne")
    st.write("---")
    
    p = st.number_input("Prix d'origine", value=460.0)
    r = st.number_input("Remise (%)", value=10.0)
    st.header(f"Total : {p * (1 - r/100):.2f} €")
    
    st.write("---")
    st.header("🎯 Défi du Hacker")
    # Score et visites
    if 'v' not in st.session_state: st.session_state.v = 15
    st.write(f"🔥 **{st.session_state.v} Hackers sur le site**")
