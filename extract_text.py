
import pyttsx3
from text_to_speech import speech
## this function takes in an already and decrypted pdf and a page_number
def Text(Opened_Pdf:object, page_number:int):

    get_page =Opened_Pdf.getPage(page_number)

    text =get_page.extractText()
    speech(text)
    print(text)
