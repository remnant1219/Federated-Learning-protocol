import socket
import os
import time

class Client:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connect_to_server()

    def connect_to_server(self):
        self.target_ip = input('Enter ip --> ')
        self.target_port = input('Enter port --> ')

        self.s.connect((self.target_ip,int(self.target_port)))

        self.main()

    def reconnect(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.connect((self.target_ip,int(self.target_port)))

    def main(self):
        t1 = time.time()
        mea_number = 10
        for i in range(0,mea_number):
            file_name = "vehcile.crt"
            self.s.send(file_name.encode())

            confirmation = self.s.recv(1024)
            print(confirmation)
            if "error" in confirmation:
                print("Certificate validation is failed: %s" %(confirmation))
                
            elif "OK" in confirmation:
                print("Certificate validation")
                 
            self.s.shutdown(socket.SHUT_RDWR)
            self.s.close()
            self.reconnect()
        t2 = time.time()
        time_taken = t2 - t1
        print(time_taken)    

            
                
client = Client()
