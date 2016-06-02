import os
import sys
import getpass
import random
count=0
userlist = []
autopassword=0
def clear():
	os.system("clear")
def adduser():
	global userlist
	global name
	global password
	global targetusertoadd
	global count
	command=("'"+name+"             "+"pptpd"+"             "+password+"        "+"*"+"'")
	os.system("echo "+command+" >> /etc/ppp/chap-secrets")
	userlist.append(name)
	if (autopassword==1):
		userlist.append(password)
	count=count+1
	clear()

def logdown():
	global name
	global password
	global targetusertoadd
	global autopassword
	print("Adding user",count+1,"of",targetusertoadd)
	name=input("Username:")
	if (name==''):
		print("Username can not be blank, please try again!")
		logdown()
	if (autopassword==0):
		password=getpass.getpass('Password (Press Enter to Auto Generate Password):')
	if (autopassword==1):
		genpassword()
	if (password==''):
		genpassword()
		autopassword=1
	else:
		if (autopassword==0):
			retypepassword=getpass.getpass('Retype Password:')

			if (retypepassword!=password):
				clear()
				print("Your passwords does not match, please try again!")
				logdown()
def batchadd():
	global targetusertoadd
	targetusertoadd=int(input("Number of users to add:"))
def sucess():
	global userlist
	global autopassword
	print("Users Add Sucess!")
	if (autopassword==1):
		print("Username and Auto Generated Password Are:")
		print(userlist)
	else:
		print("Users that were sucessfully added:",userlist)
	print("Total User Added:",count)
	

def genpassword():
	global count
	global password
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	pw_length = 8
	mypw = ""

	for i in range(pw_length):
	    next_index = random.randrange(len(alphabet))
	    mypw = mypw + alphabet[next_index]

	# replace 1 or 2 characters with a number
	for i in range(random.randrange(1,3)):
	    replace_index = random.randrange(len(mypw)//2)
	    mypw = mypw[0:replace_index] + str(random.randrange(10)) + mypw[replace_index+1:]

	# replace 1 or 2 letters with an uppercase letter
	for i in range(random.randrange(1,3)):
	    replace_index = random.randrange(len(mypw)//2,len(mypw))
	    password = mypw[0:replace_index] + mypw[replace_index].upper() + mypw[replace_index+1:]
	    

	
	

clear()
batchadd()
clear()
while (count<targetusertoadd):
	logdown()
	adduser()
sucess()
