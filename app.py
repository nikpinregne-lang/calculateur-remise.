import streamlit as st
import random
import re

# 1. CONFIGURATION GOAT (VITESSE ET STYLE)
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="wide")

# --- LISTE GÉANTE DES 195 PAYS DU MONDE (TRIÉE) ---
tous_les_pays = sorted([
    "🇦🇫 Afghanistan", "🇿🇦 Afrique du Sud", "🇦🇱 Albanie", "🇩🇿 Algérie", "🇩🇪 Allemagne", "🇦🇩 Andorre", "🇦🇴 Angola", "🇦🇬 Antigua-et-Barbuda", "🇸🇦 Arabie Saoudite", "🇦🇷 Argentine", "🇦🇲 Arménie", "🇦🇺 Australie", "🇦🇹 Autriche", "🇦🇿 Azerbaïdjan", 
    "🇧🇸 Bahamas", "🇧🇭 Bahreïn", "🇧🇩 Bangladesh", "🇧🇧 Barbade", "🇧🇪 Belgique", "🇧🇿 Belize", "🇧🇯 Bénin", "🇧🇹 Bhoutan", "🇧🇾 Biélorussie", "🇧🇲 Birmanie", "🇧🇴 Bolivie", "🇧🇦 Bosnie-Herzégovine", "🇧🇼 Botswana", "🇧🇷 Brésil", "🇧🇳 Brunei", "🇧🇬 Bulgarie", "🇧🇫 Burkina Faso", "🇧🇮 Burundi", 
    "🇰🇭 Cambodge", "🇨🇲 Cameroun", "🇨🇦 Canada", "🇨🇻 Cap-Vert", "🇨🇱 Chili", "🇨🇳 Chine", "🇨🇾 Chypre", "🇨🇴 Colombie", "🇰🇲 Comores", "🇨🇬 Congo", "🇨🇩 Congo (RDC)", "🇰🇷 Corée du Sud", "🇰🇵 Corée du Nord", "🇨🇷 Costa Rica", "🇨🇮 Côte d'Ivoire", "🇭🇷 Croatie", "🇨🇺 Cuba", 
    "🇩🇰 Danemark", "🇩🇯 Djibouti", "🇩🇲 Dominique", "🇪🇬 Égypte", "🇦🇪 Émirats Arabes Unis", "🇪🇨 Équateur", "🇪🇷 Érythrée", "🇪🇸 Espagne", "🇪🇪 Estonie", "🇸🇿 Eswatini", "🇺🇸 USA", "🇪🇹 Éthiopie", "🇫🇮 Finlande", "🇫🇷 France", "🇬🇦 Gabon", "🇬🇲 Gambie", "🇬🇪 Géorgie", "🇬🇭 Ghana", "🇬🇷 Grèce", "🇬🇩 Grenade", "🇬🇹 Guatemala", "🇬🇳 Guinée", "🇬🇼 Guinée-Bissau", "🇬🇶 Guinée équatoriale", "🇬🇾 Guyana", "🇭🇹 Haïti", "🇭🇳 Honduras", "🇭🇺 Hongrie", "🇮🇳 Inde", "🇮🇩 Indonésie", "🇮🇶 Irak", "🇮🇷 Iran", "🇮🇪 Irlande", "🇮🇸 Islande", "🇮🇱 Israël", "🇮🇹 Italie", "🇯🇲 Jamaïque", "🇯🇵 Japon", "🇯🇴 Jordanie", "🇰🇿 Kazakhstan", "🇰🇪 Kenya", "🇰🇬 Kirghizistan", "🇰🇮 Kiribati", "🇰🇼 Koweït", "🇱🇦 Laos", "🇱🇸 Lesotho", "🇱🇻 Lettonie", "🇱🇧 Liban", "🇱🇷 Liberia", "🇱🇾 Libye", "🇱🇮 Liechtenstein", "🇱🇹 Lituanie", "🇱🇺 Luxembourg", "🇲🇰 Macédoine du Nord", "🇲🇬 Madagascar", "🇲🇾 Malaisie", "🇲🇼 Malawi", "🇲🇻 Maldives", "🇲️ Mali", "🇲🇹 Malte", "🇲🇦 Maroc", "🇲🇭 Maurice", "🇲🇷 Mauritanie", "🇲🇽 Mexique", "🇫🇲 Micronésie", "🇲🇩 Moldavie", "🇲🇨 Monaco", "🇲🇳 Mongolie", "🇲🇪 Monténégro", "🇲🇿 Mozambique", "🇳🇦 Namibie", "🇳🇷 Nauru", "🇳🇵 Népal", "🇳🇮 Nicaragua", "🇳🇪 Niger", "🇳🇬 Nigeria", "🇳🇴 Norvège", "🇳🇿 Nouvelle-Zélande", "🇴🇲 Oman", "🇺🇬 Ouganda", "🇺🇿 Ouzbékistan", "🇵🇰 Pakistan", "🇵🇼 Palaos", "🇵🇸 Palestine", "🇵🇦 Panama", "🇵🇬 Papouasie-Nouvelle-Guinée", "🇵🇾 Paraguay", "🇳🇱 Pays-Bas", "🇵🇪 Pérou", "🇵🇭 Philippines", "🇵🇱 Pologne", "🇵🇹 Portugal", "🇶🇦 Qatar", "🇨🇿 Rép. Tchèque", "🇷🇴 Roumanie", "🇬🇧 Royaume-Uni", "🇷🇺 Russie", "🇷🇼 Rwanda", "🇸🇳 Sénégal", "🇷🇸 Serbie", "🇸🇨 Seychelles", "🇸🇬 Singapour", "🇸🇰 Slovaquie", "🇸🇮 Slovénie", "🇸🇴 Somalie", "🇸🇩 Soudan", "🇱🇰 Sri Lanka", "🇸🇪 Suède", "🇨🇭 Suisse", "🇸🇾 Syrie", "🇹🇯 Tadjikistan", "🇹🇿 Tanzanie", "🇹🇩 Tchad", "🇹🇭 Thaïlande", "🇹🇬 Togo", "🇹🇳 Tunisie", "🇹🇲 Turkménistan", "🇹🇷 Turquie", "🇺🇦 Ukraine", "🇺🇾 Uruguay", "🇻🇦 Vatican", "🇻🇪 Venezuela", "🇻🇳 Vietnam", "🇾🇪 Yémen", "🇿🇲 Zambie", "🇿🇼 Zimbabwe"
])

