Tutor Académico de Inglés con IA (RAG)
Descripción del Proyecto

Este proyecto consiste en el desarrollo de un asistente experto basado en inteligencia artificial que funciona como un Tutor Académico de Inglés.

El sistema permite ayudar a estudiantes en el aprendizaje del idioma inglés mediante:

explicación de gramática
enseñanza de vocabulario
corrección de oraciones
traducción de frases

El asistente utiliza técnicas de:

Prompt Engineering
Few-Shot Prompting
RAG (Retrieval Augmented Generation)

y funciona de manera local utilizando Python.

Objetivo

Desarrollar un tutor académico inteligente capaz de:

responder preguntas sobre inglés
explicar conceptos de forma clara
corregir errores en oraciones
proporcionar ejemplos prácticos
restringir respuestas fuera del contexto educativo
Tecnologías Utilizadas
Python
API de Gemini
Visual Studio Code
GitHub
LangChain
FAISS
Sentence Transformers
Arquitectura del Sistema

El sistema está compuesto por varios componentes clave:

🔹 1. System Prompt

Define el comportamiento del asistente como un Tutor Académico de Inglés.

Incluye:

instrucciones claras
funciones del tutor
reglas de comportamiento

Ejemplo de regla:

"Lo siento, soy tu tutor de inglés. Sigamos aprendiendo."

🔹 2. Few-Shot Prompting

Se incluyen ejemplos dentro del prompt para guiar al modelo.

Formato de respuesta esperado:

Explicación
Ejemplo
Traducción

Esto permite mantener consistencia en las respuestas.

🔹 3. Delimitadores

Se utilizan triple comillas (""") para separar:

instrucciones del sistema
contexto de conocimiento

Esto mejora la comprensión del modelo.

4. Implementación de RAG (Avance 2)

En esta fase se implementó un sistema RAG dinámico, que permite recuperar información relevante antes de generar una respuesta.

🔄 Flujo del sistema RAG

El sistema funciona de la siguiente manera:

Se carga el archivo conocimiento.txt
El texto se divide en fragmentos (chunks)
Cada fragmento se convierte en un vector (embedding)
Los vectores se almacenan en una base vectorial (FAISS)
El usuario realiza una pregunta
El sistema busca los fragmentos más relevantes
Se construye un contexto dinámico
El contexto se envía al modelo
El modelo genera la respuesta
Chunking (división del texto)

El documento se divide en fragmentos para mejorar la búsqueda:

CharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

Esto permite trabajar con partes más pequeñas del conocimiento.

Embeddings

Cada fragmento se convierte en un vector numérico usando:

sentence-transformers/all-MiniLM-L6-v2

Esto permite realizar búsqueda semántica (por significado, no por palabras exactas).

Base Vectorial (FAISS)

Los embeddings se almacenan en una base vectorial:

FAISS.from_documents(docs, embeddings)

Esto permite encontrar rápidamente los fragmentos más relevantes.

Búsqueda Semántica

Cuando el usuario hace una pregunta:

similarity_search(pregunta, k=2)

El sistema recupera los fragmentos más relacionados.

 Integración con el modelo

El contexto recuperado se inserta en el prompt:

contexto = obtener_contexto(pregunta)

Esto permite que el modelo responda usando información específica.

 Funcionalidades

El asistente puede:

explicar gramática
enseñar vocabulario
traducir frases
corregir oraciones
dar ejemplos
usar contexto dinámico (RAG)
mantener historial de conversación
 Ejecución del sistema

El sistema se ejecuta desde la terminal:

python Proyecto.py

Ejemplo:

Estudiante: what is the verb to be

Tutor:
Explicación:
...
 Historial de conversación

La conversación finaliza cuando el usuario escribe:

salir

Al finalizar, se muestra el historial completo de la interacción.

 Resultados

El uso de RAG permite:

respuestas más precisas
uso de conocimiento específico
mejor comprensión del contexto
 Conclusión

El proyecto demuestra cómo integrar técnicas de:

Prompt Engineering
Few-Shot Prompting
RAG

para construir un asistente académico inteligente.

El uso de una base vectorial permite mejorar significativamente la calidad de las respuestas, al proporcionar contexto relevante al modelo.