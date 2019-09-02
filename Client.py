from ftplib import FTP 
from getpass import getpass

BLUE = '\033[1;34m'
RED = '\033[0;31m'
DEFAULT = '\033[0m'

ftp = FTP('')
try:
	ftp.connect("192.168.1.9", 2000)
except:
	print(RED + "Error connection to server" + DEFAULT)
	exit()

username = input("Username: ")
password = getpass("Password: ")

try:
	ftp.login(username, password)
	ftp.encoding = 'utf-8'
except:
	print(RED + "Wrong username or password" + DEFAULT)
	exit()

print(BLUE + "Success!" + DEFAULT)