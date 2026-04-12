import streamlit as st
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


