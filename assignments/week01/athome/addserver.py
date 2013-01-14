import socket
import sys

# Create a TCP/IP socket
aserver = socket.socket( 2, 1, 0)

# Bind the socket to the port
server_address = ('127.0.0.1', 50000)
aserver.bind(server_address)
# Listen for incoming connections
aserver.listen(2) #listen(num) is the number of sequential connections allowed

while True:
# Wait for a connection
    con, cli = aserver.accept()
    
    try:
        # Receive the data and send it back
        msg = con.recv(1024)
        
        a, b = (int(msg.split()[0]), int(msg.split()[1]))
        thesum = str(a + b)
        out = con.sendall(thesum)
    
    finally:
        # Clean up the connection
        con.close()
        