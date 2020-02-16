import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
from tkinter.filedialog import askdirectory
import pygame
from mutagen.id3 import ID3
import mp3play
from tkinter import *
import spotipy
from spotipy import util as util
from json.decoder import JSONDecodeError
import omdb

'''Internet Needed'''
engine = pyttsx3.init()
client = wolframalpha.Client('LRWJW6-436RP7LH87')

google = 'search for'
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    print('S.K.A.V.A : ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 10 and currentH < 3:
        speak('Hi Sir,Good Morning! The time is',currentH)
        speak('The time is '+(str(datetime.datetime.now().strftime('%H:%M:%S'))))

    if currentH >= 3 and currentH < 16:
        speak('Hi Sir,Good Afternoon!')
        speak('The time is '+(str(datetime.datetime.now().strftime('%H:%M:%S'))))

    if currentH >= 16 and currentH <19:
        speak('Hi Sir,Good Evening!')
        speak('The time is '+(str(datetime.datetime.now().strftime('%H:%M:%S'))))

    if currentH >= 19 and currentH >10:
        speak('Good Night sir! ')
        speak('The time is '+(str(datetime.datetime.now().strftime('%H:%M')))+'pm')
        #speak ('May i help you?')

greetMe()

speak('I am your assistant SKAVA ,How may I help you?')


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source)
    try:
        #query = r.recognize_sphinx(audio).lower()
        query = r.recognize_google(audio).lower()
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        print("Sphinx error; {0}".format(e))
        query=input("")

    return query

listofsongs = []
realnames = []
index = 0

