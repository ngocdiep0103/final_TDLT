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
        elif i<2:
            speak("I can not understand, please repeat!")
    return 'user'

def welcome():
    hour = datetime.now().hour
    if hour >=6 and hour<12:
        speak('Good morning')
    elif hour >=12 and hour<18:
        speak('Good afternoon')
    else:
        speak('Good night')

def get_day():
    today = date.today()
    # Hàm strftime() trong Python trả về một chuỗi biểu diễn giá trị ngày, giờ và thời gian bằng cách sử dụng các đối tượng date, time và datetime.
    d2 = today.strftime("%B %d, %Y")
    print("Today is " + d2)
    return d2

def get_time():
    now = datetime.now()
    time = now.strftime("%I:%M %p")
    print("Current time is : " + time )
    return time

def stop():
    speak("See you later!")

def assistant():
    speak('What is your name?')
    name = get_text()
    speak('Hello ' +str(name))
    speak('What can I help you?')
    while True:
        text=get_text()
        if text=='user':
            speak('I can not understand')
            stop()
            break
        elif 'time' in str(text):
            get_time()
        elif 'day' in str(text):
            get_day()
        elif 'stop' in str(text) or 'bye' in str(text):
            stop()
            break

assistant()
