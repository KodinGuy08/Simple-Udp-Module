# Simple-Udp-Module
A really simple, but helpful module to easily use UDP sockets.



## Usage/Examples

```Python
from UDPServer import Server

def recv(data, sender):
    print("%s sent a packet: %s" % (str(data), str(sender)))
    
    server.writeData(data, sender)

server = Server("0.0.0.0", 4900, recv)
server.readData()

while True:
    pass
```

