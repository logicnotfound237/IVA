import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
newVoiceRate = 150
engine.setProperty('rate', newVoiceRate)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def runtest():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
        speak("hope your day will be good")
        print("this project is made by aditya dwivedi.")
        print("roll.no :- 11115")
        print("class:- XI  section :-'A'")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
        print("this project is made by aditya dwivedi.")
        print("roll.no :- 11115")
        print("class:- XI  section :-'A'")
    else:
        speak("Good Evening!")
        speak("how was your day")
        print("this project is made by aditya dwivedi.")
        print("roll.no :- 11115")
        print("class:- XI  section :-'A'")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("i didn't get that")
        speak("i didn't get that")
        return "None"
    return query


if __name__ == '__main__':
    runtest()
    while True:
        query = takeCommand().lower()
        if 'tell me' in query:
            speak('Searching')
            query = query.replace("tell me", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'thank you' in query:
            z = "its okay i love helping other people"
            speak(z)

        elif 'play some music' in query:
            song_location = 'D:\\music'
            songs = os.listdir(song_location)
            A = random.randint(0, 93)
            os.startfile(os.path.join(song_location, songs[A]))
            B = os.path.join(song_location, songs[A])
            C = str(B.replace('\\', ''))
            D = C.replace("D:music", "")
            E = D.replace(".mp3", "")
            speak("as you say")
            print("now playing:-", E)

        elif 'play music' in query:
            song_location = 'D:\\music'
            songs = os.listdir(song_location)
            A = random.randint(0, 93)
            os.startfile(os.path.join(song_location, songs[A]))
            B = os.path.join(song_location, songs[A])
            C = str(B.replace('\\', ''))
            D = C.replace("D:music", "")
            E = D.replace(".mp3", "")
            speak("all right")
            print("now playing:-", E)

        elif 'play something' in query:
            song_location = 'D:\\music'
            songs = os.listdir(song_location)
            A = random.randint(0, 93)
            os.startfile(os.path.join(song_location, songs[A]))
            B = os.path.join(song_location, songs[A])
            C = str(B.replace('\\', ''))
            D = C.replace("D:music", "")
            E = D.replace(".mp3", "")
            speak("done")
            print("now playing:-", E)

        elif 'play different' in query:
            song_location = 'D:\\music'
            songs = os.listdir(song_location)
            A = random.randint(0, 93)
            os.startfile(os.path.join(song_location, songs[A]))
            B = os.path.join(song_location, songs[A])
            C = str(B.replace('\\', ''))
            D = C.replace("D:music", "")
            E = D.replace(".mp3", "")
            speak("okay")
            print("now playing:-", E)

        elif 'change the music' in query:
            song_location = 'D:\\music'
            songs = os.listdir(song_location)
            A = random.randint(0, 93)
            os.startfile(os.path.join(song_location, songs[A]))
            B = os.path.join(song_location, songs[A])
            C = str(B.replace('\\', ''))
            D = C.replace("D:music", "")
            E = D.replace(".mp3", "")
            speak("changing it")
            print("now playing:-", E)

        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {time}")

        elif 'open c drive' in query:
            Path = "C:"
            os.startfile(Path)

        elif 'open d drive' in query:
            Path = "D:"
            os.startfile(Path)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            webbrowser.open("www.google.com/maps/place/" + location + "/&amp;")

        '''if "remind me" in query:
            number = []
            for a in query.split():
                if a.isdigit():
                   number.append(int(a))
                   t = int(number[0])
                   t_t = t             
                   Z = query.replace("remind me to", "")
                   speak("okay i will remind you to" + Z + ".")
                   A = time.time()+t_t
                   B = time.time()
                   print(A)
                   print(B)
                   while True:
                       if time.time() == A:
                           speak("you have to" + Z + ".")'''    

        if "bye" in query:
            speak("see you next time bye")
            self_loc.close()
            self_loc = 'D:\\IVA\\iva.py'
           

        if "buy" in query:
            speak("see you next time bye")
            self_loc.close()
            self_loc = 'D:\\IVA\\iva.py'

        if "can you calculate" in query:
            speak("well i am sorry the person who programed me is an idiot he did not programed me to do calculations")

        if "reply to om" in query:
            speak("nice work on that meem ")    
            print("                               ")

        if "can you explain me what is debugging" in query:
            speak("its like being the detective in a crime movie where you are also the murderer")

