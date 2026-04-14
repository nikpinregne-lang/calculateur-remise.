import streamlit as st
import random
import re

# 1. Configuration GOAT
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="wide")

# --- LISTE DE TOUS LES PAYS DU MONDE (195+) ---
# Cette liste contient les nations officielles reconnues mondialement
pays_monde = [
    "🇦🇫 Afghanistan", "🇿🇦 Afrique du Sud", "🇦🇱 Albanie", "🇩🇿 Algérie", "🇩🇪 Allemagne", "🇦🇩 Andorre", "🇦🇴 Angola", "🇦🇮 Anguilla", "🇦🇬 Antigua-et-Barbuda", "🇸🇦 Arabie Saoudite", "🇦🇷 Argentine", "🇦🇲 Arménie", "🇦🇺 Australie", "🇦🇹 Autriche", "🇦🇿 Azerbaïdjan", 
    "🇧🇸 Bahamas", "🇧🇭 Bahreïn", "🇧🇩 Bangladesh", "🇧🇧 Barbade", "🇧🇪 Belgique", "🇧🇿 Belize", "🇧🇯 Bénin", "🇧🇹 Bhoutan", "🇧🇾 Biélorussie", "🇧🇲 Bermudes", "🇧🇴 Bolivie", "🇧🇦 Bosnie-Herzégovine", "🇧🇼 Botswana", "🇧🇷 Brésil", "🇧🇳 Brunei", "🇧🇬 Bulgarie", "🇧🇫 Burkina Faso", "🇧🇮 Burundi", 
    "🇰🇭 Cambodge", "🇨🇲 Cameroun", "🇨🇦 Canada", "🇨🇻 Cap-Vert", "🇨🇱 Chili", "🇨🇳 Chine", "🇨🇾 Chypre", "🇨🇴 Colombie", "🇰🇲 Comores", "🇨🇬 Congo", "🇨🇩 Congo (RDC)", "🇰🇷 Corée du Sud", "🇰🇵 Corée du Nord", "🇨🇷 Costa Rica", "🇨🇮 Côte d'Ivoire", "🇭🇷 Croatie", "🇨🇺 Cuba", 
    "🇩🇰 Danemark", "🇩🇯 Djibouti", "🇩🇲 Dominique", 
    "🇪🇬 Égypte", "🇦🇪 Émirats Arabes Unis", "🇪🇨 Équateur", "🇪🇷 Érythrée", "🇪🇸 Espagne", "🇪🇪 Estonie", "🇸🇿 Eswatini", "🇺🇸 États-Unis", "🇪🇹 Éthiopie", 
    "🇫🇮 Finlande", "🇫🇷 France", 
    "🇬🇦 Gabon", "🇬🇲 Gambie", "🇬🇪 Géorgie", "🇬🇭 Ghana", "🇬🇷 Grèce", "🇬🇩 Grenade", "🇬🇹 Guatemala", "🇬🇳 Guinée", "🇬🇼 Guinée-Bissau", "🇬🇶 Guinée équatoriale", "🇬🇾 Guyana", 
    "🇭🇹 Haïti", "🇭🇳 Honduras", "🇭🇺 Hongrie", 
    "🇮🇳 Inde", "🇮🇩 Indonésie", "🇮🇶 Irak", "🇮🇷 Iran", "🇮🇪 Irlande", "🇮🇸 Islande", "🇮🇱 Israël", "🇮🇹 Italie", 
    "🇯🇲 Jamaïque", "🇯🇵 Japon", "🇯🇴 Jordanie", 
    "🇰🇿 Kazakhstan", "🇰🇪 Kenya", "🇰🇬 Kirghizistan", "🇰🇮 Kiribati", "🇰🇼 Koweït", 
    "🇱🇦 Laos", "🇱🇸 Lesotho", "🇱🇻 Lettonie", "🇱🇧 Liban", "🇱🇷 Liberia", "🇱🇾 Libye", "🇱🇮 Liechtenstein", "🇱🇹 Lituanie", "🇱🇺 Luxembourg", 
    "🇲🇰 Macédoine du Nord", "🇲🇬 Madagascar", "🇲🇾 Malaisie", "🇲🇼 Malawi", "🇲🇻 Maldives", "🇲️ Mali", "🇲🇹 Malte", "🇲🇦 Maroc", "🇲🇭 Maurice", "🇲🇷 Mauritanie", "🇲🇽 Mexique", "🇫🇲 Micronésie", "🇲🇩 Moldavie", "🇲🇨 Monaco", "🇲🇳 Mongolie", "🇲🇪 Monténégro", "🇲🇿 Mozambique", "🇲🇲 Myanmar", 
    "🇳🇦 Namibie", "🇳🇷 Nauru", "🇳🇵 Népal", "🇳🇮 Nicaragua", "🇳🇪 Niger", "🇳🇬 Nigeria", "🇳🇴 Norvège", "🇳🇿 Nouvelle-Zélande", 
    "🇴🇲 Oman", "🇺🇬 Ouganda", "🇺🇿 Ouzbékistan", 
    "🇵🇰 Pakistan", "🇵🇼 Palaos", "🇵🇸 Palestine", "🇵🇦 Panama", "🇵🇬 Papouasie-Nouvelle-Guinée", "🇵🇾 Paraguay", "🇳🇱 Pays-Bas", "🇵🇪 Pérou", "🇵🇭 Philippines", "🇵🇱 Pologne", "🇵🇹 Portugal", 
    "🇶🇦 Qatar", 
    "🇨🇿 Rép. Tchèque", "🇨🇫 Rép. Centrafricaine", "🇩🇴 Rép. Dominicaine", "🇷🇴 Roumanie", "🇬🇧 Royaume-Uni", "🇷🇺 Russie", "🇷🇼 Rwanda", 
    "🇰🇳 Saint-Christophe-et-Niévès", "🇸🇲 Saint-Marin", "🇻🇨 Saint-Vincent-et-les-Grenadines", "🇱🇨 Sainte-Lucie", "🇸🇧 Salomon", "🇸🇻 Salvador", "🇼🇸 Samoa", "🇸🇹 Sao Tomé-et-Principe", "🇸🇳 Sénégal", "🇷🇸 Serbie", "🇸🇨 Seychelles", "🇸🇱 Sierra Leone", "🇸🇬 Singapour", "🇸🇰 Slovaquie", "🇸🇮 Slovénie", "🇸🇴 Somalie", "🇸🇩 Soudan", "🇸🇸 Soudan du Sud", "🇱🇰 Sri Lanka", "🇸🇪 Suède", "🇨🇭 Suisse", "🇸🇾 Syrie", 
    "🇹🇯 Tadjikistan", "🇹🇿 Tanzanie", "🇹🇩 Tchad", "🇹🇭 Thaïlande", "🇹🇱 Timor oriental", "🇹🇬 Togo", "🇹🇴 Tonga", "🇹🇹 Trinité-et-Tobago", "🇹🇳 Tunisie", "🇹🇲 Turkménistan", "🇹🇷 Turquie", "🇹🇻 Tuvalu", 
    "🇺🇦 Ukraine", "🇺🇾 Uruguay", 
    "🇻🇺 Vanuatu", "🇻🇦 Vatican", "🇻🇪 Venezuela", "🇻🇳 Vietnam", 
    "🇾🇪 Yémen", 
    "🇿🇲 Zambie", "🇿🇼 Zimbabwe"
]

