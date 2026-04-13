import streamlit as st
import random

# 1. Configuration de la page
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="wide")

# --- DICTIONNAIRE DE TOUTES LES LANGUES ---
languages = {
    "Français": {
        "title": "Calculateur Hacker Cosmic", "author": "Créé par Règne",
        "price": "Prix d'origine (€)", "promo": "Réduction (%)",
        "total": "Total après réduction", "exo": "📝 Exercice Infini",
        "check": "Vérifier", "new": "Nouvel exercice 🔄",
        "bot_hi": "Salut ! Je suis l'IA de Règne. Pose-moi n'importe quelle question !"
    },
    "English": {
        "title": "Hacker Cosmic Calculator", "author": "Created by Règne",
        "price": "Original Price (€)", "promo": "Discount (%)",
        "total": "Total after discount", "exo": "📝 Infinite Exercise",
        "check": "Check", "new": "New Exercise 🔄",
        "bot_hi": "Hi! I am the AI of Règne. Ask me any question!"
    },
    "Español": {
        "title": "Calculadora Hacker Cosmic", "author": "Creado por Règne",
        "price": "Precio original (€)", "promo": "Descuento (%)",
        "total": "Total con descuento", "exo": "📝 Ejercicio Infinito",
        "check": "Verificar", "new": "Nuevo ejercicio 🔄",
        "bot_hi": "¡Hola! Soy la IA de Règne. ¡Hazme n'importe quelle pregunta!"
    },
    "Deutsch": {
        "title": "Hacker Cosmic Rechner", "author": "Erstellt von Règne",
        "price": "Originalpreis (€)", "promo": "Rabatt (%)",
        "total": "Gesamt nach Rabatt", "exo": "📝 Unendliche Übung",
        "check": "Prüfen", "new": "Neue Übung 🔄",
        "bot_hi": "Hallo! Ich bin die KI von Règne. Frag mich was du willst!"
    },
    "Italiano": {
        "title": "Calcolatrice Hacker Cosmic", "author": "Creato da Règne",
        "price": "Prezzo originale (€)", "promo": "Sconto (%)",
        "total": "Totale scontato", "exo": "📝 Esercizio Infinito",
        "check": "Verifica", "new": "Nuovo esercizio 🔄",
        "bot_hi": "Ciao! Sono l'IA di Règne. Chiedimi qualsiasi cosa!"
    },
    "العربية": {
        "title": "حاسبة هكر كوزميك", "author": "تم إنشاؤه بواسطة Règne",
        "price": "السعر الأصلي (€)", "promo": "خصم (%)",
        "total": "المجموع بعد الخصم", "exo": "📝 تمرين لا نهائي",
        "check": "تحقق", "new": "تمرين جديد 🔄",
        "bot_hi": "أهلاً! أنا ذكاء Règne الاصطناعي. اسألني أي شيء!"
    }
}

# --- BARRE LATÉRALE : CHATBOT ---
with st.sidebar:
    st.title("🤖 Chatbot 1CA")
    st.write("Assistant officiel de **Règne**")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])

    if prompt := st.chat_input("Dis-moi n'importe quoi..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        
        # Logique de réponse "Intelligente"
        p = prompt.lower()
        if "bonbon" in p:
            reponse = "Un bonbon est une sucrerie délicieuse. Règne adore ça ! 🍬"
        elif "qui" in p and "cree" in p:
            reponse = "C'est le grand **Règne** qui a tout créé ! 👑"
        else:
            reponse = f"'{prompt}' ? C'est fascinant ! En tant qu'IA de Règne, je vais y réfléchir."

        with st.chat_message("assistant"): st.markdown(reponse)
        st.session_state.messages.append({"role": "assistant", "content": reponse})

# --- CORPS PRINCIPAL ---
# On crée deux colonnes : une large pour le contenu, une petite à droite pour la langue
col_main, col_lang = st.columns([0.8, 0.2])

with col_lang:
    selected_lang = st.selectbox("🌐 Langue", list(languages.keys()))
    T = languages[selected_lang]

with col_main:
    # Votre logo IMG_0956.png
    try:
        st.image("IMG_0956.png", width=200)
    except:
        st.info("Logo Hacker Cosmic")

    st.title(f"{T['title']} 1CA 2026")
    st.markdown(f"### {T['author']}")
    st.write("---")

    # Calculateur
    prix_orig = st.number_input(T["price"], min_value=0.0, value=100.0)
    reduction = st.number_input(T["promo"], min_value=0.0, max_value=100.0, value=10.0)
    
    st.header(f"{T['total']} : {prix_orig * (1 - reduction / 100):.2f} €")

    st.write("---")

    # Exercice Infini
    st.header(T["exo"])
    if 'exo_prix' not in st.session_state:
        st.session_state.exo_prix = random.randint(10, 500)
        st.session_state.exo_remise = random.randint(5, 75)
        st.session_state.sol = st.session_state.exo_prix * (1 - st.session_state.exo_remise / 100)

    st.write(f"**Défi :** {st.session_state.exo_prix} € avec {st.session_state.exo_remise} % de remise.")
    user_ans = st.number_input("Réponse (€) :", key="ans_input")

    c1, c2 = st.columns(2)
    with c1:
        if st.button(T["check"]):
            if abs(user_ans - st.session_state.sol) < 0.05:
                st.success("✅ Bravo !")
            else:
                st.error(f"❌ La réponse était {st.session_state.sol:.2f} €")
    with c2:
        if st.button(T["new"]):
            del st.session_state['exo_prix']
            st.rerun()
