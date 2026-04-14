import streamlit as st
import random
import re

# 1. CONFIGURATION GOAT (TOUJOURS EN PREMIER)
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="wide")

# --- LISTE GÉANTE DE TOUS LES PAYS DU MONDE (ORDRE ALPHABÉTIQUE) ---
tous_les_pays = sorted([
    "🇦🇫 Afghanistan", "🇿🇦 Afrique du Sud", "🇦🇱 Albanie", "🇩🇿 Algérie", "🇩🇪 Allemagne", "🇦🇩 Andorre", "🇦🇴 Angola", "🇦🇬 Antigua-et-Barbuda", "🇸🇦 Arabie Saoudite", "🇦🇷 Argentine", "🇦🇲 Arménie", "🇦🇺 Australie", "🇦🇹 Autriche", "🇦🇿 Azerbaïdjan", 
    "🇧🇸 Bahamas", "🇧🇭 Bahreïn", "🇧🇩 Bangladesh", "🇧🇧 Barbade", "🇧🇪 Belgique", "🇧🇿 Belize", "🇧🇯 Bénin", "🇧🇹 Bhoutan", "🇧🇾 Biélorussie", "🇧🇲 Birmanie", "🇧🇴 Bolivie", "🇧🇦 Bosnie-Herzégovine", "🇧🇼 Botswana", "🇧🇷 Brésil", "🇧🇳 Brunei", "🇧🇬 Bulgarie", "🇧🇫 Burkina Faso", "🇧🇮 Burundi", 
    "🇰🇭 Cambodge", "🇨🇲 Cameroun", "🇨🇦 Canada", "🇨🇻 Cap-Vert", "🇨🇱 Chili", "🇨🇳 Chine", "🇨🇾 Chypre", "🇨🇴 Colombie", "🇰🇲 Comores", "🇨🇬 Congo", "🇨🇩 Congo (RDC)", "🇰🇷 Corée du Sud", "🇰🇵 Corée du Nord", "🇨🇷 Costa Rica", "🇨🇮 Côte d'Ivoire", "🇭🇷 Croatie", "🇨🇺 Cuba", 
    "🇩🇰 Danemark", "🇩🇯 Djibouti", "🇩🇲 Dominique", "🇪🇬 Égypte", "🇦🇪 Émirats Arabes Unis", "🇪🇨 Équateur", "🇪🇷 Érythrée", "🇪🇸 Espagne", "🇪🇪 Estonie", "🇸🇿 Eswatini", "🇺🇸 USA", "🇪🇹 Éthiopie", "🇫🇮 Finlande", "🇫🇷 France", "🇬🇦 Gabon", "🇬🇲 Gambie", "🇬🇪 Géorgie", "🇬🇭 Ghana", "🇬🇷 Grèce", "🇬🇩 Grenade", "🇬🇹 Guatemala", "🇬🇳 Guinée", "🇬🇼 Guinée-Bissau", "🇬🇶 Guinée équatoriale", "🇬🇾 Guyana", "🇭🇹 Haïti", "🇭🇳 Honduras", "🇭🇺 Hongrie", "🇮🇳 Inde", "🇮🇩 Indonésie", "🇮🇶 Irak", "🇮🇷 Iran", "🇮🇪 Irlande", "🇮🇸 Islande", "🇮🇱 Israël", "🇮🇹 Italie", "🇯🇲 Jamaïque", "🇯🇵 Japon", "🇯🇴 Jordanie", "🇰🇿 Kazakhstan", "🇰🇪 Kenya", "🇰🇬 Kirghizistan", "🇰🇮 Kiribati", "🇰🇼 Koweït", "🇱🇦 Laos", "🇱🇸 Lesotho", "🇱🇻 Lettonie", "🇱🇧 Liban", "🇱🇷 Liberia", "🇱🇾 Libye", "🇱🇮 Liechtenstein", "🇱🇹 Lituanie", "🇱🇺 Luxembourg", "🇲🇰 Macédoine du Nord", "🇲🇬 Madagascar", "🇲🇾 Malaisie", "🇲🇼 Malawi", "🇲🇻 Maldives", "🇲️ Mali", "🇲🇹 Malte", "🇲🇦 Maroc", "🇲🇭 Maurice", "🇲🇷 Mauritanie", "🇲🇽 Mexique", "🇫🇲 Micronésie", "🇲🇩 Moldavie", "🇲🇨 Monaco", "🇲🇳 Mongolie", "🇲🇪 Monténégro", "🇲🇿 Mozambique", "🇳🇦 Namibie", "🇳🇷 Nauru", "🇳🇵 Népal", "🇳🇮 Nicaragua", "🇳🇪 Niger", "🇳🇬 Nigeria", "🇳🇴 Norvège", "🇳🇿 Nouvelle-Zélande", "🇴🇲 Oman", "🇺🇬 Ouganda", "🇺🇿 Ouzbékistan", "🇵🇰 Pakistan", "🇵🇼 Palaos", "🇵🇸 Palestine", "🇵🇦 Panama", "🇵🇬 Papouasie-Nouvelle-Guinée", "🇵🇾 Paraguay", "🇳🇱 Pays-Bas", "🇵🇪 Pérou", "🇵🇭 Philippines", "🇵🇱 Pologne", "🇵🇹 Portugal", "🇶🇦 Qatar", "🇨🇿 Rép. Tchèque", "🇷🇴 Roumanie", "🇬🇧 Royaume-Uni", "🇷🇺 Russie", "🇷🇼 Rwanda", "🇸🇳 Sénégal", "🇷🇸 Serbie", "🇸🇨 Seychelles", "🇸🇬 Singapour", "🇸🇰 Slovaquie", "🇸🇮 Slovénie", "🇸🇴 Somalie", "🇸🇩 Soudan", "🇱🇰 Sri Lanka", "🇸🇪 Suède", "🇨🇭 Suisse", "🇸🇾 Syrie", "🇹🇯 Tadjikistan", "🇹🇿 Tanzanie", "🇹🇩 Tchad", "🇹🇭 Thaïlande", "🇹🇬 Togo", "🇹🇳 Tunisie", "🇹🇲 Turkménistan", "🇹🇷 Turquie", "🇺🇦 Ukraine", "🇺🇾 Uruguay", "🇻🇦 Vatican", "🇻🇪 Venezuela", "🇻🇳 Vietnam", "🇾🇪 Yémen", "🇿🇲 Zambie", "🇿🇼 Zimbabwe"
])

