import socket
import time


class sending:

    def __init__(self) -> None:
        self.HEADER = 64
        PORT = 5050
        SERVER = "192.168.43.194"
        ADDR = (SERVER,PORT)
        FORMAT = 'utf-8'
        DISCONNECT_MESSAGE = "!DISCONNECT"
        client  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(ADDR)
        f = open('chain.txt',"r")
        e= open('chain.txt',"r")
        a=len(e.readlines())
        e.close()
        print(a)
        b=0
        for i in f:
            if(b<a):
                print(i)
                j= str(i)
                message = j.encode(FORMAT)
                msg_length = len(message)
                #print(msg_length)
                send_length = str(msg_length).encode(FORMAT)
                send_length += b' ' * (self.HEADER - len(send_length))
                client.send(send_length)
                client.send(message)
                print(client.recv(2048).decode(FORMAT))
                b=b+1
            else:
                message = ("!DISCONNECT").encode(FORMAT)
                msg_length = len(message)
                #print(msg_length)
                send_length = str(msg_length).encode(FORMAT)
                send_length += b' ' * (self.HEADER - len(send_length))
                client.send(send_length)
                client.send(message)
                print(client.recv(2048).decode(FORMAT))

        

 
    #print(data)

#ver()
#time.sleep(2)

#send("!DISCONNECT")