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
            return 'user'
def stop():
    speak("See you later!")

def assistant():
    speak('What is your name')
    name = get_audio()
    speak('Hello ' +str(name))
    speak('What can I help you?')
    a=1
    while a > 0:
        text=get_audio()
        if 'stop' in str(text) or 'bye' in str(text):
            stop()
            break
        elif text=='user':#không nói gì tức là text=user
            speak('I can not understand')
            stop()
            break
        else:
            speak('I can not understand')
assistant()



