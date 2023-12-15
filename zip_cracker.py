#!/usr/bin/env python3

from zipfile import *
import time
import numpy as np
import sys
import time
import webbrowser as wb

archies = sys.argv

file_zip = archies[1]
psswdlist = archies[2]

for i in range(5):
    print("·", end="")
    time.sleep(1)

print('WELCOME TO ZIP CRACKER!\nHow to use:\nCommandline: "./zip_cracker.py [file.zip] [password_list.txt]"')

def hailEris():
    try:
        while 2 < 3:
            print("HAIL ERIS!!!!!")
            time.sleep(0.5)
    except FileNotFoundError:
        print("And this.")

def wtfDisco():
    try:
        wb.open("https://www.principiadiscordia.com/downloads/Principia%20Discordia%20(Wholly%201st%20Edition).pdf", autoraise=True) 
    except FileNotFoundError:
        print("And this.")

def crack_zip(zipFile, list_pass):
    
    df = np.loadtxt(list_pass, dtype="str")
    
    for pswd in df:
        try:
            with ZipFile(zipFile) as zf:
                zf.extractall(pwd=pswd.encode())
                print(f'SUCCESS! Password is:{pswd}')
                time.sleep(0.1)
                return
        except FileNotFoundError:
            print("And that!")
            continue
        except BadZipfile:
            print("Sorry! File not found! :(")
            time.sleep(0.1)
            return
        except RuntimeError:
            print(f'Incorrect password:{pswd}')
            time.sleep(0.1)
            continue
        print("Sorry! Password not found!:(")
        
    
    
if file_zip == 'disco' and psswdlist == '5':
    hailEris()
        
elif file_zip == 'wtf' and psswdlist == 'disco':
    wtfDisco()
else:
    crack_zip(file_zip, psswdlist)

