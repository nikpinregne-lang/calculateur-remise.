import streamlit as st

# 1. Configuration de la page (onglet du navigateur)
st.set_page_config(page_title="Calculateur Hacker Cosmic", page_icon="💰")

# 2. En-tête : Logo et Titre
col1, col2 = st.columns([1, 3]) # On crée deux colonnes pour aligner le logo et le titre

with col1:
    st.image("IMG_0956.png", width=150) # Ton logo de Hacker

with col2:
    st.title("Mon calculateur de réduction Hacker Cosmic 1CA")
    st.write("Créé par **RÈGNE**")

st.write("---") # Une ligne de séparation

# 3. Les entrées de chiffres
prix_initial = st.number_input("Prix d'origine (€)", min_value=0.0, value=100.0, step=1.0)
pourcentage = st.number_input("Réduction (%)", min_value=0.0, max_value=100.0, value=10.0, step=1.0)

# 4. Les calculs magiques
montant_remise = (prix_initial * pourcentage) / 100
prix_final = prix_initial - montant_remise

st.write("---")

# 5. Affichage du résultat (Le plus important pour les parents)
st.subheader("Prix après réduction")
st.metric(label="", value=f"{prix_final} €", delta=f"-{montant_remise} €", delta_color="inverse")

# 6. Le détail pour le prof de math (et pour bien comprendre)
with st.expander("👁️ Voir le détail du calcul"):
    st.info(f"Raisonnement : {prix_initial} € - ({prix_initial} € . {pourcentage}/100) = {prix_final} €")

# 7. Signature en bas
st.caption("🚀 Hacker Cosmic 1CA 2026 | Mode Haute Lisibilité")
