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
    "Numa próxima viagem de caballo...",
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

verbos = [
    "despertará",
    "confundirá",
    "revelará",
    "ocultará",
    "transformará",
    "dominará",
    "incendiará",
    "organizará",
    "anunciará",
    "marcará",
    "iluminará",
    "trairá",
    "aprofundará",
    "tocará",
    "desafiará",
    "seduzirá",
    "esmagará",
    "manipulará",
    "provocará",
    "intensificará",
    "consumirá"
]

destinos = [
    "teu império de samba",
    "tu destino secreto",
    "tua paz nos dias de chuva",
    "teu poder de mover-se como uma gazela",
    "o calor dos teus lábios",
    "a imagem da reina malportada",
    "os efeitos de exercícios proibidos de cardio",
    "o palco invisível da tua vida",
    "tu reputação secreta",
    "o teu fogo interior",
    "los olhos que te observan",
    "tua fragilidade escondida",
    "o teu equilíbrio emocional caliente",
    "a tua noite mais perigosa",
    "tu confiança exagerada",
    "o ritmo do teu coração selvagem",
    "a energia que te rodeia"
]

avisos = [
    "Pero… cuídate. Hay más… pero no tan pronto.",
    "Ku ku kuku… algo se aproxima.",
    "Y lo más importante, cariño…",
    "Nem todos suportan tu brillo.",
    "Lo que parece dulce puede quemar.",
    "Alguém está observando em silêncio.",
    "El poder siempre cobra precio.",
    "Tu intensidade pode assustar até los fuertes."
]

conselhos = [
    "Não confies em conselhos de um sordo.",
    "Ku ku kuku.",
    "Agrade a primeira samba do próximo mês.",
    "Evite os pratos veganos e não picantes.",
    "Devolve 50% do teu salário ao Miko.",
    "No pidas permiso."
]

# -------------- LOGIC --------------

def gerar_profecia() -> str:
    return (
        f"{random.choice(tempo)}\n\n"
        f"{random.choice(sujeitos)} {random.choice(verbos)} {random.choice(destinos)}.\n\n"
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