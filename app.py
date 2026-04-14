import streamlit as st
import random
import re

# 1. CONFIGURATION ET STYLE GOAT
st.set_page_config(page_title="Hacker Cosmic 1CA 2026", layout="wide")

# --- DICTIONNAIRE DE TRADUCTION INTÉGRAL ---
# Ici, on lie chaque pays à sa langue pour que TOUT change sur le site
LANGS = {
    "Français": {"calc": "Mon calculateur de réduction", "orig": "Prix d'origine (€)", "rem": "Remise (%)", "defi": "🎯 Défi du Hacker", "check": "Vérifier", "score": "Score", "win": "✅ GAGNÉ !", "lost": "❌ FAUX !", "visit": "Hackers ont visité !"},
    "English": {"calc": "My Discount Calculator", "orig": "Original Price (€)", "rem": "Discount (%)", "defi": "🎯 Hacker Challenge", "check": "Check", "score": "Score", "win": "✅ WON!", "lost": "❌ WRONG!", "visit": "Hackers visited!"},
    "Maroc (Arabe)": {"calc": "حاسبة الخصم الخاصة بي", "orig": "السعر الأصلي", "rem": "خصم (%)", "defi": "🎯 تحدي الهكر", "check": "تحقق", "score": "نتيجة", "win": "✅ فزت!", "lost": "❌ خطأ!", "visit": "هكر زاروا الموقع"},
    "Română": {"calc": "Calculatorul de reduceri", "orig": "Preț original", "rem": "Reducere", "defi": "🎯 Provocarea Hackerului", "check": "Verifică", "score": "Scor", "win": "✅ CÂȘTIGAT!", "lost": "❌ GREȘIT!", "visit": "Hackeri au vizitat!"},
    "Türkçe": {"calc": "İndirim Hesaplayıcı", "orig": "Orijinal Fiyat", "rem": "İndirim", "defi": "🎯 Hacker Meydan Okuması", "check": "Kontrol Et", "score": "Puan", "win": "✅ KAZANDIN!", "lost": "❌ YANLIŞ!", "visit": "Hacker ziyaret etti!"},
    "Українська": {"calc": "Калькулятор знижок", "orig": "Початкова ціна", "rem": "Знижка", "defi": "🎯 Виклик хакера", "check": "Перевірити", "score": "Рахунок", "win": "✅ ПЕРЕМОГА!", "lost": "❌ ПОМИЛКА!", "visit": "Хакери відвідали!"}
}

# --- LISTE DES PAYS DU MONDE (TOP 50+) ---
PAYS_LISTE = [
    "🇫🇷 Français", "🇲🇦 Maroc (Arabe)", "🇺🇸 English (USA)", "🇷🇴 Română", "🇹🇷 Türkçe", "🇺🇦 Українська", 
    "🇩🇿 Algérie", "🇹🇳 Tunisie", "🇸🇦 Arabie Saoudite", "🇧🇪 Belgique", "🇨🇦 Canada", "🇨🇭 Suisse", 
    "🇮🇹 Italia", "🇪🇸 España", "🇵🇹 Portugal", "🇩🇪 Deutschland", "🇧🇷 Brasil", "🇯🇵 Japan", 
    "🇨🇳 China", "🇷🇺 Russia", "🇮🇳 India", "🇲🇽 México", "🇦🇺 Australia", "🇰🇷 South Korea"
]

