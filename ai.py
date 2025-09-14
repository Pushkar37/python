import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import os
from googlesearch import search
from pygame import mixer





engine = pyttsx3.init()


def speak(audio):
    
    engine.say(audio)
    engine.runAndWait()

def time():
    time=datetime.datetime.now().strftime("%H:%M:%S")
    speak("the current time is")
    speak(time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("current date is ")
    speak(day)
    speak(month)
    speak(year)

def wishme():
    speak("welcome back sir ")
    
    hour=datetime.datetime.now().hour 
    if(hour>=6 and hour<12):
        speak("Good Morning")
    elif(hour>=12 and hour<16):
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("how can i help you")

def takeCommand():
    r=sr.Recognizer() 
    with sr.Microphone() as source:
        print("listening")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recognizing")
        query=r.recognize_google(audio,language='en-In')
        print(query)
    except Exception as e:
        print(e)
        speak("please,repeat the query")
        return "none"
    return query
def musiccommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("any commands for me")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("executing command")
        command=r.recognize_google(audio,language='en-In')
        print(command)
    except Exception as e:
        print("could not execute command try again")
        return "none"
    return command
        


    
if __name__=="__main__" :
    wishme()
     
    while True:
        query=takeCommand().lower()
        
        if 'what time' in query:
            time()
        if 'date' in query:
            date()
        if 'wikipedia' in query:
            speak("Searching..")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query ,sentences = 2,auto_suggest=False)
            print(result)
            speak(result)
        if 'search on google' in query:
            speak("Here are your links ")
            query =query.replace("search on google about","")
            for j in search(query,tld="co.in",num=10,stop=10,pause=2):
             print(j)
             
        if 'open' in query:
            speak("opening")
            query=query.replace("open","")
            if 'google' in query:
                os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome")
            if 'notepad' in query:
                os.startfile("notepad")
            if 'camera' in query:
                os.startfile("Camera")
        
            
        
        if 'play' in query:
            query=query.replace("play","")
            query=query[1:]
            
            if 'baby one more time' in query:
              mixer.init()
              mixer.music.load("baby one more time.mp3") 
              mixer.music.play()
              inp=input("Press y to give voice command")
              if 'y' in inp:
                  while True:
                
                   a=musiccommand()
                   if 'pause' in a:
                      mixer.music.pause()
                   if 'play' in a:
                      mixer.music.play()
                   if 'next' in a:
                       mixer.music.load("the search.mp3") 
                       mixer.music.play()
                       inp1=input("Press y to give voice command")
                       if 'y' in inp1:
                         while True:
                          a=musiccommand()
                          if 'pause' in a:
                             mixer.music.pause()
                          if 'play' in a:
                             mixer.music.play()
                          if 'stop' in a:
                             mixer.music.stop()
                             quit()   
                    
                   if 'stop' in a:
                      mixer.music.stop()
                      quit()   
            if 'the search' in query:
                
              mixer.music.load("the search.mp3") 
              mixer.music.play()
              inp2=input("Press y to give command")
              if 'y' in inp2:
                   while True:
                     a=musiccommand()
                     if 'pause' in a:
                         mixer.music.pause()
                     if 'play' in a:
                         mixer.music.play()
                     if 'next' in a:
                         mixer.music.load("baby one more time.mp3") 
                         mixer.music.play()
                         while True:
                          a=musiccommand()
                          if 'pause' in a:
                             mixer.music.pause()
                         if 'play' in a:
                              mixer.music.play()
                         if 'next' in a:
                             mixer.music.load("the search.mp3") 
                             mixer.music.play()
                             while True:
                              a=musiccommand()
                              if 'pause' in a:
                                 mixer.music.pause()
                              if 'play' in a:
                                 mixer.music.play()
                              if 'stop' in a:
                                 mixer.music.stop()
                                 quit()   
                        
                              if 'stop' in a:
                                  mixer.music.stop()
                                  quit()   
                
                
                  
        if 'quit' in query:
            quit()