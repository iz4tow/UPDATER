from ftplib import FTP
import sys
import os

def update_fase1(versione):
	##############################################APERTURA FILE INI IMPOSTAZIONI###############################################################
	file = open("update.ini", "r") 
	for riga in file:
		if riga.find("|")!=-1: #SOLO LE RIGHE DELLE IMPOSTAZIONI CHE CONTENGONO IL | VENGONO CONSIDERATE, GLI ALTRI SONO COMMENTI
			riga=riga.replace(" ","") #TOGLO GLI SPAZI BIANCHI
			impostazione,valore=riga.split("|"); #PRENDE IMPOSTAZIONE E VALORE IMPOSTAZIONE USANDO COME SEPARATORE I :
			if impostazione=='server':
				server=valore
				server=server.replace("\n","")
			if impostazione=='user':
				user=valore
				user=user.replace("\n","")
			if impostazione=='passw':
				passw=valore
				passw=passw.replace("\n","")
	##############################################FINE FILE INI IMPOSAZIONI###################################################################
	

	ftp = FTP(server)
	try:
		ftp.login(user,passw) 
	except:
		print ("UTENTE O PASSWORD ERRATA")
		return 2
	
	file = open("versione.txt",'wb')
	
	try:
		ftp.retrbinary('RETR versione.txt',file.write)
	except:
		print ("IMPOSSIBILE RECUPERARE ULTIMA VERSIONE")
		return 3
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
			print ("IMPOSSIBILE RECUPERARE ULTIMA VERSIONE UPDATE.EXE")
			return 3
		file.close()
		os.system("start update.exe")
		sys.exit(0)