# --- CERVEAU IA ILLIMITÉ (RÉPOND À TOUT COMME UN HUMAIN) ---
def cerveau_ia_goat(question):
    q = question.lower().strip()
    
    # 1. Réponse au point "." ou vide
    if q == "." or q == "": return "Un point ? C'est le début d'un grand code ! Pose-moi une vraie question. 😎"
    
    # 2. Salutations de Hacker (Wesh, Sava...)
    if any(s in q for s in ["wesh", "wsh", "bien ou quoi"]): return "Wesh ! Bien ou quoi ? Je suis l'IA de **Règne**, on gère le game ensemble. 🤝"
    if any(s in q for s in ["salut", "bonjour", "hello"]): return "Salut ! Prêt à calculer des promos avec le GOAT ? 😊"
    if "ça va" in q or "sava" in q: return "Tranquille, je pète la forme numérique ! Et toi, prêt à hacker les maths ? 🚀"

    # 3. Logique Mathématique (ex: 1+1, 15*3)
    if re.search(r'\d+', q) and any(op in q for op in ['+', '-', '*', '/']):
        try:
            calcul = "".join(re.findall(r'[0-9\+\-\*\/\.]', q))
            return f"Calcul rapide : **{calcul} = {eval(calcul)}**. Trop facile pour moi ! 🧠"
        except: pass

    # 4. Culture Générale (Capitales, Définitions)
    if "bonbon" in q: return "Un bonbon est une sucrerie délicieuse, mais attention à tes dents de hacker ! 🍬"
    if "qui" in q and "cree" in q: return "Le seul et unique patron ici, c'est **Règne**. 👑"
    if "australie" in q: return "La capitale c'est **Canberra** 🇦🇺 !"
    if "belgique" in q: return "La capitale c'est **Bruxelles** 🇧🇪 !"

    # 5. Réponse Libre (Discute de tout)
    return f"Franchement, ta question sur '{question}' est super stylée. En tant qu'IA, je trouve ça fascinant. Dis-m'en plus ! 😉"

# --- INTERFACE (SIDEBAR ET MAIN) ---
# Menu des pays à droite
col_main, col_lang = st.columns([0.8, 0.2])

with col_lang:
    choix = st.selectbox("🌐 Pays / Language", PAYS_LISTE)
    # On détecte la langue selon le choix pour traduire le site
    langue_cle = "English" # Par défaut
    for key in LANGS.keys():
        if key in choix: langue_cle = key
    T = LANGS[langue_cle]

with st.sidebar:
    st.title("🤖 Chatbot 1CA")
    st.write(f"Assistant du GOAT : **Règne**")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Wesh ! Je suis ton IA illimitée. Pose-moi n'importe quoi !"}]
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
    if prompt := st.chat_input("Demande-moi n'importe quoi..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        rep = cerveau_ia_goat(prompt)
        with st.chat_message("assistant"): st.markdown(rep)
        st.session_state.messages.append({"role": "assistant", "content": rep})

with col_main:
    # 2. LOGO ET TITRES
    try: st.image("IMG_0956.png", width=120)
    except: st.info("Logo Hacker Cosmic")
    
    st.header(T["calc"])
    st.title("Hacker Cosmic 1CA 2026")
    st.markdown("### Créé par **Règne**")
    st.write("---")

    # 3. LE CALCULATEUR
    p_orig = st.number_input(T["orig"], value=460.0)
    remise = st.number_input(T["rem"], value=10.0)
    st.header(f"Total : {p_orig * (1 - remise/100):.2f} €")
    
    st.write("---")

    # 4. LE DÉFI (EXERCICE AVEC SCORE)
    st.header(T["defi"])
    if 'score' not in st.session_state: st.session_state.score = 0
    if 'ex_p' not in st.session_state:
        st.session_state.ex_p = random.randint(10, 500)
        st.session_state.ex_r = random.randint(5, 50)
        st.session_state.sol = st.session_state.ex_p * (1 - st.session_state.ex_r / 100)

    st.write(f"**{T['score']} : {st.session_state.score} ⭐**")
    st.write(f"Trouve le prix final : **{st.session_state.ex_p}€** avec **{st.session_state.ex_r}%** de remise.")
    ans = st.number_input(T["check"], key="ans_input", value=0.0)
    
    c1, c2 = st.columns(2)
    with c1:
        if st.button(T["check"]):
            if abs(ans - st.session_state.sol) < 0.1:
                st.success(T["win"])
                st.session_state.score += 1
                del st.session_state['ex_p']
                st.rerun()
            else:
                st.error(f"{T['lost']} (Réponse: {st.session_state.sol:.2f}€)")
                st.session_state.score = 0
    with c2:
        if st.button("🔄"):
            del st.session_state['ex_p']
            st.rerun()

    # 5. COMPTEUR DE VISITES
    if 'v' not in st.session_state: st.session_state.v = 14
    st.session_state.v += 1
    st.write(f"🔥 **{st.session_state.v} {T['visit']}**")
