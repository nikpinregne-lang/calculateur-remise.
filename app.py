import streamlit as st
st.set_page_config(page_title="Hacker Cosmic", page_icon="IMG_0956.png")

col1, col2 = st.columns([0.15, 0.85])



with col1:
    st.image("IMG_0956.png")

with col2:
        st.title("Mon calculateur de réduction")
        st.subheader("Hacker Cosmic 1CA 2026")


# Saisie des valeurs
prix_initial = st.number_input("Prix d'origine (€)", min_value=0.0, value=100.0)
pourcentage = st.number_input("Réduction (%)", min_value=0.0, max_value=100.0, value=10.0)

# Calculs
remise = (prix_initial * pourcentage) / 100
prix_final = prix_initial - remise

# Affichage
st.divider()
st.metric(label="Prix après réduction", value=f"{prix_final} €", delta=f"-{remise} €")
