import socket
from random import *
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
ans = randint(1,100)
print("magic num:", ans)

while True:

    data, addr = sock.recvfrom(1024)
    guess = int(data.decode())
    if(guess<ans):
        print("HIGHER")
        sock.sendto("HIGHER".encode(),addr)
        
    if(guess>ans):
        print("LOWER")
        sock.sendto("LOWER".encode(),addr)
        
    if(guess == ans):
        print("CORRECT!!")
        sock.sendto("correct".encode(),addr)
