#Talking Santa

# We'll start talking when we hear the keyword - Ok, Santa. 
# The conversation goes on till the system hear Ok, Bye.

# Basic workflow:
# App listen to human -> Send to chatGPT -> Get response from chatGPT -> Speaks to human

import speech_recognition as sr
import openai_lib

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print('say something')
    audio = recognizer.listen(source)
    with open("audio_file.wav", "wb") as file:
        file.write(audio.get_wav_data())

speechToText = openai_lib.speechToText("audio_file.wav")
print(speechToText)

system_prompt = """You are a Santa. You will get prompts from user as if they are talking to a Santa and you should reply to them 
                like you are talking to children from Santa. You should be funny and interesting. Don't add any emoji in the response. """

gpt_text = openai_lib.chat(speechToText, system_prompt)

print(gpt_text)