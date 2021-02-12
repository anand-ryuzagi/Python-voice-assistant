import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import wolframalpha


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',168)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    wtime = int(datetime.datetime.now().hour)
    if wtime>=0 and wtime <= 12:
        speak('Good morning!')
    elif wtime>=12 and wtime<=18:
        speak("Good  afternoon!")
    else:
        speak("Good Evening!")
    speak("I  am  Veronica  How  may  i  help  you?")

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('aps.anand.prasad@gmail.com','81302929')
    server.sendmail('aps.anand.prasad@gmail.com',to,content)
    server.close()


def takecommand():
    ''' speech recognition module take input from microphone and return strings'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio,language="en-in")
        print(f'user said: {query}\n')

    except Exception as e:
        print(e)
        print("Say that again please")
        return "None"
    return query
if __name__ == "__main__":
    wishme()
    while True:

        query = takecommand().lower()
    
        #logic for executing task based on query
        if 'wikipedia' in query:
            print("Searching in wikipedia...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences =2)
            print(result)
            speak("according to wikipedia")
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("www.google.com")
    
        elif 'so jao' in query:
            speak("ok sir")
            break

        elif 'play music' in query:
            music_dir = 'D:\\ld gane'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir! the time is {strtime}')

        elif 'open chrome' in query:
            chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrome_path)
        
        elif 'send email to anand' in query:
            try:
                speak("what to send sir, please speak!")
                content = takecommand()
                to = 'anandsingh2609@gmail.com'
                sendemail(to,content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("sorry bhai nhi ja rha email")
        
        elif 'calculate' in query:
            print('Searching...')
            speak('Searching...')
            try:
                client = wolframalpha.Client('V4KAHY-A8Q52LUP2P')
                result = client.query(query)
                value = next(result.results).text
                print(value)
                speak(value)
            except:
                print('sorry...')
                speak('sorry...')
