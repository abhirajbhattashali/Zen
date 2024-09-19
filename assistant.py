import speech_recognition as sr
from gtts import gTTS
import os
from fetchLLM import OlammaLLM
from pydub import AudioSegment
import asyncio
import simpleaudio as sa
import re
from OpenScriptInVS import create_program_file

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
    response = response.replace("</end_of_turn>", "").strip()
    return response



async def dialogue():
    print('----------------------------Zen-----------------------------')

    while True:
        text = await async_listen()

        if text == "exit":
            print("Exiting...")
            await async_speak("Bye!",speed=1.2)
            break

        if text:
            response = await async_handle_llm(text)
            if OlammaLLM.is_code_query(text):
                try:
                    formatted_response = f"{OlammaLLM.format_llm_response(response)}"

                    file_ext = OlammaLLM.handle_file_extension(response)
                    file_ext = file_ext.replace("</end_of_turn>", "").strip()
                    label = file_ext[1:]
                    file_name = f"zen_{label}_script{file_ext}"
                    create_program_file(file_name, formatted_response)



                    phrase = "Source code successfully generated"
                    await async_speak(phrase,speed=1.2)
                    print(f"Zen: {phrase}")
                    print('-'*100)
                    print(response)
                    print('-' * 100)
                except Exception:
                    print("Zen: Error occurred while generating source code")



            else:
                speech = "".join(response.split('.')[0:3])
                await async_speak(speech, speed=1.2)
                print()



        else:
            continue

if __name__ == '__main__':
    asyncio.run(dialogue())
