import streamlit as st
import random
import re

# 1. Configuration de la page
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="wide")

# --- DICTIONNAIRE ÉLARGI DES PAYS ET LANGUES (Zéro village, que des nations) ---
languages = {
    "🇫🇷 France": {"t": "Calculateur 1CA", "p": "Prix d'origine", "r": "Réduction", "author": "Créé par Règne", "defi": "🎯 Défi Hacker"},
    "🇲🇦 Maroc": {"t": "حاسبة هكر كوزميك", "p": "السعر الأصلي", "r": "خصم", "author": "تم إنشاؤه بواسطة Règne", "defi": "🎯 تحدي الهكر"},
    "🇸🇦 Arabie Saoudite": {"t": "حاسبة هكر كوزميك", "p": "السعر الأصلي", "r": "خصم", "author": "تم إنشاؤه بواسطة Règne", "defi": "🎯 تحدي الهكر"},
    "🇹🇷 Türkiye": {"t": "Hacker Kozmik Hesaplayıcı", "p": "Orijinal Fiyat", "r": "İndirim", "author": "Règne tarafından oluşturuldu", "defi": "🎯 Hacker Meydan Okuması"},
    "🇷🇴 România": {"t": "Calculator Cosmic", "p": "Preț original", "r": "Reducere", "author": "Creat de Règne", "defi": "🎯 Provocarea Hackerului"},
    "🇺🇦 Україна": {"t": "Калькулятор Космік", "p": "Початкова ціна", "r": "Знижка", "author": "Створено Règne", "defi": "🎯 Виклик хакера"},
    "🇧🇪 Belgique": {"t": "Calculateur 1CA", "p": "Prix d'origine", "r": "Réduction", "author": "Créé par Règne", "defi": "🎯 Défi Hacker"},
    "🇨🇦 Canada": {"t": "Calculateur Cosmic", "p": "Prix / Price", "r": "Rabais / Discount", "author": "Créé par Règne", "defi": "🎯 Défi Hacker"},
    "🇺🇸 USA / UK": {"t": "Cosmic Calculator", "p": "Original Price", "r": "Discount", "author": "Created by Règne", "defi": "🎯 Hacker Challenge"},
    "🇪🇸 España": {"t": "Calculadora Cósmica", "p": "Precio original", "r": "Descuento", "author": "Creado por Règne", "defi": "🎯 Desafío Hacker"},
    "🇮🇹 Italia": {"t": "Calcolatrice Cosmica", "p": "Prezzo originale", "r": "Sconto", "author": "Creato da Règne", "defi": "🎯 Sfida Hacker"},
    "🇩🇪 Deutschland": {"t": "Hacker Rechner", "p": "Originalpreis", "r": "Rabatt", "author": "Erstellt von Règne", "defi": "🎯 Hacker-Herausforderung"},
    "🇵🇹 Portugal": {"t": "Calculadora Cósmica", "p": "Preço original", "r": "Desconto", "author": "Criado por Règne", "defi": "🎯 Desafio Hacker"},
    "🇩🇿 Algérie": {"t": "حاسبة الجزائر", "p": "السعر الأصلي", "r": "خصم", "author": "تم إنشاؤه بواسطة Règne", "defi": "🎯 تحدي الهكر"},
    "🇹🇳 Tunisie": {"t": "حاسبة تونس", "p": "السعر الأصلي", "r": "خصم", "author": "تم إنشاؤه بواسطة Règne", "defi": "🎯 تحدي الهكر"},
    "🇨🇭 Suisse": {"t": "Calculateur 1CA", "p": "Prix d'origine", "r": "Réduction", "author": "Créé par Règne", "defi": "🎯 Défi Hacker"}
}

