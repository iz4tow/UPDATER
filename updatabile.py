import time
from ftplib import FTP
import sys
import os
from update_lib import update_fase1

versione="3.0"
print ("Versione attuale: "+versione)

update_fase1(versione)

print ("VERSIONE SOFTWARE: "+versione)