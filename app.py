import streamlit as st
import random

# 1. Configuration de la page
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="wide")

# --- FONCTION INTELLIGENTE (RÉPOND À TOUT) ---
def cerveau_ia(question):
    q = question.lower()
    # Réponses personnalisées
    if "qui" in q and "cree" in q:
        return "Ce site incroyable a été créé par mon maître, le grand **Règne** ! 👑"
    elif "bonbon" in q:
        return "Un bonbon est une friandise faite de sucre et d'arômes. **Règne** m'a dit de ne pas en abuser pour les dents ! 🍬"
    elif "ca va" in q or "ça va" in q:
        return "Je vais super bien ! Je suis boosté par l'énergie de **Règne**. Et toi ?"
    elif "meteo" in q:
        return "Il fait toujours beau dans l'univers Hacker Cosmic 2026 ! ☀️"
    elif "calcul" in q or "math" in q:
        return "Je suis un expert ! Utilise le calculateur de **Règne** au centre de l'écran."
    elif "ia" in q or "robot" in q:
        return "Je suis une intelligence artificielle au service de **Règne**."
    else:
        # Réponse quand il ne connaît pas le mot exact
        return f"'{question}' ? C'est une excellente question ! En tant qu'IA de **Règne**, je trouve cela passionnant. Tu veux que j'en parle à mon créateur ?"

# --- BARRE LATÉRALE : CHATBOT ---
with st.sidebar:
    st.title("🤖 Chatbot 1CA")
    st.write("Assistant officiel de **Règne**")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Salut ! Je suis l'IA de **Règne**. Pose-moi n'importe quelle question sur le monde, je répondrai à tout !"}]

    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])

    if prompt := st.chat_input("Dis-moi n'importe quoi..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        
        # Le chatbot utilise son cerveau
        reponse = cerveau_ia(prompt)

        with st.chat_message("assistant"): st.markdown(reponse)
        st.session_state.messages.append({"role": "assistant", "content": reponse})

# --- CORPS PRINCIPAL ---
col_main, col_lang = st.columns([0.8, 0.2])

with col_lang:
    st.selectbox("🌐 Langue", ["Français", "English", "Español"])

with col_main:
    try:
        st.image("IMG_0956.png", width=200)
    except:
        st.info("Logo Hacker Cosmic")

    st.title("Calculateur Hacker Cosmic 1CA 2026")
    st.markdown("### Créé par **Règne**")
    st.write("---")

    # Calculateur
    c1, c2 = st.columns(2)
    with c1:
        prix_orig = st.number_input("Prix d'origine (€)", min_value=0.0, value=100.0)
    with c2:
        reduction = st.number_input("Réduction (%)", min_value=0.0, max_value=100.0, value=10.0)
    
    st.header(f"Total : {prix_orig * (1 - reduction / 100):.2f} €")

    st.write("---")

    # Exercice Infini
    st.header("📝 Exercice Infini de Règne")
    if 'exo_prix' not in st.session_state:
        st.session_state.exo_prix = random.randint(10, 500)
        st.session_state.exo_remise = random.randint(5, 75)
        st.session_state.sol = st.session_state.exo_prix * (1 - st.session_state.exo_remise / 100)

    st.write(f"**Défi :** Un article coûte **{st.session_state.exo_prix} €** avec **{st.session_state.exo_remise} %** de remise.")
    user_ans = st.number_input("Ta réponse (€) :", key="ans_input")

    if st.button("Vérifier"):
        if abs(user_ans - st.session_state.sol) < 0.05:
            st.success("✅ Bravo ! Tu es digne de Règne !")
        else:
            st.error(f"❌ La réponse était {st.session_state.sol:.2f} €")
    
    if st.button("Nouvel exercice 🔄"):
        del st.session_state['exo_prix']
        st.rerun()
