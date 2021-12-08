import pyttsx3
import speech_recognition as sr

def speak(text):
    troly=pyttsx3.init()
    troly.say(text)
    troly.runAndWait()
    print('Assistant:',text)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("............")
        audio = r.listen(source, phrase_time_limit=5)
        try:
            text = r.recognize_google(audio)
            print('Me:',text)
            return text
        except:
            return 0

def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text
        elif i < 2:
            speak("I can not understand, please repeat!")
    return 'user'

def stop():
    speak("See you later!")

def assistant():
    speak('What is your name?')
    name = get_text()
    speak('Hello ' +str(name))
    speak('What can I help you?')
    while True:
        text=get_audio()
        if not text:
            speak('I can not understand')
            stop()
            break
        elif 'stop' in str(text) or 'bye' in str(text):
            stop()
            break

assistant()



