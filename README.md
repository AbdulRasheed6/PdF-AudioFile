# Designing a PDF AudioFile using Python
In this code, a simple implementation of PDF AudioFile is explained.  PDF  text is read to the user as audio using this code.

#### Introduction
Reading stories or articles or any text can be arduous, however an audio reading of the text is convenient and does not require as much concentration as reading requires. In this project, I implemented a simple PDF to audio converter. This code scans page(s) of PDF and reads it using audio, to the user. While this project is good for simple text reading, it does not perform good if a scientific paper with equations is given to it because equations are not supported to be read in pyttsx3 library which we used to extract  text from Pdf.

#### Project Flow


1) First, we open the pdf using PyPDF2 Library  .
2) Then, we check if the pdf is encrypted or not using the PyPDF2 Library.
3) Then, if it is encrypted we create a function using pikepdf and tqdm to decrypt the PDF.
3) Lastly, we create a function using pyttsx3 module to play  the audio file loud.

#### Prerequisite software
The software libraries required to run this code can be installed using:

pip install -r requirements.txt

#### Conclusion




It was seen that the code performs really well in reading straightforward PDF text files, however, if equations are involved in the text, then the reader cannot properly read the equations. Hence, the code is good for simple text but not for scientific papers as it will fumble reading the equations. However, text will be read just fine. 

Please give a star to the repo to let me know if the work helped you.

# PDF-to-Audio
A PDF-to-Audio function using Python

