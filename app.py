import streamlit as st
import random

st.set_page_config(page_title="Hacker Cosmic", page_icon="IMG_0956.png")

col1, col2 = st.columns([0.15, 0.85])



with col1:
    st.image("IMG_0956.png")

with col2:
        st.title("Mon calculateur de réduction")
        st.markdown("<p style='color: #00BFFF; font-size: 20px; font-weight: bold;'>Hacker Cosmic 1CA 2026</p>", unsafe_allow_html=True)
    st.components.v1.html("""
    <script>
        function parler() {
            var msg = new SpeechSynthesisUtterance("Bienvenue sur le site du Hacker Cosmic !");
            msg.lang = 'fr-FR';
            window.speechSynthesis.speak(msg);
        }
        window.onload = parler;
    </script>
    <button onclick="parler()" style="background-color: #00BFFF; color: white; border: none; padding: 10px; border-radius: 5px; cursor: pointer; font-weight: bold;">
        🔈 Bienvenue !
    </button>
    """, height=60)



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

# --- SECTION JEU AMÉLIORÉE (Remplace les lignes 53 à 82) ---
st.divider()
st.subheader("🎮 Le Défi du Hacker Cosmic")

if 'score' not in st.session_state:
    st.session_state.score = 0
if 'cible' not in st.session_state:
    st.session_state.cible = 20.0

col_jeu1, col_jeu2 = st.columns(2)

with col_jeu1:
    st.info(f"🏆 Score : {st.session_state.score}")
    if st.button("🎲 Nouveau défi"):
        st.session_state.cible = float(random.randint(10, 80))
        st.session_state.gagne = False

with col_jeu2:
    # Ce curseur ne sert que pour le jeu !
    p_jeu = st.slider("Ajuste pour gagner !", 0, 100, 10, key="slider_jeu")
    # On calcule le prix du jeu ici avec le nouveau curseur
    prix_jeu = prix_initial * (1 - p_jeu / 100)
    st.write(f"🎯 Cible : **{st.session_state.cible} €**")
    st.write(f"💵 Ton test : **{round(prix_jeu, 2)} €**")

# Vérification de la victoire
if round(prix_jeu, 2) == st.session_state.cible:
    if not st.session_state.get('gagne', False):
        st.session_state.score += 1
        st.session_state.gagne = True
    st.balloons()
    st.success("🏆 COMPTE EST BON !")

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
st.divider()
st.subheader("📐 Assistant de Géométrie")

forme = st.selectbox("Choisis une forme", ["Rectangle", "Triangle", "Cercle"])

if forme == "Rectangle":
    l = st.number_input("Longueur ($L$)", min_value=0.0, value=10.0)
    h = st.number_input("Largeur ($l$)", min_value=0.0, value=5.0)
    aire = l * h
    perimetre = 2 * (l + h)
    st.write(f"**Formule de l'aire :** $L \\times l$")
    st.success(f"Aire : **{aire}** | Périmètre : **{perimetre}**")

elif forme == "Triangle":
    b = st.number_input("Base ($b$)", min_value=0.0, value=10.0)
    h = st.number_input("Hauteur ($h$)", min_value=0.0, value=5.0)
    aire = (b * h) / 2
    st.write(f"**Formule :** $(b \\times h) / 2$")
    st.success(f"Aire du triangle : **{aire}**")

elif forme == "Cercle":
    r = st.number_input("Rayon ($r$)", min_value=0.0, value=5.0)
    aire = 3.14159 * (r ** 2)
    perimetre = 2 * 3.14159 * r
    st.write(f"**Formule :** $\pi \\times r^2$")
    st.success(f"Aire : **{aire:.2f}** | Périmètre : **{perimetre:.2f}**")


