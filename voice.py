from dotenv import load_dotenv
import os
import requests
load_dotenv()

CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL"

headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": os.getenv("EL_KEY"),
}

def voice(ai):
    data = {
        "text": ai,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    response = requests.post(url, json=data, headers=headers)
    with open('output.mp3', 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)

    
if __name__ == "__main__":
    text_to_speak = "Hello, this is a test 2."
    voice(text_to_speak)
