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

# --- SECTION JEU AVEC SCORE ---
st.divider()
st.subheader("🎮 Le Défi du Hacker Cosmic")

# 1. Initialisation du score (on le crée s'il n'existe pas)
if 'score' not in st.session_state:
    st.session_state.score = 0

# 2. Affichage du score en haut du jeu
st.info(f"🏆 Ton Score : {st.session_state.score} points")

if 'cible' not in st.session_state:
    st.session_state.cible = 20.0

if st.button("🎲 Nouveau défi"):
    st.session_state.cible = float(random.randint(10, 80))
    st.session_state.gagne = False # On permet de gagner à nouveau

cible_actuelle = st.session_state.cible
st.write(f"🎯 **Ton défi :** Trouve la réduction pour arriver à **{cible_actuelle} €** !")

# 3. Vérification avec ajout de point
if prix_final == cible_actuelle:
    if not st.session_state.get('gagne', False):
        st.session_state.score += 1 # On ajoute 1 point !
        st.session_state.gagne = True # On marque que c'est gagné pour ce nombre
    
    st.balloons()
    st.snow()
    st.success(f"🏆 BRAVO ! +1 point ! Score : {st.session_state.score}")
st.divider()
st.subheader("📟 Mini-Calculatrice Rapide")

# On crée deux colonnes pour que ce soit joli
col_c1, col_c2 = st.columns(2)

with col_c1:
    operation = st.text_input("Tape ton calcul (ex: 12*4)", value="10+10")

with col_c2:
    try:
        # Cette fonction calcule le texte automatiquement !
        resultat_mini = eval(operation)
        st.metric("Résultat", resultat_mini)
    except:
        st.write("Format : 2*5")
st.divider()
st.subheader("🍴 Aide au Restaurant")

c1, c2 = st.columns(2)
with c1:
    note = st.number_input("Montant total (€)", min_value=0.0, value=50.0)
with c2:
    amis = st.number_input("Nombre de personnes", min_value=1, value=2)

pourcentage_tip = st.slider("Pourboire (%)", 0, 30, 10)
total_avec_tip = note * (1 + pourcentage_tip/100)

st.info(f"Chacun doit payer : **{total_avec_tip / amis:.2f} €**")


