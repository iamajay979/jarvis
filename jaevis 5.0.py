import pyttsx3  
import speech_recognition as sr  
import datetime
import wikipedia  
import webbrowser
import os
import smtplib
import pywhatkit as kit
from requests import get 



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am jarvis Sir. Please tell me how may I help you  speak ")


def takeCommand():
    # It takes microphone input from the user and returns string output

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
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

       
if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query: str = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("sir, what should i search on google")
            query = takeCommand().lower()
            webbrowser.open(f"{query}")


        elif 'send a message' in query:
            kit.sendwhatmsg ("+911234567890","this is testing protocoal",9,33)

        elif 'play song on youtube' in query:
            
             kit.playonyt("see you again")

        elif 'ip address' in query:
             ip = get ( 'https://www.ipify.org' ).text 
             speak(f"sir,this is your ip adress{ip}")  


        elif 'open stack overflow' in query:
            webbrowser.open("www.stackoverflow.com")

        elif 'open my class'in query:
            webbrowser.open("lovelyprofessionaluniversity.codetantra.com")

        elif 'open github' in query:
            webbrowser.open("github.com")


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

       

        elif 'email to ajay' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ajayyourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend ajay . I am not able to send this email")


