import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
var = int()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for i in range(1,11):
    a = input("Enter guess "+ str(i)+": ")
    sock.sendto(a.encode(),(UDP_IP,UDP_PORT))
    var=i
    data, addr = sock.recvfrom(1024)
    if(data.decode()=="correct"):
        break
    else:
    	print(data.decode())
   
if(var==10):
    print("Better Luck Next Time")
else:
    print("well done!")
