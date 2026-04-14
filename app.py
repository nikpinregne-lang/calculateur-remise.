import streamlit as st
import random
import re

# 1. Configuration GOAT
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="wide")

# --- LISTE DE TOUS LES PAYS DU MONDE (TOP 100+ & DRAPEAUX) ---
pays_complet = [
    "🇫🇷 France", "🇲🇦 Maroc", "🇸🇦 Arabie Saoudite", "🇧🇪 Belgique", "🇷🇴 Roumanie", 
    "🇺🇦 Ukraine", "🇹🇷 Turquie", "🇩🇿 Algérie", "🇹🇳 Tunisie", "🇺🇸 USA", "🇨🇦 Canada", 
    "🇨🇭 Suisse", "🇮🇹 Italie", "🇪🇸 Espagne", "🇵🇹 Portugal", "🇩🇪 Allemagne",
    "🇬🇧 Royaume-Uni", "🇧🇷 Brésil", "🇯🇵 Japon", "🇨🇳 Chine", "🇷🇺 Russie",
    "🇦🇲 Arménie", "🇦🇺 Australie", "🇦🇹 Autriche", "🇦🇿 Azerbaïdjan", "🇧🇸 Bahamas",
    "🇧🇭 Bahreïn", "🇧🇩 Bangladesh", "🇧🇧 Barbade", "🇧🇾 Biélorussie", "🇧🇯 Bénin",
    "🇧🇴 Bolivie", "🇧🇦 Bosnie", "🇧🇼 Botswana", "🇧🇳 Brunei", "🇧🇬 Bulgarie",
    "🇨🇲 Cameroun", "🇨🇱 Chili", "🇨🇴 Colombie", "🇨🇬 Congo", "🇨🇷 Costa Rica",
    "🇨🇮 Côte d'Ivoire", "🇭🇷 Croatie", "🇨🇺 Cuba", "🇩🇰 Danemark", "🇩🇯 Djibouti",
    "🇪🇬 Égypte", "🇦🇪 Émirats Arabes Unis", "🇪🇨 Équateur", "🇪🇪 Estonie", "🇪🇹 Éthiopie",
    "🇫🇮 Finlande", "🇬🇦 Gabon", "🇬🇪 Géorgie", "🇬🇭 Ghana", "🇬🇷 Grèce", "🇬🇹 Guatemala",
    "🇭🇺 Hongrie", "🇮🇳 Inde", "🇮🇩 Indonésie", "🇮🇶 Irak", "🇮🇷 Iran", "🇮🇪 Irlande",
    "🇮🇸 Islande", "🇮🇱 Israël", "🇯🇲 Jamaïque", "🇯🇴 Jordanie", "🇰🇿 Kazakhstan",
    "🇰🇪 Kenya", "🇰🇼 Koweït", "🇱🇦 Laos", "🇱🇻 Lettonie", "🇱🇧 Liban", "🇱🇾 Libye",
    "🇱🇹 Lituanie", "🇱🇺 Luxembourg", "🇲🇾 Malaisie", "🇲️ Mali", "🇲🇹 Malte",
    "🇲🇺 Maurice", "🇲🇽 Mexique", "🇲🇨 Monaco", "🇲🇳 Mongolie", "🇳🇪 Niger",
    "🇳🇬 Nigeria", "🇳🇴 Norvège", "🇳🇿 Nouvelle-Zélande", "🇴🇲 Oman", "🇵🇰 Pakistan",
    "🇵🇦 Panama", "🇵🇾 Paraguay", "🇳🇱 Pays-Bas", "🇵🇪 Pérou", "🇵🇭 Philippines",
    "🇵🇱 Pologne", "🇶🇦 Qatar", "🇨🇿 Rép. Tchèque", "🇸🇳 Sénégal", "🇷🇸 Serbie",
    "🇸🇬 Singapour", "🇸🇰 Slovaquie", "🇸🇮 Slovénie", "🇸🇪 Suède", "🇹🇭 Thaïlande",
    "🇹🇬 Togo", "🇻🇳 Vietnam"
]