if __name__ == '__main__':

     while True:
          query = myCommand();
          query = query.lower()

          if 'open youtube' in query:
               speak('okay')
               webbrowser.open('www.youtube.com')

          elif google in query:
               words = query.split()
               del words[0:2]
               st = ' '.join(words)
               print('Google Results for: '+str(st))
               url='http://google.com/search?q='+st
               webbrowser.open(url)
               speak('Google Results for: '+str(st))





     
          elif 'open google' in query:
               speak('okay')
               webbrowser.open('www.google.co.in')


          elif 'open gmail' in query:
               speak('okay')
               webbrowser.open('www.gmail.com')

          elif "what\'s up" in query or 'how are you' in query:
               stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
               speak(random.choice(stMsgs))

          elif "who is sabesh kumar" in query or 'who is sabesh' in query or 'who is sarvesh kumar' in query or 'who is sarvesh' in query or 'sarvesh kumar' in query or 'sarvesh' in query:
               stMsgs = ['sabesh kumar is a person/human/alien who created me using his Techy Brain\n',]
               speak(random.choice(stMsgs))

          elif "describe about you" in query or 'who are you' in query or 'what is your name' in query or 'who you are' in query:
               stMsgs = ['My Name is SKAVA : \"Sabesh Kumar\'s - Advanced - Voice - Assistant ',]
               speak(random.choice(stMsgs))



          elif "what is sabesh kumars passion" in query or 'what is sabesh kumar passion' in query or 'sabesh kumar passion' in query or 'what is sarvesh passion' in query or 'sarvesh kumar passion' in query or 'sarvesh passion' in query or 'what is sabesh kumars passion' in query or 'what is sarvesh kumars passion' in query: 
               stMsgs = ['sabesh kumar is a person/human/alien who created me using his Techy Brain\n',]
               speak(random.choice(stMsgs))

          elif 'who is your creator' in query or 'who developed you' in query or 'who is your creator' in query:
               stMsgs = ['Sabesh Kumar is my God... He developed me for his Personal USE,Iam not an Artificial Inteligice, iam a programed Voice Assistant : )']
               speak(random.choice(stMsgs))

          elif 'who am i' in query:
               stMsgs = ['if ou don\'t know who you are then why you are living in Earth??? ']

          elif "can you die" in query or 'you die' in query:
               stMsgs = ['Sorry sir I can\'t,until you says kill yourself ', 'Sorry sir! it apart from my rules']
               speak(random.choice(stMsgs))

          elif 'what is the meaning of your name' in query or 'what is SKAVA' in query or 'what is S K A V A' in query or 'what is skava' in query or 'what is expansion of skava' in query or 'your name' in query:
               stMsgs = ['My Name is SKAVA , The expansion of SKAVA is \"Sabesh Kumar\'s - Advanced - Voice - Assistant ']
               speak(random.choice(stMsgs))


          elif "Tell me motivation Quotes" in query or 'motivate me' in query:
               stMsgs = ['Failure will never overtake me if my determination to succeed is strong enough',
                      'The past cannot be changed. The future is yet in your power',
                      'Only I can change my life. No one can do it for me',
                      'Change your life today. Don\'t gamble on the future, act now, without delay',
                      'Do the difficult things while they are easy and do the great things while they are small. A journey of a thousand miles must begin with a single step',
                      'Either I will find a way, or I will make one',
                      'Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time',
                      'Good, better, best. Never let it rest. Till your good is better and your better is best']
               highMsgs = ['Dont worry dude,every hard time comes to an end']
               speak(random.choice(stMsgs))
               speak('I think this Motivated You sir ... if Not . . .')
               speak('Try This one '+random.choice(highMsgs))
            
          elif "Tell me a joke " in query or 'joke' in query:
               stMsgs = ['What do you call a fish without eye?\n Fsh \n\n haa haa haa haa haa haa haaa','What do you call an alligator detective?\n  An investi-gator \n\n  haa haa haa haa haa haa haaa']
               speak(random.choice(stMsgs))

          elif 'email' in query:
               speak('Who is the recipient? ')
               recipient = myCommand()

               if 'me' in recipient:
                    try:
                         speak('What should I say? ')
                         content = myCommand()

                         server = smtplib.SMTP('smtp.gmail.com', 587)
                         server.ehlo()
                         server.starttls()
                         server.login("Your_Username", 'Your_Password')
                         server.sendmail('Your_Username', "Recipient_Username", content)
                         server.close()
                         speak('Email sent!')

                    except:
                         speak('Sorry Sir! I am unable to send your message at this moment!')


          elif 'nothing' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'kill yourself' in query or 'destroy yourself' in query or 'get destroyed' in query:
               speak('okay')
               speak('Bye Sir, have a good day.')
               sys.exit()

          elif 'what time is it' in query or 'what is the time skava' in query or 'what time is it' in query or 'time' in query or 'current time' in query:
               speak('The current time is '+(str(datetime.datetime.now().strftime('%H:%M:%S'))))

          elif 'what date is it' in query or 'what is the date skava' in query or 'what date is it' in query or 'date' in query or 'current date' in query:
               speak('The current time is '+(str(datetime.datetime.now().strftime('%H:%M:%S'))))

          elif 'hello' in query:
               speak('Hello Sir')

          elif 'note' in query:
               nte = myCommand()
               speak('opening note')
               if 'enter' in nte:
                    fh = open ('demo.txt','w')
                    fh.write(query)
                    r.pause_threshold =  1
                    #r.adjust_for_ambient_noise(source, duration=1)
                    audio = r.listen(source)
                    fh.close()

               elif 'exit' in nte:
                    break
               
               else:
                    speak ('sorry sir')
                                    
          elif 'play music' in query or 'play songs' in query or 'play songs skava' in query or 'play a song' in query or 'play song' in query:
               music_folder = 'S:\\AI\\music\\'
               music = ['Alex_Sparrow-sheiscrazybutsheismine','wedont','Konjam','stressedout']
               random_music = music_folder + random.choice(music) + '.mp3'
               speak('Okay, here is your music! Enjoy!')
               os.system(random_music)

          elif 'play english music' in query or 'play english songs' in query or 'play english songs skava' in query or 'play english song' in query:
               music_folder = 'S:\\AI\\music\\'
               music = ['Alex_Sparrow-sheiscrazybutsheismine','wedont','Konjam','stressedout']
               random_music = music_folder + random.choice(music) + '.mp3'
               speak('Okay, here is your music! Enjoy!')
               os.system(random_music)

          elif 'play tamil music' in query or 'play tamil songs' in query or 'play tamil songs skava' in query or 'play tamil song' in query:
               music_folder = 'S:\\AI\\music\\'
               music = ['Konjam']
               random_music = music_folder + random.choice(music) + '.mp3'
               speak('Okay, here is your music! Enjoy!')
               os.system(random_music)

          elif 'play hindi music' in query or 'play hindi songs' in query or 'play hindi songs skava' in query or 'play hindi song' in query:
               music_folder = 'S:\\AI\\music\\'
               music = ['ikvaariaa']
               random_music = music_folder + random.choice(music) + '.mp3'
               speak('Okay, here is your music! Enjoy!')
               os.system(random_music)

          else:
               query = query
               speak('Searching...')

               try:
                    try:
                         res = client.query(query)
                         results = next(res.results).text
                         #speak('google says - ')
                         #speak('Got it.')
                         speak(results)

                    except:
                         results = wikipedia.summary(query, sentences=2)
                         speak('Got it.')
                         #speak('WIKIPEDIA says - ')
                         speak(results)


               except:
                    speak('I Think Google is Inteligent than me :-)')
                    webbrowser.open('www.google.com')
                    


     speak('any other Command Sir!')

