import streamlit as st
import random

st.set_page_config(page_title="Hacker Cosmic", page_icon="IMG_0956.png")

col1, col2 = st.columns([0.15, 0.85])



with col1:
    st.image("IMG_0956.png")

with col2:
        st.title("Mon calculateur de réduction")
        st.markdown("<p style='color: #00BFFF; font-size: 20px; font-weight: bold;'>Hacker Cosmic 1CA 2026</p>", unsafe_allow_html=True)



# Saisie des valeurs
col_gauche, col_droite = st.columns(2)

with col_gauche:
    prix_initial = st.number_input("Prix d'origine (€)", min_value=0.0, value=100.0)

with col_droite:
    pourcentage = st.slider("Choisis ta réduction (%)", 0, 100, 10, key="valeur_remise")        






# Calculs
remise = (prix_initial * pourcentage) / 100
prix_final = prix_initial - remise

# Affichage
st.divider()
# Affichage stylé
st.metric(
    label="✅ Prix après réduction", 
    value=f"{prix_final} €", 
    delta=f"-{remise} €", 
    delta_color="inverse"
)
if pourcentage >= 50:
    st.warning("🔥 C'est une affaire de dingue !")
elif pourcentage > 0:
    st.success("💰 Super économie !")

st.balloons()

st.divider()
st.subheader("🎮 Exercice : Le Juste Prix")

# L'ordinateur choisit un nombre s'il n'y en a pas encore
if 'cible' not in st.session_state:
    st.session_state.cible = 20.0

# Bouton pour changer d'exercice
if st.button("🎲 Nouveau défi"):
    st.session_state.cible = float(random.randint(10, 80))

cible_actuelle = st.session_state.cible
st.write(f"🎯 **Ton défi :** Trouve la réduction pour arriver à **{cible_actuelle} €** !")

# Vérification pour gagner
if prix_final == cible_actuelle:
    st.balloons()
    st.snow()
    st.success(f"🏆 BRAVO ! Tu as trouvé {cible_actuelle} € !")

