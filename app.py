import streamlit as st
import random
import re

# 1. Configuration GOAT
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="wide")

# --- LISTE DES 195 PAYS DU MONDE PAR ORDRE ALPHABÉTIQUE ---
tous_les_pays = sorted([
    "🇦🇫 Afghanistan", "🇿🇦 Afrique du Sud", "🇦🇱 Albanie", "🇩🇿 Algérie", "🇩🇪 Allemagne", "🇦🇩 Andorre", "🇦🇴 Angola", "🇦🇮 Anguilla", "🇦🇬 Antigua-et-Barbuda", "🇸🇦 Arabie Saoudite", "🇦🇷 Argentine", "🇦🇲 Arménie", "🇦🇺 Australie", "🇦🇹 Autriche", "🇦🇿 Azerbaïdjan", 
    "🇧🇸 Bahamas", "🇧🇭 Bahreïn", "🇧🇩 Bangladesh", "🇧🇧 Barbade", "🇧🇪 Belgique", "🇧🇿 Belize", "🇧🇯 Bénin", "🇧🇹 Bhoutan", "🇧🇾 Biélorussie", "🇧🇲 Birmanie", "🇧🇴 Bolivie", "🇧🇦 Bosnie-Herzégovine", "🇧🇼 Botswana", "🇧🇷 Brésil", "🇧🇳 Brunei", "🇧🇬 Bulgarie", "🇧🇫 Burkina Faso", "🇧🇮 Burundi", 
    "🇰🇭 Cambodge", "🇨🇲 Cameroun", "🇨🇦 Canada", "🇨🇻 Cap-Vert", "🇨🇱 Chili", "🇨🇳 Chine", "🇨🇾 Chypre", "🇨🇴 Colombie", "🇰🇲 Comores", "🇨🇬 Congo", "🇨🇩 Congo (RDC)", "🇰🇷 Corée du Sud", "🇰🇵 Corée du Nord", "🇨🇷 Costa Rica", "🇨🇮 Côte d'Ivoire", "🇭🇷 Croatie", "🇨🇺 Cuba", 
    "🇩🇰 Danemark", "🇩🇯 Djibouti", "🇩🇲 Dominique", "🇪🇬 Égypte", "🇦🇪 Émirats Arabes Unis", "🇪🇨 Équateur", "🇪🇷 Érythrée", "🇪🇸 Espagne", "🇪🇪 Estonie", "🇸🇿 Eswatini", "🇺🇸 USA", "🇪🇹 Éthiopie", "🇫🇮 Finlande", "🇫🇷 France", "🇬🇦 Gabon", "🇬🇲 Gambie", "🇬🇪 Géorgie", "🇬🇭 Ghana", "🇬🇷 Grèce", "🇬🇩 Grenade", "🇬🇹 Guatemala", "🇬🇳 Guinée", "🇬🇼 Guinée-Bissau", "🇬🇶 Guinée équatoriale", "🇬🇾 Guyana", "🇭🇹 Haïti", "🇭🇳 Honduras", "🇭🇺 Hongrie", "🇮🇳 Inde", "🇮🇩 Indonésie", "🇮🇶 Irak", "🇮🇷 Iran", "🇮🇪 Irlande", "🇮🇸 Islande", "🇮🇱 Israël", "🇮🇹 Italie", "🇯🇲 Jamaïque", "🇯🇵 Japon", "🇯🇴 Jordanie", "🇰🇿 Kazakhstan", "🇰🇪 Kenya", "🇰🇬 Kirghizistan", "🇰🇮 Kiribati", "🇰🇼 Koweït", "🇱🇦 Laos", "🇱🇸 Lesotho", "🇱🇻 Lettonie", "🇱🇧 Liban", "🇱🇷 Liberia", "🇱🇾 Libye", "🇱🇮 Liechtenstein", "🇱🇹 Lituanie", "🇱🇺 Luxembourg", "🇲🇰 Macédoine du Nord", "🇲🇬 Madagascar", "🇲🇾 Malaisie", "🇲🇼 Malawi", "🇲🇻 Maldives", "🇲️ Mali", "🇲🇹 Malte", "🇲🇦 Maroc", "🇲🇭 Maurice", "🇲🇷 Mauritanie", "🇲🇽 Mexique", "🇫🇲 Micronésie", "🇲🇩 Moldavie", "🇲🇨 Monaco", "🇲🇳 Mongolie", "🇲🇪 Monténégro", "🇲🇿 Mozambique", "🇳🇦 Namibie", "🇳🇷 Nauru", "🇳🇵 Népal", "🇳🇮 Nicaragua", "🇳🇪 Niger", "🇳🇬 Nigeria", "🇳🇴 Norvège", "🇳🇿 Nouvelle-Zélande", "🇴🇲 Oman", "🇺🇬 Ouganda", "🇺🇿 Ouzbékistan", "🇵🇰 Pakistan", "🇵🇼 Palaos", "🇵🇸 Palestine", "🇵🇦 Panama", "🇵🇬 Papouasie-Nouvelle-Guinée", "🇵🇾 Paraguay", "🇳🇱 Pays-Bas", "🇵🇪 Pérou", "🇵🇭 Philippines", "🇵🇱 Pologne", "🇵🇹 Portugal", "🇶🇦 Qatar", "🇨🇿 Rép. Tchèque", "🇷🇴 Roumanie", "🇬🇧 Royaume-Uni", "🇷🇺 Russie", "🇷🇼 Rwanda", "🇰🇳 Saint-Christophe-et-Niévès", "🇸🇲 Saint-Marin", "🇻🇨 Saint-Vincent", "🇸🇳 Sénégal", "🇷🇸 Serbie", "🇸🇨 Seychelles", "🇸🇬 Singapour", "🇸🇰 Slovaquie", "🇸🇮 Slovénie", "🇸🇴 Somalie", "🇸🇩 Soudan", "🇱🇰 Sri Lanka", "🇸🇪 Suède", "🇨🇭 Suisse", "🇸🇾 Syrie", "🇹🇯 Tadjikistan", "🇹🇿 Tanzanie", "🇹🇩 Tchad", "🇹🇭 Thaïlande", "🇹🇬 Togo", "🇹🇳 Tunisie", "🇹🇲 Turkménistan", "🇹🇷 Turquie", "🇺🇦 Ukraine", "🇺🇾 Uruguay", "🇻🇦 Vatican", "🇻🇪 Venezuela", "🇻🇳 Vietnam", "🇾🇪 Yémen", "🇿🇲 Zambie", "🇿🇼 Zimbabwe"
])