# --- CERVEAU IA ILLIMITÉ (PERSONNALITÉ GOAT 😎) ---
def cerveau_ia_ultime(question):
    q = question.lower().strip()
    
    # 1. Réponse aux signes ( . ? ! )
    if q in [".", "?", "!", "..."]: 
        return "Même tes points de suspension ont du style ! Dis-m'en plus, je suis prêt. 😎"
    
    # 2. Salutations et politesse
    if any(s in q for s in ["wesh", "wsh", "bien ou quoi"]): 
        return "Wesh ! Bien ou quoi ? Je suis l'IA de **Règne**, on gère le système ensemble. 🤝"
    if any(s in q for s in ["salut", "bonjour", "hello", "sava", "ça va"]): 
        return "Salut ! Je vais super bien, boosté à l'énergie de **Règne**. Et toi ? 😊"

    # 3. Calculs directs (ex: 1+1, 15*3, etc.)
    if re.search(r'\d+', q) and any(op in q for op in ['+', '-', '*', '/']):
        try:
            calcul = "".join(re.findall(r'[0-9\+\-\*\/\.]', q))
            return f"Après analyse : **{calcul} = {eval(calcul)}**. Trop facile pour moi ! 🧠"
        except: pass

    # 4. Culture G (Capitales, Définitions, Monde)
    if "bonbon" in q: return "Le bonbon est une confiserie sucrée. Miam, mais attention aux dents ! 🍬"
    if "qui" in q and "cree" in q: return "Le seul et unique créateur, c'est le GOAT **Règne**. 👑"
    if "belgique" in q: return "La capitale c'est **Bruxelles** 🇧🇪 !"
    if "maroc" in q: return "La capitale c'est **Rabat** 🇲🇦 !"

    # 5. Réponse Libre (Si l'IA ne sait pas, elle discute vraiment comme un pote)
    return f"Franchement, ta question sur '{question}' est super stylée. En tant qu'IA de **Règne**, je trouve ça fascinant. Dis-m'en plus ! 😉"

# --- INTERFACE ---
col_main, col_lang = st.columns([0.8, 0.2])

with col_lang:
    # Menu déroulant avec absolument TOUS les pays
    st.selectbox("🌐 Pays / Language", tous_les_pays)

with st.sidebar:
    st.title("🤖 Chatbot 1CA")
    st.write(f"Assistant du GOAT : **Règne**")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Wesh ! Je suis l'IA illimitée de Règne. Pose-moi n'importe quoi !"}]
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    if prompt := st.chat_input("Demande-moi n'importe quoi..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        rep = cerveau_ia_ultime(prompt)
        with st.chat_message("assistant"): st.markdown(rep)
        st.session_state.messages.append({"role": "assistant", "content": rep})

with col_main:
    # LOGO ET TITRES RÉPARÉS
    try: st.image("IMG_0956.png", width=130)
    except: st.info("Logo Hacker Cosmic")
    
    st.header("Mon calculateur de réduction") # REVOILÀ TON TITRE !
    st.title("Hacker Cosmic 1CA 2026")
    st.markdown("### Créé par **Règne**")
    st.write("---")

    # CALCULATEUR
    p_orig = st.number_input("Prix d'origine (€)", value=460.0)
    remise = st.number_input("Remise (%)", value=10.0)
    st.header(f"Total : {p_orig * (1 - remise/100):.2f} €")
    
    st.write("---")

    # LE DÉFI DU HACKER (EXERCICE AVEC SCORE)
    st.header("🎯 Défi du Hacker")
    if 'score' not in st.session_state: st.session_state.score = 0
    if 'ex_p' not in st.session_state:
        st.session_state.ex_p = random.randint(10, 500)
        st.session_state.ex_r = random.randint(5, 50)
        st.session_state.sol = st.session_state.ex_p * (1 - st.session_state.ex_r / 100)

    st.write(f"**Score actuel : {st.session_state.score} ⭐**")
    st.write(f"DÉFI : {st.session_state.ex_p}€ avec {st.session_state.ex_r}% de remise.")
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
    if 'v' not in st.session_state: st.session_state.v = 15
    st.session_state.v += 1
    st.write(f"🔥 **{st.session_state.v} Hackers ont visité ce site !**")
