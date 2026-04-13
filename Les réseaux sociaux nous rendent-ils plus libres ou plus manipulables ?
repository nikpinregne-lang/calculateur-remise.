import streamlit as st

st.set_page_config(page_title="Projet EMC - Réseaux Sociaux", layout="wide")

st.title("📱 Les réseaux : Liberté ou Manipulation ?")

# --- ARGUMENTATION ---
st.markdown("""
### 🧠 Ma réflexion
Les algorithmes nous aident à trouver ce qu'on aime, mais ils peuvent aussi nous enfermer. 
C'est le paradoxe de la **bulle de filtre**.
""")

# --- GALERIE D'IMAGES (Utilise tes fichiers déjà présents) ---
st.header("📸 Analyse visuelle")
col1, col2 = st.columns(2)

with col1:
    st.image("IMG_0818.png", caption="Données et Influence")
    st.image("IMG_0820.png", caption="Le poids des algorithmes")

with col2:
    st.image("IMG_0819.png", caption="La captation de l'attention")
    st.image("IMG_0821.png", caption="Liberté numérique")

# --- INTERACTIF ---
st.divider()
if st.button("🔥 CLIQUER POUR TESTER VOTRE LIBERTÉ"):
    st.balloons()
    st.error("L'algorithme a détecté votre clic. Vous êtes sous influence !")