# --- CERVEAU IA (CONNAISSANCE UNIVERSELLE) ---
def chatbot_cerveau(question):
    q = question.lower().strip()
    
    # Capitales (Mode Dictionnaire Géant)
    caps = {
        "afghanistan": "Kaboul", "albanie": "Tirana", "algérie": "Alger", "allemagne": "Berlin",
        "andorre": "Andorre-la-Vieille", "angola": "Luanda", "arabie saoudite": "Riyad",
        "argentine": "Buenos Aires", "arménie": "Erevan", "australie": "Canberra",
        "autriche": "Vienne", "azerbaïdjan": "Bakou", "bahamas": "Nassau", "bahreïn": "Manama",
        "bangladesh": "Dacca", "barbade": "Bridgetown", "belgique": "Bruxelles", "bénin": "Porto-Novo",
        "brésil": "Brasília", "bulgarie": "Sofia", "canada": "Ottawa", "chili": "Santiago",
        "chine": "Pékin", "chypre": "Nicosie", "colombie": "Bogotá", "corée du sud": "Séoul",
        "croatie": "Zagreb", "cuba": "La Havane", "danemark": "Copenhague", "égypte": "Le Caire",
        "espagne": "Madrid", "états-unis": "Washington D.C.", "éthiopie": "Addis-Abeba",
        "finlande": "Helsinki", "france": "Paris", "grèce": "Athènes", "hongrie": "Budapest",
        "inde": "New Delhi", "indonésie": "Jakarta", "irak": "Bagdad", "iran": "Téhéran",
        "irlande": "Dublin", "islande": "Reykjavik", "israël": "Jérusalem", "italie": "Rome",
        "japon": "Tokyo", "jordanie": "Amman", "kazakhstan": "Astana", "kenya": "Nairobi",
        "liban": "Beyrouth", "libye": "Tripoli", "luxembourg": "Luxembourg", "madagascar": "Antananarivo",
        "malaisie": "Kuala Lumpur", "mali": "Bamako", "maroc": "Rabat", "mexique": "Mexico",
        "monaco": "Monaco", "norvège": "Oslo", "nouvelle-zélande": "Wellington", "pakistan": "Islamabad",
        "pays-bas": "Amsterdam", "pologne": "Varsovie", "portugal": "Lisbonne", "qatar": "Doha",
        "roumanie": "Bucarest", "royaume-uni": "Londres", "russie": "Moscou", "sénégal": "Dakar",
        "suisse": "Berne", "thaïlande": "Bangkok", "tunisie": "Tunis", "turquie": "Ankara",
        "ukraine": "Kyiv", "vietnam": "Hanoï"
    }

    if "qui" in q and "cree" in q: return "Le GOAT absolu, c'est **Règne** ! 👑"
    if "1+1" in q: return "Ça fait 2, facile ! 🤓"
    
    # Vérification automatique des pays
    for pays, cap in caps.items():
        if pays in q: return f"La capitale de ce pays est **{cap}**. Règne connaît tout ! 🌍"

    if q in ["salut", "bonjour", "wesh"]: return "Wesh ! Je suis l'IA de Règne, je connais tous les pays !"
    
    return f"Pour '{question}', je dois demander au cerveau de **Règne**, mais sache que c'est un sujet de génie !"

# --- INTERFACE ---
col_main, col_lang = st.columns([0.8, 0.2])

with col_lang:
    st.selectbox("🌐 Tous les Pays", pays_complet)

with st.sidebar:
    st.title("🤖 Chatbot 1CA")
    st.write("Assistant de **Règne**")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Wesh ! Pose-moi n'importe quelle question sur les pays !"}]
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    if prompt := st.chat_input("Demande-moi une capitale..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        rep = chatbot_cerveau(prompt)
        with st.chat_message("assistant"): st.markdown(rep)
        st.session_state.messages.append({"role": "assistant", "content": rep})

with col_main:
    st.image("IMG_0956.png", width=120)
    st.title("Hacker Cosmic 1CA 2026")
    st.subheader("Créé par **Règne**")
    st.write("---")

    # CALCULATEUR
    p = st.number_input("Prix d'origine (€)", value=460.0)
    r = st.number_input("Remise (%)", value=10.0)
    st.header(f"Total : {p * (1 - r/100):.2f} €")
    
    st.write("---")
    
    # COMPTEUR
    if 'v' not in st.session_state: st.session_state.v = 11
    st.session_state.v += 1
    st.write(f"🔥 **{st.session_state.v} Hackers** ont visité ce site !")
