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
password = getpass()

try:
	ftp.login(username, password)
	ftp.encoding = 'utf-8'
except:
	print(RED + "Wrong username or password" + DEFAULT)
	exit()

print(BLUE + "Connection successful!" + DEFAULT)

print("commands: help, cd, ls, download, send, exit")
while True:
	answer = input("$")
	if answer == "exit":
		break

	elif answer == "help":
		print("cd: change the directory. Type the path of the new directory")
		print("ls: print whatever is on the current directory")
		print("donwload: download a file from the current directory")
		print("send: upload a file to the current directory")
		print("exit: exit the program")

	elif answer == "ls":
		for file in ftp.nlst():
			print(BLUE + file + DEFAULT)

	else: 
		whitespace = answer.find(' ')
		answer = answer.split(" ", 1)
		print(answer)

print(BLUE + "Logging you out" + DEFAULT)
