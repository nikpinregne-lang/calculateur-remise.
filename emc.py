import streamlit as st

st.set_page_config(page_title="Projet EMC - Réseaux Sociaux", layout="centered")

# --- MÉMOIRE DU CHAT ---
if 'messages' not in st.session_state:
    st.session_state.messages = []

# --- TITRE ET ARGUMENTS COMPLETS ---
st.title("📱 Les réseaux sociaux : Liberté ou Manipulation ?")

st.markdown("""
### 🧠 Question Philosophique
**« Sommes-nous encore maîtres de nos choix face aux algorithmes ? »**

### ⚖️ Les deux arguments clés :

1. **La Liberté (Émancipation Numérique) :**
    *   **Accès Universel :** Les réseaux permettent à chacun d'accéder gratuitement à une infinité de savoirs et de cultures, brisant les barrières sociales.
    *   **Liberté d'Expression :** Ils offrent une voix aux citoyens pour défendre des causes et créer des communautés d'entraide mondiales sans passer par les médias traditionnels.

2. **La Manipulation (L'Invisibilité des Algorithmes) :**
    *   **Bulles de Filtres :** Les algorithmes ne nous montrent que ce que nous aimons déjà. Cela enferme notre esprit critique dans une "chambre d'écho" où l'on n'entend plus d'avis contraires.
    *   **Économie de l'Attention :** Les plateformes utilisent des mécanismes psychologiques (scroll infini, notifications) pour nous rendre dépendants et maximiser le profit publicitaire.

---
### 🛡️ Solution Citoyenne
*Développer son **esprit critique** et exiger la **transparence des algorithmes** pour redevenir acteur de sa vie numérique.*
""")

# --- LE CHATBOT CITOYEN ---
st.header("🤖 Assistant Citoyen Éclairé")
st.write("Posez une question sur l'influence des réseaux sociaux :")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ex: Est-ce que les algorithmes choisissent pour moi ?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    reponse = f"Analyse de '{prompt}' : C'est une question clé. L'algorithme cherche à prédire votre comportement. Pour rester libre, il faut varier ses sources d'information !"
    st.session_state.messages.append({"role": "assistant", "content": reponse})
    with st.chat_message("assistant"):
        st.markdown(reponse)

# --- OPTIONS ---
st.sidebar.title("Options")
if st.sidebar.button("🗑️ Effacer la discussion"):
    st.session_state.messages = []
    st.rerun()
