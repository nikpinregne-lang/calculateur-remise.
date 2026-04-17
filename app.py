import streamlit as st
import random
import re

# 1. Configuration GOAT
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="wide")

# --- LISTE DES PAYS ---
tous_les_pays = sorted([
    "🇫🇷 France", "🇦🇫 Afghanistan", "🇿🇦 Afrique du Sud", "🇩🇿 Algérie", "🇩🇪 Allemagne", 
    "🇧🇪 Belgique", "🇨🇦 Canada", "🇲🇦 Maroc", "🇺🇸 USA" # (Garde ta liste complète ici)
])

# --- TRADUCTIONS (On utilise des codes simples) ---
trads = {
    "FR": {"titre": "Mon calculateur de réduction", "prix": "Prix d'origine (€)", "remise": "Remise (%)", "total": "Total :"},
    "EN": {"titre": "My Discount Calculator", "prix": "Original Price ($)", "remise": "Discount (%)", "total": "Total:"},
    "AR": {"titre": "حاسبة الخصم الخاصة بي", "prix": "السعر الأصلي", "remise": "خصم (%)", "total": "المجموع :"}
}

# --- CERVEAU IA GOAT ---
def cerveau_ia_goat(question):
    q = question.lower().strip()
    connaissances = {
        "canada": "Ottawa 🇨🇦", "france": "Paris 🇫🇷", "maroc": "Rabat 🇲🇦", 
        "qui": "Le seul patron ici, c'est le GOAT **Règne**. 👑"
    }
    for mot, rep in connaissances.items():
        if mot in q: return f"La réponse est **{rep}**."
    # ... (Le reste de ton cerveau IA reste identique)
    return f"Pour '{question}', c'est captivant ! 😉"

# --- INTERFACE ---
col_main, col_lang = st.columns([0.8, 0.2])

with col_lang:
    # ON FORCE LE FRANÇAIS PAR DÉFAUT ICI
    index_fr = 0
    try: index_fr = tous_les_pays.index("🇫🇷 France")
    except: pass
    
    pays = st.selectbox("🌐 Choisis ton pays", tous_les_pays, index=index_fr)

# --- LA LOGIQUE DE LANGUE (TRÈS SIMPLE) ---
# Par défaut, on est en Français
L = trads["FR"] 

# UNIQUEMENT si l'utilisateur change pour un pays spécifique, on change la langue
if "Afghanistan" in pays or "Algérie" in pays:
    L = trads["AR"]
elif "USA" in pays or "Canada" in pays or "Royaume-Uni" in pays:
    L = trads["EN"]

with st.sidebar:
    st.title("🤖 Chatbot 1CA")
    st.write(f"Assistant de **Règne**")
    # Le chatbot reste TOUJOURS en Français pour toi
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Wesh ! Demande-moi n'importe quoi."}]
    # ... (Reste du code chatbot)

with col_main:
    st.header(L["titre"]) # Utilise la langue choisie
    st.title("Hacker Cosmic 1CA 2026")
    st.subheader("Créé par **Règne**")
    
    # CALCULATEUR TRADUIT
    p = st.number_input(L["prix"], value=460.0)
    r = st.number_input(L["remise"], value=10.0)
    st.header(f"{L['total']} {p * (1 - r/100):.2f}")
