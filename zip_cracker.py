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
if file_zip == 'man' and psswdlist == 'zip_cracker':
	mssg = 'WELCOME TO ZIP CRACKER!/nHow to use:/nCommandline: ./zip_cracker [file.zip] [password_list.txt]/n'
	print(mssg)

if file_zip == 'disco' and psswdlist == '5':
        while 2 < 3:
            print("HAIL ERIS!!!")
            time.sleep(0.5)
            
if file_zip == 'wtf' and psswdlist == 'disco':
        wb.open("https://www.principiadiscordia.com/downloads/Principia%20Discordia%20(Wholly%201st%20Edition).pdf", autoraise=True)    
                
            
def crack_zip(zipFile, list_pass):
    
    df = np.loadtxt(list_pass, dtype="str")
    
    for pswd in df:
        try:
            with ZipFile(zipFile) as zf:
                zf.extractall(pwd=pswd.encode())
                print(f'SUCCESS! Password is:{pswd}')
                time.sleep(0.1)
                return
        except BadZipfile:
            print("Sorry! File not found! :(")
            time.sleep(0.1)
            return
        except RuntimeError:
            print(f'Incorrect password:{pswd}')
            time.sleep(0.1)
            continue
        print("Sorry! Password not found!:(")
    
    


crack_zip(file_zip, psswdlist)

