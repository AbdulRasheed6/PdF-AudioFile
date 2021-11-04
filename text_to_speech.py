import pyttsx3
import typing
def speech(Text:object):
    ## extract the text
    
    ## reading the text
    speak= pyttsx3.init()
    speak.say(Text)
    speak.runAndWait()
