import streamlit as st

st.set_page_config(page_title="Exposé EMC", layout="centered")

# --- TITRE PRINCIPAL ---
st.title("📱 Les réseaux sociaux nous rendent-ils plus libres ou plus manipulables ?")
st.subheader("Étude de l'influence des algorithmes sur le citoyen")

st.divider()

# --- QUESTION PHILOSOPHIQUE ---
st.markdown("""
### 🧠 Question Philosophique
**« Sommes-nous encore maîtres de nos choix face à des systèmes conçus pour anticiper nos désirs ? »**
""")

st.divider()

# --- LES ARGUMENTS CLÉS ---
st.markdown("""
### ⚖️ Les deux arguments clés :

#### 1. La Liberté (L’Émancipation Numérique)
*   **Accès Universel au Savoir :** Les réseaux brisent les barrières géographiques et sociales. Tout le monde peut accéder gratuitement à une infinité de connaissances (tutoriels, cours, cultures).
*   **Liberté d'Expression :** Ils offrent une voix aux citoyens sans passer par les médias traditionnels, permettant de défendre des causes importantes et de créer des communautés mondiales.

#### 2. La Manipulation (L’Invisibilité des Algorithmes)
*   **Les Bulles de Filtres :** Pour maximiser notre temps de connexion, les algorithmes ne nous montrent que ce que nous aimons déjà. Cela affaiblit notre esprit critique et nous enferme dans nos propres certitudes.
*   **L'Économie de l'Attention :** Les plateformes (TikTok, Instagram) utilisent des mécanismes psychologiques comme le "scroll infini" pour capter notre temps de cerveau disponible au profit des publicitaires.
""")

st.divider()

# --- CONCLUSION & SOLUTION ---
st.markdown("""
### 🛡️ Solution Citoyenne
Pour rester libre, le citoyen doit **développer son esprit critique**, varier ses sources d'information et exiger la **transparence des algorithmes** (Open Source) afin de redevenir acteur de sa vie numérique.
""")
