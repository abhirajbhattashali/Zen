---

# Zen Desktop Assistant

Zen Desktop Assistant is an AI-powered virtual assistant that uses advanced natural language processing to interact with users in real-time. It listens to spoken commands, processes them asynchronously using **OlammaLLM** and **Langchain**, and responds with natural, human-like speech. Zen is optimized for low-end devices, utilizing the **Gemma:2b** model for offline text-to-speech on devices with 8GB of RAM, such as the **Mac M1 (8GB)**.

## Features:
- **Speech Recognition**: Uses Google Speech Recognition API for accurate voice command detection.
- **NLP & Responses**: Generates intelligent responses using OlammaLLM and Langchain for efficient natural language processing.
- **Text-to-Speech**: Converts text to speech with gTTS and uses Gemma:2b for offline TTS, optimized for low-RAM environments.
- **Code Processing**: Identifies programming languages, extracts file extensions, formats code, creates temporary source code files, and opens them in VSCode using AppleScript for seamless switching between terminal and editor.
- **Asynchronous & Offline Support**: Optimized for a smooth, real-time conversation flow with support for offline task handling.

## Tech Stack:
- **Programming Languages**: Python
- **Libraries & APIs**: gTTS, Google Speech Recognition, OlammaLLM, Langchain, Pydub, SimpleAudio
- **Models**: Gemma:2b
- **Tools**: AppleScript, VSCode

## Future Enhancements:
- **Terminal Code Execution**: Integration of terminal code execution via Python and AppleScript.

---
