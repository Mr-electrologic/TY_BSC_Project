import socket
import threading


class server_start:

    HEADER = 64
    PORT = 5050
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "!DISCONNECT"

    def __init__(self) -> None:   
        
        
        # cmd command ipconfig
        #SERVER = "192.168.43.194"
        SERVER =socket.gethostbyname(socket.gethostname())
        print(SERVER)
        #SERVER = socket.gethostbyname(socket.gethostbyname())
        ADDR = (SERVER,self.PORT)
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(ADDR)
        server.listen()
        print(f"[LISTENING] Server is listening on {SERVER}")
        while True:
            conn, addr= server.accept()
            thread = threading.Thread(target=self.handle_client , args=(self,conn,addr))
            thread.start()

    

    def handle_client(self,conn, addr):
        print(f"[new connection] {addr} connected..")
        connected = True
        f= open("data.txt", "w")
        while connected:
            msg_length = conn.recv(self.HEADER).decode(self.FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(self.FORMAT)
                print(f"[{addr}]{msg}")
                if(msg != self.DISCONNECT_MESSAGE ):
                    f.write(msg)
            if msg == self.DISCONNECT_MESSAGE:
                connected = False
                print(f"[{addr}]{msg}")
            
            conn.send("msg received".encode(self.FORMAT))
        
            #print(f"[ACTIVE CONNECTIONS]{threading.activeCount()}")

    
