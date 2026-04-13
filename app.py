import streamlit as st

# 1. Configuration de la page et style CSS personnalisé
st.set_page_config(page_title="Hacker Cosmic 1CA", layout="centered")

st.markdown("""
    <style>
    /* Fond sombre et police 'Hacker' */
    .stApp {
        background-color: #0e1117;
        color: #00ff41;
    }
    /* Style des titres */
    h1, h2, h3 {
        color: #00ff41 !important;
        font-family: 'Courier New', Courier, monospace;
        text-shadow: 2px 2px #000000;
    }
    /* Style du prix final */
    .price-text {
        font-size: 50px !important;
        font-weight: bold;
        color: #00ff41;
        text-align: center;
        border: 2px solid #00ff41;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 0 15px #00ff41;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Organisation en colonnes pour les entrées
st.title("🌌 Hacker Cosmic 1CA")
st.write("---")

col1, col2 = st.columns(2)

with col1:
    prix_origine = st.number_input("Prix d'origine (€)", min_value=0.0, value=100.0, step=1.0)

with col2:
    reduction = st.number_input("Réduction (%)", min_value=0.0, max_value=100.0, value=10.0, step=1.0)

# 3. Calcul et affichage stylisé
prix_final = prix_origine * (1 - reduction / 100)

st.write("### Prix après réduction")
st.markdown(f'<p class="price-text">{prix_final:.2f} €</p>', unsafe_allow_html=True)

# 4. Message de succès "Hacker"
st.success(f"Économie réalisée : {prix_origine - prix_final:.2f} €")

