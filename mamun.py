import pyttsx3
import webbrowser
import random
import wikipedia
import datetime
import wolframalpha
import os
import sys

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('XHH495-74TX5U9WPL')

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')
greetMe()
def course():
    speak('Welcome to AI Sessional Test')
    speak('Course Teacher is Saha Renu and External Teacher is Shovon Bhowmik')
    speak('Thanks for Teching us')
course()

speak('Hello Team Artiligence, I am your digital assistant!')
speak('How may I help you?')
        
if __name__ == '__main__':

    while True:
        query = str(input('Command: '))
        query = query.lower()
        
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'access classroom' in query:
            speak('okay')
            webbrowser.open('www.classroom.google.com')
            
        elif 'go to website' in query:
            speak('okay')
            webbrowser.open('https://fireawareness.wordpress.com')

        elif 'baiust website' in query:
            speak('okay')
            webbrowser.open('www.baiust.edu.bd')
            
        elif "whats up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))
            
        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Bye Team Artiligence, have a good day.')
            sys.exit()

        
        elif 'hello' in query:
            speak('Hello Team Artiligence')

        elif 'bye' in query:
            speak('Bye Bye Team Artiligence, have a good day.')
            sys.exit()
            
        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Next Command!!')
