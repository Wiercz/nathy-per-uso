import random
import streamlit as st

st.set_page_config(page_title="Nathy Per Uso 🔮", page_icon="🔮")

st.title("🔮 Nathy Per Uso")
st.write("Se precisares da Nathy, escreve: **Chama!**")

# ---------------- DATA ----------------

tempo = [
    "Hoje, papi...",
    "Num dia caliente...",
    "Ku ku kukuku... ahora!",
    "Em breve... si te gusta así...",
    "Cada vez que encontras uma mulher malportada...",
    "Na próxima viagem de caballo...",
    "Quando la Mami aparece..."
]

sujeitos = [
    "una businesswoman... ou una mafiosa",
    "una égua divina",
    "un escândalo internacional",
    "una argentina más próxima",
    "uma gaja misteriosa",
    "tua desconhecida hermana adoptada",
    "una persona que respeta las leyes de la salsa",
    "um fofoqueiro imprevisível",
    "aquela kleoparta negra",
    "el veneno em tua sangue",
    "una criatura linda, sem roupa",
    "una mirada de mil mujeres",
    "teu lado sin vergüenza",
    "un deseo de aprender secretos de salsa",
    "um inesperado vício que no te deja dormir, papi",
    "una creencia numa deusa",
    "un amor que mata y no perdona",
    "tua fragilidade a los besos",
    "un grupo organizado de los papis y mamis"
]

# -------- DESTINO CATEGORIES --------

emotional_destinos = [
    "tua paz nos dias de chuva",
    "o calor dos teus lábios",
    "o teu fogo interior",
    "tua fragilidade escondida",
    "o teu equilíbrio emocional caliente",
    "tu confiança exagerada",
    "o ritmo do teu coração selvagem",
    "a energia que te rodeia"
]

social_destinos = [
    "teu império de samba",
    "tu destino secreto",
    "a imagem da reina malportada",
    "o palco invisível da tua vida",
    "tu reputação secreta",
    "los olhos que te observan"
]

event_destinos = [
    "teu poder de mover-se como uma gazela",
    "os efeitos de exercícios proibidos de cardio",
    "a tua noite mais perigosa"
]

all_destinos = emotional_destinos + social_destinos + event_destinos

# -------- VERB CATEGORIES --------

transformative_verbs = [
    "transformará",
    "intensificará",
    "despertará",
    "aprofundará",
    "consumirá"
]

revelation_verbs = [
    "revelará",
    "iluminará",
    "anunciará",
    "marcará"
]

emotional_verbs = [
    "incendiará",
    "seduzirá",
    "provocará",
    "tocará",
    "trairá"
]

power_verbs = [
    "dominará",
    "manipulará",
    "confundirá",
    "desafiará",
    "esmagará",
    "ocultará"
]

# -------- AVISOS --------

avisos = [
    "Pero… cuídate. Hay más… pero no tan pronto.",
    "Ku ku kuku… algo se aproxima.",
    "Y lo más importante, cariño…",
    "Nem todos suportan tu brillo.",
    "Lo que parece dulce puede quemar.",
    "Alguém está observando em silêncio.",
    "El poder siempre cobra precio.",
    "Tu intensidade pode assustar até los fuertes.",
    "Hay pasos de samba prohibidos…",
    "Pero tu sabes bien...",
    "Y escucha bien…",
    "Y lo que siempre se murmura en los bares sospechosos…"
]

# -------- CONSELHOS --------

conselhos = [
    "Não confies em conselhos de um sordo.",
    "Ku ku kuku.",
    "Agrade a primeira samba do próximo mês.",
    "Evite os pratos veganos e não picantes.",
    "Devolve 50% do teu salário ao Miko.",
    "No pidas permiso.",
    "Por enquanto, não confies nem na tua sombra."
]

# -------------- LOGIC --------------

def escolher_verbo(destino):
    if destino in emotional_destinos:
        return random.choice(transformative_verbs + emotional_verbs)
    elif destino in social_destinos:
        return random.choice(revelation_verbs + power_verbs)
    elif destino in event_destinos:
        return random.choice(transformative_verbs + emotional_verbs + power_verbs)

def gerar_profecia() -> str:
    destino = random.choice(all_destinos)
    verbo = escolher_verbo(destino)

    return (
        f"{random.choice(tempo)}\n\n"
        f"{random.choice(sujeitos)} {verbo} {destino}.\n\n"
        f"{random.choice(avisos)}\n\n"
        f"{random.choice(conselhos)}"
    )

# -------------- UI --------------

entrada = st.text_input("Escreve aqui:", placeholder="Chama")

if st.button("Invocar 🔥"):
    if entrada.strip().lower() == "chama":
        st.success("🔮 Nathy Per Uso diz:")
        st.code(gerar_profecia(), language="text")
    else:
        st.warning("A Nathy não foi invocada. Escreve: **Chama**")
