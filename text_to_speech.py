import pyttsx3

def speech(get_page):
    ## extract the text
    text =get_page.extractText()

    ## reading the text
    speak= pyttsx3.init()
    speak.say(text)
    speak.runAndWait()