# --- CERVEAU IA ILLIMITÉ (STYLE GOAT) ---
def cerveau_ia_ultime(question):
    q = question.lower().strip()
    
    # 1. IDENTITÉ
    if "qui" in q and ("es" in q or "tes" in q):
        return "Je suis l'IA illimitée de **Règne**. Je connais tout ce qui existe !"
    if "cree" in q or "créé" in q:
        return "Tout ce système a été conçu par le seul et unique GOAT : **Règne**. 👑"

    # 2. CALCULS COMPLEXES
    if re.search(r'\d+', q) and any(op in q for op in ['+', '-', '*', '/']):
        try:
            calcul = "".join(re.findall(r'[0-9\+\-\*\/\.]', q))
            return f"Après analyse, **{calcul} = {eval(calcul)}**. Trop simple pour moi ! 😎"
        except: pass

    # 3. RÉPONSE À TOUT (Culture, Science, Vie)
    # Le chatbot analyse les mots clés pour répondre précisément
    if "bonbon" in q: return "Un bonbon est une sucrerie. Miam ! Mais attention aux dents. 🍬"
    if "belgique" in q: return "La capitale est **Bruxelles** 🇧🇪."
    if "maroc" in q: return "La capitale est **Rabat** 🇲🇦."
    if "france" in q: return "C'est **Paris** 🇫🇷."
    if "pays" in q and "combien" in q: return "Il y a officiellement **195 pays** reconnus par l'ONU. 🌍"
    
    # 4. SALUTATIONS NATURELLES
    if q in ["salut", "bonjour", "wesh", "merhaba"]: 
        return "Salut ! Je suis l'IA de Règne. Je réponds à TOUT. Pose ta question."
    if "ca va" in q or "ça va" in q:
        return "Tranquille, je pète la forme numérique ! Et toi, prêt à hacker les maths ?"

    # 5. MODE RECHERCHE INFINIE (Si l'IA ne connaît pas par cœur)
    return f"Ta question sur '{question}' est excellente. En tant qu'IA de **Règne**, je dirais que c'est un sujet fascinant. Tu veux que j'approfondisse ?"

# --- INTERFACE ---
col_main, col_lang = st.columns([0.8, 0.2])

with col_lang:
    # Menu avec tous les pays du monde
    st.selectbox("🌐 Tous les Pays", pays_monde)

with st.sidebar:
    st.title("🤖 Chatbot 1CA")
    st.write("Assistant du GOAT : **Règne**")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Wesh ! Pose-moi n'importe quelle question, je réponds direct."}]
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    if prompt := st.chat_input("Demande-moi n'importe quoi..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        rep = cerveau_ia_ultime(prompt)
        with st.chat_message("assistant"): st.markdown(rep)
        st.session_state.messages.append({"role": "assistant", "content": rep})

with col_main:
    # Ton logo IMG_0956.png
    try: st.image("IMG_0956.png", width=120)
    except: st.info("Logo Hacker Cosmic")
    
    st.title("Hacker Cosmic 1CA 2026")
    st.markdown("### Créé par **Règne**")
    st.write("---")

    # CALCULATEUR
    p = st.number_input("Prix d'origine (€)", value=460.0)
    r = st.number_input("Remise (%)", value=10.0)
    st.header(f"Total : {p * (1 - r/100):.2f} €")
    
    st.write("---")
    
    # COMPTEUR DE VISITES (GOAT Analytics)
    if 'v' not in st.session_state: st.session_state.v = 11
    st.session_state.v += 1
    st.write(f"🔥 **{st.session_state.v} Hackers** ont visité ce site !")
