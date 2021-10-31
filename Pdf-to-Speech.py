from os import path
import PyPDF2
import pyttsx3
import os
from encryption import Decrypt
from text_to_speech import speech

def pdf_to_speech(Pdf_folder, Pdf_doc, page_number):

    ## the path of the pdf
    Pdf_path =os.path.join(os.getcwd(), Pdf_folder, Pdf_doc)

    ## open the pdf file
    path =open(Pdf_path,"rb" )

    ## create a PdfFilereader object
    pdfReader= PyPDF2.PdfFileReader(path)

    ## check if the pdf is encrypted
    if pdfReader.isEncrypted:
       ## decrypt the password using Decrypt 
        Read_Pdf =Decrypt(path)
        ReadPdf=Read_Pdf
        get_page =ReadPdf.getPage(page_number)
        speech(get_page)
    else:
        ReadPdf=pdfReader
        get_page =ReadPdf.getPage(page_number)
        speech(get_page)
        
pdf_to_speech('PDF_File', 'Experiment NO.4.pdf', 0)


