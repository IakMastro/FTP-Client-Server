from ftplib import FTP 
from getpass import getpass
from tqdm import tqdm
import os

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

print("commands: help, cd, ls, download, upload, exit")
while True:
	answer = input("$" + GREEN)
	ftp.voidcmd('TYPE i')
	print(DEFAULT, end='')

	if answer == "exit":
		break

	elif answer == "help":
		print(GREEN + "cd" + DEFAULT + ":\t  change the directory. Type the path of the new directory")
		print(GREEN + "ls" + DEFAULT + ":\t  print whatever is on the current directory")
		print(GREEN + "download" + DEFAULT + ": download a file from the current directory")
		print(GREEN + "upload" + DEFAULT + ":\t  upload a file to the current directory")
		print(GREEN + "exit" + DEFAULT + ":\t  exit the program")

	elif answer == "ls":
		print(f"Current path: {ftp.pwd()}")
		for file in ftp.nlst():
			print(BLUE + file + DEFAULT)

	else:
		try: 
			answer = answer.split(' ', 1)
			if answer[0] == "cd":
				try:
					ftp.cwd(answer[1])

				except:
					print(RED + "This directory doesn't exist" + DEFAULT)

			elif answer[0] == "download":
				try:
					with open(answer[1], 'wb') as file:
						print(BLUE + "Please wait while it's downloading" + DEFAULT)
						with tqdm(leave = False, desc = "Downloading", unit = "bits", unit_scale = True,
							total = ftp.size(file.name)) as tqdm_instance:
							def callback(data):
								tqdm_instance.update(len(data))
								file.write(data)
							ftp.retrbinary('RETR {}'.format(answer[1]), callback = callback)
						print(BLUE + "Finished the download" + DEFAULT)

				except:
					print(RED + "Couldn't download the file" + DEFAULT)

			elif answer[0] == "upload":
				try:
					with open(answer[1], "rb") as file:
						print(BLUE + "Please wait while it's uploading" + DEFAULT)
						with tqdm(leave = False, desc = "Uploading", unit = "bits", 
							total = os.path.getsize(file.name)) as tqdm_instance:
							ftp.storbinary(f"STOR {answer[1]}", file, 
								callback = lambda sent: tqdm_instance.update(len(sent)))
						print(BLUE + "Finished the upload" + DEFAULT)

				except:
					print(RED + "Couldn't upload the file" + DEFAULT)

		except:
			print(RED + "You have to give an argument as well" + DEFAULT)

print(BLUE + "Logging you out" + DEFAULT)
