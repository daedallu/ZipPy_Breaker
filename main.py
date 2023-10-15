import zipfile as zfile
import numpy as np

def bruteForce_decryptZip(zip_file, password_list):
	#transform a txt list into a Python array
	df=np.loadtxt(password_list, dtype="str")
	for psswd in df:
		try:
			with zfile.ZipFile(zip_file) as zf:
				zf.extractall(pwd=psswd.encode())
				print(f"Senha encontrada: {psswd}")
				return
		except zfile.BadZipfile:
			print("Arquivo ZIP inválido.")
			return
		except RuntimeError:
			print(f"Senha não encontrada.")

		
bruteForce_decryptZip("breakme.zip","attacklist.txt")