# --- CERVEAU DU CHATBOT GOAT (SANS BLABLA) ---
def cerveau_ia_goat(question):
    q = question.lower().strip()
    
    # Capitales mondiales
    capitales = {
        "france": "Paris 🇫🇷", "belgique": "Bruxelles 🇧🇪", "maroc": "Rabat 🇲🇦", "arabie": "Riyad 🇸🇦",
        "turquie": "Ankara 🇹🇷", "ukraine": "Kyiv 🇺🇦", "roumanie": "Bucarest 🇷🇴", "italie": "Rome 🇮🇹",
        "espagne": "Madrid 🇪🇸", "algérie": "Alger 🇩🇿", "tunisie": "Tunis 🇹🇳", "suisse": "Berne 🇨🇭",
        "canada": "Ottawa 🇨🇦", "allemagne": "Berlin 🇩🇪", "portugal": "Lisbonne 🇵🇹"
    }

    if "qui" in q and "cree" in q: return "Le seul GOAT ici, c'est **Règne** ! 👑"
    if "goat" in q: return "Le patron, c'est **Règne**. Moi je suis juste son IA. 🐐"
    
    for pays, cap in capitales.items():
        if pays in q: return f"La capitale c'est {cap}."

    # Calculs directs
    if re.search(r'\d+', q) and any(op in q for op in ['+', '-', '*', '/']):
        try:
            res = eval("".join(re.findall(r'[0-9\+\-\*\/\.]', q)))
            return f"Ça fait **{res}**. Facile pour moi ! 😎"
        except: return "Calcul trop bizarre."

    if q in ["salut", "bonjour", "wesh", "merhaba"]: return "Salut ! Pose ta question, je réponds direct."
    if "ca va" in q or "ça va" in q: return "Tranquille, je pète la forme numérique ! Et toi ?"
    if "merci" in q: return "Normal ! 😉"
    
    return f"Je sais pas tout sur '{question}', mais demande à **Règne**, c'est lui le cerveau. 😉"

# --- INTERFACE ---
col_main, col_lang = st.columns([0.8, 0.2])

with col_lang:
    sel = st.selectbox("🌐 Pays / Langue", list(languages.keys()))
    T = languages[sel]

with st.sidebar:
    st.title("🤖 Chatbot 1CA")
    st.write("Assistant de **Règne**")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Wesh ! Pose ta question."}]
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    if prompt := st.chat_input("Écris-moi..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        rep = cerveau_ia_goat(prompt)
        with st.chat_message("assistant"): st.markdown(rep)
        st.session_state.messages.append({"role": "assistant", "content": rep})

with col_main:
    st.title(T["t"] + " 2026")
    st.subheader(T["author"])
    st.write("---")
    
    prix = st.number_input(T["p"], value=100.0)
    taux = st.number_input(T["r"], value=10.0)
    st.header(f"Total : {prix * (1 - taux/100):.2f} €")
    
    st.write("---")
    
    # LE DÉFI AVEC SCORE
    st.header(T["defi"])
    if 'score' not in st.session_state: st.session_state.score = 0
    if 'ex_p' not in st.session_state:
        st.session_state.ex_p, st.session_state.ex_r = random.randint(10, 500), random.randint(5, 50)
        st.session_state.sol = st.session_state.ex_p * (1 - st.session_state.ex_r / 100)

    st.write(f"**Score actuel : {st.session_state.score} ⭐**")
    st.write(f"Prix : {st.session_state.ex_p}€ | Remise : {st.session_state.ex_r}%")
    ans = st.number_input("Ta réponse :", key="ans")
    
    if st.button("Vérifier"):
        if abs(ans - st.session_state.sol) < 0.1:
            st.success("✅ GAGNÉ !")
            st.session_state.score += 1
            del st.session_state['ex_p']
            st.rerun()
        else:
            st.error(f"❌ FAUX ! C'était {st.session_state.sol:.2f}€")
            st.session_state.score = 0
# --- COMPTEUR DE VISITES (GOAT STYLE) ---
if 'count' not in st.session_state:
    st.session_state.count = 10 # On commence à 10 comme sur tes stats !
else:
    st.session_state.count += 1

st.write("---")
st.write(f"🔥 **{st.session_state.count} Hackers** ont visité ce site !")
