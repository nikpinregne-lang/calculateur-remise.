import streamlit as st
import random
import re

# 1. Configuration GOAT
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="wide")

# --- LA LISTE GÉANTE DES 195 PAYS (Remets bien tous tes pays ici) ---
tous_les_pays = sorted([
    "🇫🇷 France", "🇦🇫 Afghanistan", "🇿🇦 Afrique du Sud", "🇦🇱 Albanie", "🇩🇿 Algérie", "🇩🇪 Allemagne", 
    "🇦🇩 Andorre", "🇦🇴 Angola", "🇦🇮 Anguilla", "🇦🇬 Antigua-et-Barbuda", "🇸🇦 Arabie Saoudite", 
    "🇦🇷 Argentine", "🇦🇲 Arménie", "🇦🇺 Australie", "🇦🇹 Autriche", "🇦🇿 Azerbaïdjan", "🇧🇸 Bahamas", 
    "🇧🇭 Bahreïn", "🇧🇩 Bangladesh", "🇧🇧 Barbade", "🇧🇪 Belgique", "🇧🇿 Belize", "🇧🇯 Bénin", 
    "🇧🇹 Bhoutan", "🇧🇾 Biélorussie", "🇧🇲 Birmanie", "🇧🇴 Bolivie", "🇧🇦 Bosnie-Herzégovine", 
    "🇧🇼 Botswana", "🇧🇷 Brésil", "🇧🇳 Brunei", "🇧🇬 Bulgarie", "🇧🇫 Burkina Faso", "🇧🇮 Burundi",
    "🇰🇭 Cambodge", "🇨🇲 Cameroun", "🇨🇦 Canada", "🇨🇻 Cap-Vert", "🇨🇱 Chili", "🇨🇳 Chine", "🇺🇸 USA"
    # ... Continue ta liste ici comme dans ton code original
])

# --- DICTIONNAIRE DES LANGUES (Pour le calculateur) ---
trads = {
    "FR": {"titre": "Mon calculateur de réduction", "prix": "Prix d'origine (€)", "remise": "Remise (%)", "total": "Total :"},
    "EN": {"titre": "My Discount Calculator", "prix": "Original Price ($)", "remise": "Discount (%)", "total": "Total:"},
    "AR": {"titre": "حاسبة الخصم الخاصة بي", "prix": "السعر الأصلي", "remise": "خصم (%)", "total": "المجموع :"}
}

# --- CERVEAU IA GOAT ILLIMITÉ (TON CODE ORIGINAL) ---
def cerveau_ia_goat(question):
    q = question.lower().strip()
    
    # 1. Culture G
    connaissances = {
        "canada": "Ottawa 🇨🇦", "france": "Paris 🇫🇷", "maroc": "Rabat 🇲🇦", 
        "belgique": "Bruxelles 🇧🇪", "australie": "Canberra 🇦🇺", "usa": "Washington D.C. 🇺🇸",
        "allemagne": "Berlin 🇩🇪", "italie": "Rome 🇮🇹", "espagne": "Madrid 🇪🇸",
        "bonbon": "Une sucrerie délicieuse. Miam ! 🍬",
        "qui": "Le seul patron ici, c'est le GOAT **Règne**. 👑"
    }
    for mot, rep in connaissances.items():
        if mot in q: return f"La réponse est **{rep}**."

    # 2. Maths
    if re.search(r'\d+', q) and any(op in q for op in ['+', '-', '*', '/']):
        try:
            res = eval("".join(re.findall(r'[0-9\+\-\*\/\.]', q)))
            return f"Résultat : **{res}**. Trop facile ! 😎"
        except: pass

    # 3. Style Humain
    if any(s in q for s in ["wesh", "salut", "bonjour", "sava", "ça va"]):
        return "Wesh ! Je suis l'IA de **Règne**. Je réponds à TOUT. Pose ta question."
    
    return f"Pour '{question}', je dirais que c'est captivant ! Dis-m'en plus. 😉"

# --- INTERFACE ---
col_main, col_lang = st.columns([0.8, 0.2])

with col_lang:
    # On trouve l'index de la France pour que le site s'ouvre en Français
    try: idx = tous_les_pays.index("🇫🇷 France")
    except: idx = 0
    pays = st.selectbox("🌐 Tous les Pays", tous_les_pays, index=idx)

# LOGIQUE DE LANGUE (Pour que ça marche enfin !)
L = trads["FR"] # Français par défaut
if "Afghanistan" in pays or "Algérie" in pays or "Maroc" in pays:
    L = trads["AR"]
elif "USA" in pays or "Canada" in pays or "Australie" in pays:
    L = trads["EN"]

# CHATBOT DANS LA SIDEBAR (TON CODE ORIGINAL)
with st.sidebar:
    st.title("🤖 Chatbot 1CA")
    st.write(f"Assistant de **Règne**")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Wesh ! Demande-moi n'importe quoi."}]
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    if prompt := st.chat_input("Écris-moi..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        rep = cerveau_ia_goat(prompt)
        with st.chat_message("assistant"): st.markdown(rep)
        st.session_state.messages.append({"role": "assistant", "content": rep})

# PARTIE PRINCIPALE (TON CODE ORIGINAL)
with col_main:
    try: st.image("IMG_0956.png", width=120)
    except: pass

    st.header(L["titre"])
    st.title("Hacker Cosmic 1CA 2026")
    st.subheader("Créé par **Règne**")
    st.write("---")

    # CALCULATEUR
    p = st.number_input(L["prix"], value=460.0)
    r = st.number_input(L["remise"], value=10.0)
    st.header(f"{L['total']} {p * (1 - r/100):.2f}")
    
    st.write("---")

    # DÉFI DU HACKER (TON CODE ORIGINAL)
    st.header("🎯 Défi du Hacker")
    if 'score' not in st.session_state: st.session_state.score = 0
    if 'ex_p' not in st.session_state:
        st.session_state.ex_p, st.session_state.ex_r = random.randint(10, 500), random.randint(5, 50)
        st.session_state.sol = st.session_state.ex_p * (1 - st.session_state.ex_r / 100)

    st.write(f"**Score : {st.session_state.score} ⭐**")
    st.write(f"Défi : **{st.session_state.ex_p}€** avec **{st.session_state.ex_r}%** de remise.")
    ans = st.number_input("Ta réponse (€) :", key="ans_input", value=0.0)
    
    if st.button("Vérifier"):
        if abs(ans - st.session_state.sol) < 0.1:
            st.success("✅ GAGNÉ ! +1 Point")
            st.session_state.score += 1
            del st.session_state['ex_p']
            st.rerun()
        else:
            st.error(f"❌ FAUX ! C'était {st.session_state.sol:.2f}€")
            st.session_state.score = 0

    st.write(f"🔥 **{random.randint(25, 60)} Hackers ont visité ce site !**")
