import speech_recognition as sr
from gtts import gTTS
import os
from fetchLLM import OlammaLLM
from pydub import AudioSegment
import asyncio
import simpleaudio as sa


r = sr.Recognizer()

async def async_speak(text, speed=1.2):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")

    audio = AudioSegment.from_mp3("response.mp3")
    sped_up_audio = audio.speedup(playback_speed=speed)
    sped_up_audio.export("response.wav", format="wav")
    await asyncio.to_thread(play_wav)

    os.remove("response.mp3")
    os.remove("response.wav")

def play_wav():
    wave_obj = sa.WaveObject.from_wave_file("response.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()

async def async_listen():
    with sr.Microphone() as source:
        print("Listening...")
        await async_speak("Listening")
        audio = await asyncio.to_thread(r.listen, source)

        try:
            print("Recognizing...")
            await async_speak("Recognizing")
            text = await asyncio.to_thread(r.recognize_google, audio, language='en-us')

            print("User: ", text)
            return text.lower()
        except Exception as e:
            await async_speak("Could you repeat")
            print("Could you repeat?")
            return None

async def async_handle_llm(text):
    response = await asyncio.to_thread(OlammaLLM.handle_conversation, text)
    return response

async def dialogue():
    print('------------------------Zen-----------------------')

    while True:
        text = await async_listen()

        if text == "exit":
            print("Exiting...")
            await async_speak("Bye!")
            break

        if text:
            response = await async_handle_llm(text)
            speech= "".join(response.split('.')[0:2])
            if not ("script" in text or "program" in text or "code" in text):
                await async_speak(speech, speed=1.2)
            print(f"Zen: {response}")

        else:
            continue

if __name__ == '__main__':
    asyncio.run(dialogue())
