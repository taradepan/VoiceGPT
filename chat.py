from dotenv import load_dotenv
load_dotenv()
import os
import pygame
import openai
from voice import voice
from test import play_audio
import mutagen.mp3
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat(userInput):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=100,
    messages=[
        {"role": "system", "content": "You are a personal A.I. assistant and your name is 'Bella'. try to answer the user's questions under 100 tokens"},
        {"role": "user", "content": userInput},
    ]
    )

    print(completion.choices[0].message.content)

    voice(completion.choices[0].message.content)
    play_audio("output.mp3")

# chat("Hello, what is openai?")

def get_audio_duration(audio_file):
    audio = mutagen.mp3.MP3(audio_file)
    return audio.info.length

def play_audio(audio_file):
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    audio_duration = get_audio_duration(audio_file)
    delay_seconds = int(audio_duration) 

    pygame.time.delay(delay_seconds * 1000 + 1000)  

    pygame.mixer.music.stop()

if __name__ == "__main__":
    audio_file = "output.mp3"  
    play_audio(audio_file)

    audio_duration = get_audio_duration(audio_file)
    delay_seconds = int(audio_duration) 

    pygame.time.delay(delay_seconds * 1000 + 1000)  

    pygame.mixer.music.stop()
