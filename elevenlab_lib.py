from elevenlabs import generate, play, set_api_key
import os

set_api_key(os.getenv('ELEVEN_API_KEY'))
os.environ['PATH'] += os.pathsep + 'C:\\ffmpeg\\bin'

def speak(textToSpeech, ):
    audio = generate(
    text=textToSpeech,
    voice="Oswald",
    model="eleven_monolingual_v1"
    )
    
    play(audio)