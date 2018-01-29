import time
from ftplib import FTP
import sys
import os

versione="2.0"
print ("Versione attuale: "+versione)

try:
	ftp = FTP('127.0.0.1')
	ftp.login("prova","prova") 
	file = open("versione.txt",'wb')
except:
	errore_bdi=20
try:
	ftp.retrbinary('RETR versione.txt',file.write)
except:
	errore_bdi=20
file.close()
file = open("versione.txt",'r')
versione_att=str(file.read()) #ritorna solo la riga 1
riga,versione_att=versione_att.split("\n")
file.close()
os.remove("versione.txt")
if versione==versione_att:
	print ("IDENTICHE")
else:
	print ("DIVERSE")
	file = open("update.exe",'wb')
	try:
		ftp.retrbinary('RETR update.exe',file.write)
	except:
		errore_bdi=20
	file.close()
	os.system("start update.exe")
	sys.exit(0)
