
import streamlit as st
import random
import re

# 1. Configuration
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="wide")

# --- CERVEAU ILLIMITÉ ---
def cerveau_ia_illimite(question):
    q = question.lower().strip()
    if re.search(r'\d+', q) and any(op in q for op in ['+', '-', '*', '/']):
        try:
            calcul = "".join(re.findall(r'[0-9\+\-\*\/\.]', q))
            return f"Après analyse, **{calcul} est égal à {eval(calcul)}**. Pas mal, non ? 😎"
        except: pass
    if any(word in q for word in ["salut", "bonjour", "hello"]):
        return "Salut ! Comment vas-tu aujourd'hui ? 😊"
    elif any(word in q for word in ["merci", "bravo"]):
        return "Tout le plaisir est pour moi ! ✨"
    elif "ça va" in q or "sava" in q:
        return "Je vais super bien ! Je suis en pleine forme numérique grâce à **Règne**. Et toi ?"
    elif "bonbon" in q:
        return "Un bonbon est une confiserie sucrée. C'est délicieux ! 🍬"
    elif "qui" in q and "tes" in q:
        return "Je suis l'assistant intelligent de **Règne**, le GOAT du projet 1CA !"
    return f"Ta question sur '{question}' est très pertinente. En tant qu'IA, je dirais que c'est un sujet qui mérite réflexion."

# --- INTERFACE ---
col_main, col_lang = st.columns([0.8, 0.2])

with col_lang:
    languages = {
        "🇫🇷 Français": "Calculateur Hacker Cosmic 1CA",
        "🇸🇦 Arabie Saoudite": "حاسبة هكر كوزميك 1CA",
        "🇲🇦 Maroc": "حاسبة هكر كوزميك 1CA",
        "🇷🇴 Română": "Calculator Hacker Cosmic 1CA",
        "🇺🇦 Українська": "Калькулятор Hacker Cosmic 1CA"
    }
    sel = st.selectbox("🌐 Pays & Langues", list(languages.keys()))

with st.sidebar:
    st.title("🤖 Chatbot 1CA")
    st.write("Assistant de **Règne**")
    
    # Phrase d'accueil exacte
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Salut ! Je suis ton ia illimité. pose moi nimporte quelle question"}]
    
    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])
            # Petit bouton pour la voix
            if m["role"] == "assistant":
                if st.button("🔊 Écouter", key=m["content"][:10] + str(random.random())):
                    st.components.v1.html(f"""
                        <script>
                        var msg = new SpeechSynthesisUtterance("{m['content'].replace('**', '')}");
                        msg.lang = 'fr-FR';
                        window.speechSynthesis.speak(msg);
                        </script>
                    """, height=0)

    if prompt := st.chat_input("Écris-moi..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        rep = cerveau_ia_illimite(prompt)
        st.session_state.messages.append({"role": "assistant", "content": rep})
        st.rerun()

with col_main:
    try: st.image("IMG_0956.png", width=130)
    except: st.info("Logo Hacker Cosmic")
    st.title(languages[sel] + " 2026")
    st.write("### Créé par **Règne**")
    st.write("---")
    p = st.number_input("Prix (€)", min_value=0.0, value=100.0)
    r = st.number_input("Réduction (%)", min_value=0.0, max_value=100.0, value=10.0)
    st.header(f"Total : {p * (1 - r / 100):.2f} €")
