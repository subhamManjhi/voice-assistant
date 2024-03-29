import speech_recognition as sr
from . import search 
from . import info
from playsound import playsound
from . import addFiles
import re


# creating an object of recognizer
recognizer = sr.Recognizer()

def getQuery():
    with sr.Microphone() as source:
        print("speak now ...")
        query = recognizer.listen(source)
        #recognizing a query i.e converting to string
        queryInText = recognizer.recognize_google(query)
        print("YOU:",queryInText)
        return queryInText

def waitForCall():
    with sr.Microphone() as source:
        call = recognizer.listen(source=source,phrase_time_limit=3)
        if(recognizer.recognize_google(call)=="hello"):
            return True
        return False

def handleQuery(string):
    if('search' in string):
        search.search(string.split("search")[1])
    elif('today' in string and 'date' in string):
        info.date()
    elif('time' in string and 'now' in string):
        info.time()
    elif("who are you" in string ):
        info.intro()
    elif('add' in string or 'display' in string):
        addFiles.handleFiles(string)
    else:
        playsound('./Data/audio/unrecognized.mp3')


