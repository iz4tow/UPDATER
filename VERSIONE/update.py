import time
from ftplib import FTP
import sys
import os

ftp = FTP('127.0.0.1')
ftp.login("prova","prova") 
file = open("updatabile.exe",'wb')
ftp.retrbinary('RETR updatabile.exe',file.write)
file.close()
#os.system("updatabile.exe")
sys.exit(0)
