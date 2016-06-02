import os

username=input("What Username Do You Want To Check?")
command="grep '"+username+"' /etc/ppp/chap-secrets"
os.system(command)
