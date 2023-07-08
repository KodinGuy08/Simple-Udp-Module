# Simple-Udp-Module
A really simple, but helpful module to easily use UDP sockets.
## Usage/Examples

Simply call import the following module
```Python
from UDPServer import Server
```

Then define your method that will receive the message packet. Do note that that this method/function must have 2 parameters data and sender.

- Data is a bytes datatype.

- Sender is a tuple with the format (SENDER_IP, PORT_NUMBER).

- SENDER_IP is a string and PORT_NUMBER is an integer.

Here we defining a receiving funtion that will send the same message packet back to the sender.
```Python
def recv(data, sender):
    print("%s sent a packet: %s" % (str(data), str(sender)))
    
    server.writeData(data, sender)
```

Finally, we can initialise with 3 simple variables, respectively.
- The host IP
- The listening port number
- The receiving function

Don't forget to call "readData" otherwise you will not receive data.

```Python
server = Server("0.0.0.0", 4900, recv)
server.readData()
```

Full Example
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

