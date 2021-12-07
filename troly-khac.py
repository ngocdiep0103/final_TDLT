import pyttsx3
import speech_recognition as sr

def speak(text):
    troly=pyttsx3.init()
    troly.say(text)
    troly.runAndWait()
    print(text)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm listening ")
        audio = r.listen(source, phrase_time_limit=5)
        try:
            text = r.recognize_google(audio)
            return text
        except:
            print("I cannot hear")
            return 0

def stop():
    speak("See you later!")

speak('What is your name')
name = get_audio()
speak('Hello '+ name)
stop()