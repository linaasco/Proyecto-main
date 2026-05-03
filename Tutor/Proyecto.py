import os
from google import genai
from dotenv import load_dotenv
from prompts import system_prompt, few_shot_examples
from rag import obtener_contexto

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

# historial de conversación
historial = []

while True:

    pregunta = input("\nEstudiante: ")

    if pregunta.lower() == "salir":
        break

    # 🔥 Obtener contexto desde RAG
    contexto = obtener_contexto(pregunta)

    # 🔥 Crear prompt dinámico
    prompt_final = system_prompt.format(contexto=contexto) + few_shot_examples

    # 🔥 Generar respuesta
    respuesta = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt_final + "\nPregunta: " + pregunta
    )

    texto_respuesta = respuesta.text

    print("\nTutor:", texto_respuesta)

    # guardar en historial
    historial.append({
        "pregunta": pregunta,
        "respuesta": texto_respuesta
    })

# mostrar historial
print("\n===== HISTORIAL DE LA CONVERSACIÓN =====\n")

for i, conversacion in enumerate(historial, start=1):
    print(f"Interacción {i}")
    print("Estudiante:", conversacion["pregunta"])
    print("Tutor:", conversacion["respuesta"])
    print("----------------------------------")