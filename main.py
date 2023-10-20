from dotenv import load_dotenv
load_dotenv()
from chat import chat
import openai
import os
from audio import record_audio
openai.api_key = os.getenv("OPENAI_API_KEY")

record_audio("input.wav")

audio_data = open("input.wav", "rb")
response = openai.Audio.transcribe("whisper-1", audio_data)

transcript = response.text
print("Transcription:", transcript)

chat(transcript)