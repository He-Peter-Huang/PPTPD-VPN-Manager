import os

def Main():
	while(True):	
		print("""

			1. Add VPN Users
			2. Check VPN Users
			3. Show Logged in VPN Users
			4. Edit VPN Users
			5. Check VPN Users Login History
			6. Check Inidivisual VPN Users Login History

			""")
		select=input("Please select the number:")
		if (select=="1"):
			clear()
			os.system("python3 /etc/pptp/adduser")
		if (select=="2"):
			clear()
			os.system("python3 /etc/pptp/checkuser")
		if (select=="3"):
			clear()
			os.system("last | grep still | grep ppp")
		if (select=="4"):
			clear()
			os.system("nano /etc/ppp/chap-secrets")
		if (select=="5"):
			clear()
			os.system("last |grep ppp")
		if (select=="6"):
			clear()
			os.system("python3 /etc/pptp/loginhistory")

def clear():
	os.system("clear")


clear()

print("""
  _____     _             __      _______  _   _    __  __                                   
 |  __ \   | |            \ \    / /  __ \| \ | |  |  \/  |                                  
 | |__) |__| |_ ___ _ __   \ \  / /| |__) |  \| |  | \  / | __ _ _ __   __ _  __ _  ___ _ __ 
 |  ___/ _ \ __/ _ \ '__|   \ \/ / |  ___/| . ` |  | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
 | |  |  __/ ||  __/ |       \  /  | |    | |\  |  | |  | | (_| | | | | (_| | (_| |  __/ |   
 |_|   \___|\__\___|_|        \/   |_|    |_| \_|  |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   
                                                                              __/ |          
                                                                             |___/             
""")


Main()
