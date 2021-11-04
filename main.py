from os import path
import PyPDF2
import pyttsx3
import typing
import os
from encryption import Decrypt
from extract_text import Text
from text_to_speech import speech

def pdf_to_speech(Pdf_folder:str, Pdf_doc:str):

    ## the path of the pdf
    Pdf_path =os.path.join(os.getcwd(), Pdf_folder, Pdf_doc)

    ## open the pdf file
    path =open(Pdf_path,"rb" )

    ## create a PdfFilereader object
    pdfReader= PyPDF2.PdfFileReader(path)
    

    ## check if the pdf is encrypted
    if pdfReader.isEncrypted:
       ## store the decrypted pdf in a variable called Reaf_Pdf 
        Read_Pdf =Decrypt(path)

        ## read the decrypted pdf 
        Decrypted_pdf= PyPDF2.PdfFileReader(Read_Pdf)

        ## we create a new object 'Page_number' which takes in an int
        ## then we pass the value of 'Page_number' into the  argument of a function Text (that is 'page_number')
        Page_number =input("Please enter a page number:")
        Page_number =int(Page_number)
        
        ## extract the text from the pdf using the Text function
        raw_text= Text(Decrypted_pdf, Page_number)

        ## use the speech function to transform the text to spoken input
        speech(raw_text)
    else:
        ## we create a new object 'Page_number' which takes in an int
        ## then we pass the value of 'Page_number' into the  argument of a function Text (that is 'page_number')
        Page_number= input("Please enter a page number:")
        Page_number=int(Page_number)

        ## extract the text from the pdf using the Text function
        raw_text =Text(pdfReader, Page_number)
        speech(raw_text)
        


        
pdf_to_speech('PDF_File', 'Experiment NO.4.pdf')


