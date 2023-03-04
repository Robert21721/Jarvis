import pyttsx3
import datetime
from datetime import date
import webbrowser
import speech_recognition as sr
import switcher
import whatsapp
import webbrowser

engine = pyttsx3.init()
today = date.today()


def speak(audio):

    engine = pyttsx3.init("espeak")
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[11].id)
    engine.setProperty('rate', 170)
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)


def date():
    d = today.strftime("%B %d %Y")
    speak(d)


def wishme():
    speak("Welcome back sir! Jarvis at your service. Please tell me how can I help you")


def Firefox():
    webbrowser.get('firefox').open_new_tab('http://www.google.com')


def websearch(command):
    webbrowser.open("https://google.co.in/search?q=" + command)


def Youtube():
    webbrowser.open("https://www.youtube.com")


def WappMessage(message):
    name = message.split()[0]
    name = name.capitalize()
    message = message[len(name) + 1:]
    whatsapp.WhatsApp_Messages(name, message)


# def WappCall(name):
#     whatsapp.WhatsApp_Call(name)


def Words():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        print("Listening...")

        r.pause_threshold = 1
        audio = r.listen(source, timeout=10)
    try:
        print("Recognizning...")
        global query
        query = r.recognize_google(audio, language='en-in')

    except Exception as e:
        print(e)
        query = "exception"
        speak("Say that again please...")


ok = 1

def TakeCommand():

    Words()
    if(query == "no thanks" or query == "stop"):
        global ok
        ok = 0

    elif query != "exception":
        switcher.simple_switcher(query)
        speak("Can i help you with something else?")


def takeCommand_loop():

    while(True):
        TakeCommand()

        if(ok == 0):
            break
