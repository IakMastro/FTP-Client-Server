from ftplib import FTP 
from getpass import getpass

BLUE = '\033[1;34m'
RED = '\033[0;31m'
GREEN = '\033[1;32m'
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
	answer = input("$" + GREEN)
	print(DEFAULT, end='')
	if answer == "exit":
		break

	elif answer == "help":
		print(GREEN + "cd" + DEFAULT + ":\t  change the directory. Type the path of the new directory")
		print(GREEN + "ls" + DEFAULT + ":\t  print whatever is on the current directory")
		print(GREEN + "donwload" + DEFAULT + ": download a file from the current directory")
		print(GREEN + "send" + DEFAULT + ":\t  upload a file to the current directory")
		print(GREEN + "exit" + DEFAULT + ":\t  exit the program")

	elif answer == "ls":
		print(f"Current path: {ftp.pwd()}")
		for file in ftp.nlst():
			print(BLUE + file + DEFAULT)

	else:
		try: 
			answer = answer.split(' ', answer.find(' '))
			print(answer[0], answer[1])
			if answer[0] == "cd":
				ftp.cwd(answer[1])

		except:
			print(RED + "You have to give an argument as well" + DEFAULT)

print(BLUE + "Logging you out" + DEFAULT)
