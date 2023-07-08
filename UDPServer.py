import Thread
import socket
import base64
import zlib

class Server:
    def __init__(self, HOST, PORT, func):
        self.host = HOST
        self.port = PORT
        
        self.ds = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.ds.bind((HOST, PORT))

        self.func = func

        self.status = True
        self.thread = Thread.Thread("Socket Thread", self.readData)
        self.thread.start()

        self.compress = False

    def writeData(self, data, tar):
        if self.compress:
            data = zlib.compress(data)
        self.ds.sendto(data, tar)

    def readData(self, buff_size=5000):
        print("Receiving data!")
        
        self.status = True
    
        while self.status:
            data, addr = self.ds.recvfrom(buff_size)

            try:
                if self.compress:
                    self.func(zlib.decompress(data), addr)
                else:
                    self.func(data, addr)
            except Exception as e:
                print(e)
                print(data)
                
        print("No longer receiving messages.")
                
    def stop(self):
        print("Ending socket...")
        self.status = False
        
