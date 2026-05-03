# Tutor Académico de Inglés con IA (RAG)

## Descripción del Proyecto

Este proyecto consiste en el desarrollo de un **asistente experto basado en inteligencia artificial** que funciona como un **Tutor Académico de Inglés**.

El sistema está diseñado para responder preguntas relacionadas con el aprendizaje del idioma inglés, como:

- gramática
- vocabulario
- corrección de oraciones
- traducción de frases

El asistente utiliza técnicas de **Prompt Engineering**, **Few-Shot Prompting** y **RAG (Retrieval Augmented Generation)** para generar respuestas educativas.

Además, el sistema funciona de manera local utilizando Python.

---

# Objetivo

Crear un tutor académico inteligente que pueda:

- responder preguntas de inglés
- explicar conceptos de gramática
- corregir frases
- proporcionar ejemplos
- rechazar preguntas fuera del contexto educativo

---

# Tecnologías Utilizadas

- Python
- API de Gemini
- Visual Studio Code
- GitHub
- Prompt Engineering

---

# Arquitectura del Sistema

El sistema está compuesto por tres partes principales:

### 1. System Prompt

Define el comportamiento del asistente.

El modelo se configura como un **Tutor Académico de Inglés** que:

- explica conceptos
- da ejemplos
- traduce frases
- corrige errores

También se establecen reglas para evitar responder preguntas fuera del tema.

Ejemplo:

> "Lo siento, soy tu tutor de inglés. Sigamos aprendiendo."
---

### 2. Few-Shot Prompting

Se incluyen ejemplos dentro del prompt para enseñarle al modelo **cómo debe responder**.

Ejemplo:

Pregunta:

Respuesta esperada:

- Explicación
- Ejemplo
- Traducción

Esto ayuda al modelo a mantener un formato consistente en las respuestas.

---

### 3. Delimitadores

Se utilizan **triple comillas (`"""`)** para separar el contexto del conocimiento de las instrucciones del sistema.

Esto ayuda a que el modelo entienda claramente qué parte corresponde al contexto educativo.

---

### 4. RAG (Retrieval Augmented Generation)

El sistema utiliza un archivo de conocimiento (`conocimiento.txt`) que contiene información sobre inglés.

Este contenido se incluye dentro del prompt para que el modelo pueda utilizarlo al generar respuestas.

Esto permite que el tutor responda basándose en un **material específico de estudio**.

---

# Funcionalidades

El asistente puede:

- explicar gramática
- enseñar vocabulario
- traducir frases
- corregir oraciones
- dar ejemplos
- mantener un historial de conversación

La conversación termina cuando el estudiante escribe:
salir

En ese momento se muestra el **historial completo de la conversación**.


