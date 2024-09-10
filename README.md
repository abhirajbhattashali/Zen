

---

# Zen Desktop Assistant

**Zen Desktop Assistant** is an AI-powered virtual assistant that leverages advanced natural language processing to interact with users in real-time. It listens to spoken commands, processes them asynchronously using **OlammaLLM** and **Langchain**, and responds with natural, human-like speech. For small tasks, Zen uses the **Gemma:2b** model for offline text-to-speech, specifically optimized for devices with only 8GB of RAM, such as the **Mac M1 (8GB)**.

## Features:
- **Speech Recognition**: Powered by Google Speech Recognition API.
- **NLP & Responses**: Generates intelligent responses using OlammaLLM and Langchain for efficient language model handling.
- **Text-to-Speech**: Converts text to speech via gTTS, with offline TTS using Gemma:2b for small tasks, ideal for low-RAM environments.
- **Asynchronous & Offline Support**: Optimized for faster, seamless conversation flow with offline task handling.

## Tech Stack:
- Python, gTTS, Google Speech Recognition, OlammaLLM, Langchain, Pydub, SimpleAudio, Gemma:2b

---
