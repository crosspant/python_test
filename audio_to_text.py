from io import BytesIO

import openai
import speech_recognition as sr

openai.api_key = "openapikey"

r = sr.Recognizer()
with sr.Microphone(sample_rate=16_000) as source:
    print("What do you wanna talk?")
    audio = r.listen(source)
    print("Thingking...")

audio_data = BytesIO(audio.get_wav_data())
audio_data.name = "from_mic.wav"
transcript = openai.Audio.transcribe("whisper-1", audio_data)
print(transcript["text"])
