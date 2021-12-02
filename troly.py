import pyttsx3
import speech_recognition as sr

def getaudio():
    voice = sr.Recognizer()
    with sr.Microphone() as mic:
        print('I am listening..')
        audio = voice.listen(mic)
    try:
        user = voice.recognize_google(audio)
    except:
        user= "I do not understand"
    print(user)
    return user
def speak(text):
    troly=pyttsx3.init()
    troly.say(text)
    troly.runAndWait()
    print(text)

speak('What is your name')
name = getaudio()
speak('Hello '+ name)