# --- TRADUCTION ---
LANGS = {
    "FR": {"calc": "Mon calculateur de réduction", "orig": "Prix d'origine", "rem": "Remise", "total": "Total", "defi": "🎯 Défi Hacker", "score": "Score"},
    "AR": {"calc": "حاسبة الخصم", "orig": "السعر الأصلي", "rem": "خصم", "total": "المجموع", "defi": "🎯 تحدي الهكر", "score": "نتيجة"},
    "EN": {"calc": "My Calculator", "orig": "Original Price", "rem": "Discount", "total": "Total", "defi": "🎯 Hacker Challenge", "score": "Score"}
}

# --- CERVEAU IA (RÉPOND À TOUT) ---
def cerveau_ia_goat(question):
    q = question.lower().strip()
    
    # 1. Identité et patron
    if "qui" in q and "cree" in q: return "Le GOAT absolu c'est **Règne** ! 👑"
    if "goat" in q: return "Le seul patron ici c'est **Règne**. 😎"
    
    # 2. Capitales (Dictionnaire étendu)
    caps = {
        "allemagne": "Berlin 🇩🇪", "belgique": "Bruxelles 🇧🇪", "france": "Paris 🇫🇷",
        "maroc": "Rabat 🇲🇦", "espagne": "Madrid 🇪🇸", "italie": "Rome 🇮🇹",
        "australie": "Canberra 🇦🇺", "portugal": "Lisbonne 🇵🇹"
    }
    for pays, cap in caps.items():
        if pays in q: return f"La capitale c'est **{cap}**."

    # 3. Calculs directs (ex: 1+1)
    if re.search(r'\d+', q):
        try:
            expr = "".join(re.findall(r'[0-9\+\-\*\/\.]', q))
            return f"Calcul fait : **{eval(expr)}**. Facile pour l'IA de Règne ! 🧠"
        except: pass

    # 4. Politesse
    if any(s in q for s in ["wesh", "salut", "bonjour", "hello"]):
        return "Wesh ! Bien ou quoi ? Je réponds à TOUT maintenant. Pose ta question."
    if "ca va" in q or "ça va" in q:
        return "Je pète la forme numérique ! Et toi ?"

    return f"Pour '{question}', je dirais que c'est captivant. Demande à **Règne**, il a toutes les réponses ! 😉"

# --- INTERFACE ---
col_main, col_lang = st.columns([0.8, 0.2])

with col_lang:
    choix = st.selectbox("🌐 Tous les Pays", tous_les_pays)
    T = LANGS["AR"] if any(f in choix for f in ["🇲🇦", "🇸🇦", "🇩🇿"]) else LANGS["FR"]

with st.sidebar:
    st.title("🤖 Chatbot 1CA")
    st.write("Assistant de **Règne**")
    if "messages" not in st.session_state: st.session_state.messages = []
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    if prompt := st.chat_input("Écris-moi..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        rep = cerveau_ia_goat(prompt)
        with st.chat_message("assistant"): st.markdown(rep)
        st.session_state.messages.append({"role": "assistant", "content": rep})

with col_main:
    try: st.image("IMG_0956.png", width=130)
    except: st.info("Logo Hacker Cosmic")
    st.header(T["calc"])
    st.title("Hacker Cosmic 1CA 2026")
    st.subheader(f"Créé par Règne")
    st.write("---")
    
    prix = st.number_input(T["orig"], value=460.0)
    rem = st.number_input(T["rem"], value=10.0)
    st.header(f"{T['total']} : {prix * (1 - rem/100):.2f} €")
    
    st.write("---")
    st.header(T["defi"])
    if 'score' not in st.session_state: st.session_state.score = 0
    st.write(f"**Score : {st.session_state.score} ⭐**")
    
    if 'v' not in st.session_state: st.session_state.v = 15
    st.session_state.v += 1
    st.write(f"🔥 **{st.session_state.v} Visiteurs**")
