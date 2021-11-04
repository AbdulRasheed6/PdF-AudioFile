import  pikepdf
from tqdm import tqdm

def Decrypt(path):
    # load password list
    passwords =[line.strip() for  line in open("Wordlist.txt")]

    ## iterate over password
    for Password in tqdm(passwords, "Decrypting PDF"):
        ## open pdf
        try:

            with pikepdf.open(path, password="Password") as pdf:
                print("[+] Password found:" , Password)
                return pdf
                
                

                break
            ## an error is raised 
        except pikepdf._qpdf.PasswordError as e:
            
            print("{} not decrypted".format(path))
            # wrong password just continue in a loop
            continue


