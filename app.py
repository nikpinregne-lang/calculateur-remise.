
import streamlit as st
import random

# 1. Configuration
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="wide")

# --- DICTIONNAIRE MULTILINGUE ---
languages = {
    "Français": {"title": "Calculateur", "price": "Prix d'origine", "promo": "Réduction", "check": "Vérifier", "new": "Nouveau", "author": "Créé par IEEM"},
    "English": {"title": "Calculator", "price": "Original Price", "promo": "Discount", "check": "Check", "new": "New", "author": "Created by IEEM"},
    "Español": {"title": "Calculadora", "price": "Precio original", "promo": "Descuento", "check": "Verificar", "new": "Nuevo", "author": "Creado por IEEM"},
    "Deutsch": {"title": "Rechner", "price": "Originalpreis", "promo": "Rabatt", "check": "Prüfen", "new": "Neu", "author": "Erstellt von IEEM"},
    "Italiano": {"title": "Calcolatrice", "price": "Prezzo originale", "promo": "Sconto", "check": "Verifica", "new": "Nuovo", "author": "Creato da IEEM"},
    "Português": {"title": "Calculadora", "price": "Preço original", "promo": "Desconto", "check": "Verificar", "new": "Novo", "author": "Criado por IEEM"},
    "العربية": {"title": "حاسبة", "price": "السعر الأصلي", "promo": "خصم", "check": "تحقق", "new": "جديد", "author": "تم إنشاؤه بواسطة IEEM"}
}

# --- BARRE LATÉRALE GAUCHE : CHATBOT ---
with st.sidebar:
    st.title("🤖 Chatbot 1CA")
    if "messages" not in st.session_state: st.session_state.messages = []
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    
    if prompt := st.chat_input("Pose-moi une question..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        resp = f"Assistant IEEM: {prompt}"
        with st.chat_message("assistant"): st.markdown(resp)
        st.session_state.messages.append({"role": "assistant", "content": resp})

# --- CORPS PRINCIPAL ---
# On crée deux colonnes : une large pour le contenu, une petite à droite pour la langue
col_main, col_lang = st.columns([0.8, 0.2])

with col_lang:
    selected_lang = st.selectbox("🌐 Language", list(languages.keys()))
    T = languages[selected_lang]

with col_main:
    try:
        st.image("IMG_0956.png", width=200)
    except:
        st.info("Logo IMG_0956.png")

    st.title(f"{T['title']} Hacker Cosmic 1CA 2026")
    st.write(T["author"])
    st.write("---")

    prix_origine = st.number_input(f"{T['price']} (€)", min_value=0.0, value=100.0)
    reduction = st.number_input(f"{T['promo']} (%)", min_value=0.0, max_value=100.0, value=10.0)

    st.header("Total")
    st.subheader(f"{prix_origine * (1 - reduction / 100):.2f} €")

    st.write("---")

    # --- EXERCICE INFINI ---
    st.header("📝 Exercice")
    if 'exo_prix' not in st.session_state:
        st.session_state.exo_prix = random.randint(10, 500)
        st.session_state.exo_remise = random.randint(5, 75)
        st.session_state.sol = st.session_state.exo_prix * (1 - st.session_state.exo_remise / 100)

    st.write(f"Prix: **{st.session_state.exo_prix} €** | Remise: **{st.session_state.exo_remise} %**")
    user_ans = st.number_input("Réponse :", key="ans")

    c1, c2 = st.columns(2)
    with c1:
        if st.button(T["check"]):
            if abs(user_ans - st.session_state.sol) < 0.05: st.success("✅")
            else: st.error("❌")
    with c2:
        if st.button(T["new"]):
            del st.session_state['exo_prix']
            st.rerun()