# --- CERVEAU DE L'IA ILLIMITÉE (CONNAISSANCE TOTALE) ---
def cerveau_ia_goat(question):
    q = question.lower().strip()
    
    # 1. Réponse aux signes ( . ? ! )
    if q in [".", "?", "!", "..."]: return "Même tes points de suspension ont du style ! Pose une vraie question, le Hacker. 😎"
    
    # 2. Salutations et politesse (Le chatbot est cool)
    if any(s in q for s in ["wesh", "wsh", "bien ou quoi"]): return "Wesh ! Bien ou quoi ? On gère le système avec **Règne**. 🤝"
    if any(s in q for s in ["salut", "bonjour", "hello", "sava", "ça va"]): return "Salut ! Je suis boosté à l'énergie cosmique ! Et toi ? 😊"

    # 3. Calculs directs (ex: 1+1, 15*3)
    if re.search(r'\d+', q) and any(op in q for op in ['+', '-', '*', '/']):
        try:
            calcul = "".join(re.findall(r'[0-9\+\-\*\/\.]', q))
            return f"Résultat : **{eval(calcul)}**. Trop facile ! 🧠"
        except: pass

    # 4. BASE DE CONNAISSANCES INFINIE (Science, Espace, Monde)
    connaissances = {
        "planète": "Une planète est un corps céleste en orbite autour d'une étoile. Il y en a 8 dans notre système ! 🪐",
        "bonbon": "Une sucrerie délicieuse, mais attention à tes dents de hacker ! 🍬",
        "soleil": "C'est notre étoile ! Une boule de feu géante qui nous donne la vie. ☀️",
        "qui": "Le créateur et le seul patron ici, c'est le GOAT **Règne**. 👑",
        "belgique": "Capitale : Bruxelles 🇧🇪.",
        "australie": "Capitale : Canberra 🇦🇺.",
        "maroc": "Capitale : Rabat 🇲🇦.",
        "ia": "Je suis une Intelligence Artificielle conçue pour être aussi forte que Règne !",
        "2026": "C'est l'année de la révolution Hacker Cosmic ! 🚀"
    }
    for mot, rep in connaissances.items():
        if mot in q: return rep

    # 5. Réponse Libre (Si l'IA ne sait pas, elle improvise comme un humain)
    return f"Écoute, '{question}' c'est super profond. En tant qu'IA, je dirais que c'est une pièce du puzzle universel de **Règne**. Dis-m'en plus ! 😉"

# --- INTERFACE ---
col_main, col_lang = st.columns([0.8, 0.2])

with col_lang:
    # Menu déroulant avec absolument TOUS les pays
    st.selectbox("🌐 Pays / Language", tous_les_pays)

with st.sidebar:
    st.title("🤖 Chatbot 1CA")
    st.write(f"Assistant du GOAT : **Règne**")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Wesh ! Pose-moi n'importe quoi, je réponds à TOUT."}]
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
    
    st.header("Mon calculateur de réduction") # Le titre est revenu !
    st.title("Hacker Cosmic 1CA 2026")
    st.markdown("### Créé par **Règne**")
    st.write("---")

    # CALCULATEUR
    p_orig = st.number_input("Prix d'origine (€)", value=460.0)
    remise = st.number_input("Remise (%)", value=10.0)
    st.header(f"Total : {p_orig * (1 - remise/100):.2f} €")
    
    st.write("---")

    # LE DÉFI DU HACKER (RÉPARÉ ET COMPLET)
    st.header("🎯 Défi du Hacker")
    if 'score' not in st.session_state: st.session_state.score = 0
    if 'ex_p' not in st.session_state:
        st.session_state.ex_p = random.randint(10, 500)
        st.session_state.ex_r = random.randint(5, 50)
        st.session_state.sol = st.session_state.ex_p * (1 - st.session_state.ex_r / 100)

    st.write(f"**Score actuel : {st.session_state.score} ⭐**")
    st.write(f"Trouve le prix : **{st.session_state.ex_p}€** avec **{st.session_state.ex_r}%** de remise.")
    ans = st.number_input("Ta réponse (€) :", key="ans_input", value=0.0)
    
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Vérifier"):
            if abs(ans - st.session_state.sol) < 0.1:
                st.success("✅ GAGNÉ ! +1 Point")
                st.session_state.score += 1
                del st.session_state['ex_p']
                st.rerun()
            else:
                st.error(f"❌ FAUX ! C'était {st.session_state.sol:.2f}€")
                st.session_state.score = 0
    with c2:
        if st.button("Nouveau Défi 🔄"):
            del st.session_state['ex_p']
            st.rerun()

    # COMPTEUR DE VISITES
    if 'v' not in st.session_state: st.session_state.v = 19
    st.session_state.v += 1
    st.write(f"🔥 **{st.session_state.v} Hackers ont visité ce site !**")
