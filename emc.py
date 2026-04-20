import streamlit as st

st.set_page_config(page_title="Projet EMC - Réseaux Sociaux", layout="centered")

# --- MÉMOIRE DU CHAT ---
if 'messages' not in st.session_state:
    st.session_state.messages = []

# --- TITRE ET ARGUMENTATION (Ce qu'il y a sur ta feuille) ---
st.title("📱 Les réseaux sociaux nous rendent-ils plus libres ou plus manipulables ?")

st.markdown("""
### 🧠 Question Philosophique
**« Sommes-nous encore maîtres de nos choix face aux algorithmes ? »**

### ⚖️ Les deux arguments clés :
1. **La Liberté :** Un accès universel à la culture et une liberté d'expression sans précédent.
2. **La Manipulation :** L'enfermement dans des "bulles de filtres" et l'influence des algorithmes sur nos opinions.

---
""")

# --- LE CHATBOT CITOYEN ---
st.header("🤖 Assistant Citoyen Éclairé")
st.write("Posez une question sur l'influence des réseaux sociaux :")

# Interface du chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ex: Est-ce que TikTok me manipule ?"):
    # Ajouter le message de l'utilisateur
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Réponse de l'IA (Analyse citoyenne)
    reponse = f"Analyse de '{prompt}' : Attention, les algorithmes utilisent vos données pour vous montrer ce que vous voulez voir, ce qui peut limiter votre esprit critique."
    st.session_state.messages.append({"role": "assistant", "content": reponse})
    with st.chat_message("assistant"):
        st.markdown(reponse)

# --- BOUTON POUR TOUT EFFACER ---
st.sidebar.title("Options")
if st.sidebar.button("🗑️ Effacer la discussion"):
    st.session_state.messages = []
    st.rerun()
