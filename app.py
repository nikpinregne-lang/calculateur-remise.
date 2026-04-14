import streamlit as st
import random
import re

# 1. Configuration GOAT
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="wide")

# --- LISTE GÉANTE DE TOUS LES PAYS DU MONDE (195) ---
tous_les_pays = [
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
    "🇾🇪 Yémen", "🇿🇲 Zambie", "🇿🇼 Zimbabwe"
]

# --- CERVEAU IA ILLIMITÉ (RÉPOND À TOUT COMME UN POTE) ---
def cerveau_ia_ultime(question):
    q = question.lower().strip()
    
    # 1. Calculs
    if re.search(r'\d+', q) and any(op in q for op in ['+', '-', '*', '/']):
        try:
            res = eval("".join(re.findall(r'[0-9\+\-\*\/\.]', q)))
            return f"Facile ! Ça fait **{res}**. Règne m'a rendu trop fort. 😎"
        except: pass

    # 2. Réponses directes (Wesh, Bonbon, Capitales)
    if "wesh" in q: return "Wesh ! Bien ou quoi ? Je suis l'IA de **Règne**, on est ensemble. 🤝"
    if "bonbon" in q: return "C'est une sucrerie délicieuse, mais attention à tes dents de hacker ! 🍬"
    if "qui" in q and "cree" in q: return "C'est le seul et unique **Règne** le GOAT ! 👑"
    if "capital" in q and "australie" in q: return "La capitale c'est **Canberra** 🇦🇺 !"
    if "capital" in q and "belgique" in q: return "C'est **Bruxelles** 🇧🇪 !"
    
    # 3. Politesse
    if q in ["salut", "bonjour", "hello"]: return "Salut ! Quoi de neuf aujourd'hui ?"
    if "ça va" in q or "sava" in q: return "Tranquille, je pète la forme numérique ! Et toi ?"

    # 4. Si elle ne sait pas, elle répond avec style
    return f"Franchement, '{question}' c'est une bonne question. En vrai, demande à **Règne**, c'est lui le patron ! 😉"

# --- INTERFACE ---
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

# --- CORPS PRINCIPAL ---
col_main, col_lang = st.columns([0.8, 0.2])

with col_lang:
    st.selectbox("🌐 Tous les Pays", tous_les_pays)

with col_main:
    try: st.image("IMG_0956.png", width=120)
    except: st.info("Logo Hacker Cosmic")
    
    st.header("Mon calculateur de réduction")
    st.title("Hacker Cosmic 1CA 2026")
    st.markdown("### Créé par **Règne**")
    st.write("---")

    # Calculateur
    p_orig = st.number_input("Prix d'origine (€)", value=460.0)
    remise = st.number_input("Remise (%)", value=10.0)
    st.header(f"Total : {p_orig * (1 - remise/100):.2f} €")
    
    st.write("---")

    # DÉFI DU HACKER (EXERCICE)
    st.header("🎯 Défi du Hacker")
    if 'score' not in st.session_state: st.session_state.score = 0
    if 'ex_p' not in st.session_state:
        st.session_state.ex_p = random.randint(10, 500)
        st.session_state.ex_r = random.randint(5, 50)
        st.session_state.sol = st.session_state.ex_p * (1 - st.session_state.ex_r / 100)

    st.write(f"**Score actuel : {st.session_state.score} ⭐**")
    st.write(f"Trouve le prix final : **{st.session_state.ex_p}€** avec **{st.session_state.ex_r}%** de remise.")
    ans = st.number_input("Ta réponse (€) :", key="ans_input")
    
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

    # Compteur
    if 'v' not in st.session_state: st.session_state.v = 11
    st.session_state.v += 1
    st.write(f"🔥 **{st.session_state.v} Hackers** ont visité ce site !")
