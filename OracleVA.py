from gtts import gTTS
import speech_recognition as sr 
from playsound import playsound
import datetime
import wikipedia
import webbrowser
import os

def speak(speech):
    filename = "speech.mp3"
    audio = gTTS(text=speech,lang='en',slow=False)
    audio.save(filename)
    print("Saying:", speech)    
    playsound(filename)
    os.remove(filename)

def wishMe():   #wishes according to time
    hour = int(datetime.datetime.now().hour)
    #print(hour) 
    if hour >= 0 and hour < 12:
        speak("Good Morning!. How may help you, sir?")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon! How may help you, sir?")
    elif hour >= 18 and hour < 21:
        speak("Good Evening! How may help you, sir?")
    else:
        speak("Good Night! How may help you, sir?")
    

def takeCommand():      #takes microphone input and returns strings
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....") 
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said: {query}\n")
    except Exception as e:
        #print(e)
        speak("Say that again please")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()        
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:            
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)            
            speak("According to wikipedia " + results)
        elif 'youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com/")
        elif 'google' in query:
            speak("Opening Google.com")
            webbrowser.open("https://google.com/")
        elif 'email' in query or 'gmail' in query:
            speak("Opening Email")
            webbrowser.open("https://mail.google.com/")
        elif 'music' in query or 'song' in query:
            speak("Opening YouTube Music")
            webbrowser.open("https://music.youtube.com/")
        elif 'time' in query:
            time = datetime.datetime.now().strftime("%H:%M")
            speak("The time is " + time)
        elif 'today' in query:
            d = datetime.date.today()
            speak("Today is "+str(d))
        elif 'code' in query:
            codePath = "C:\\Users\\THUNDER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("Opening Visual Studio Code")
            os.startfile(codePath)
        elif 'oracle' in query or 'who are you' in query:
            text = "I am Oracle. I have been developed by Samiruddin Thunder. I am built upon Python. I am here to help you. How may I help you, sir?"
            speak(text)
        elif 'what can you do' in query or 'can do' in query:
            text = "I can open youtube, google.com, gmail for you. I can play music for you. I can open Visual Studio Code and tell the time and date for you. How may I help you, sir?"
            speak(text)
        elif 'quit' in query or 'shutdown' in query or 'sleep' in query:
            speak("Goodbye, Sir")
            quit()

input()


        



