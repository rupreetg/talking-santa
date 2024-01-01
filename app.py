#Talking Santa

# We'll start talking when we hear the keyword - Okay Santa. 
# The conversation goes on till the system hear GoodBye Santa.

# Basic workflow:
# App listen to human -> Send to chatGPT -> Get response from chatGPT -> Speaks to human

import speech_recognition as sr
import openai_lib
import elevenlab_lib

recognizer = sr.Recognizer()
activation_keyword = "Okay Santa".lower()
termination_keyword = "Goodbye Santa".lower()

def record():
    with sr.Microphone() as source:
        print('say something')
        audio = recognizer.listen(source)
        #speech = recognizer.recognize_google_cloud(audio).lower()
        #if(keywork in speech):
        with open("audio_file.wav", "wb") as file:
            file.write(audio.get_wav_data())
        return True 

def speak(textToSpeak):
    system_prompt = """You are a Santa. You will get prompts from user as if they are talking to a Santa and you should reply to them 
                    like you are talking to children from Santa. You should be funny and interesting. Don't add any emoji in the response. """

    gpt_text = openai_lib.chat(textToSpeak, system_prompt)
    print(gpt_text)

    elevenlab_lib.speak(gpt_text)


while True:
    if(record()):
        speechToText = openai_lib.transcribe("audio_file.wav")
        print(speechToText)        
        
        if(activation_keyword in speechToText.lower()):
            command = speechToText.lower().split(activation_keyword)[1]
            print("Command: " + command)
            speak(command)

        if(termination_keyword in speechToText.lower()):
            break

