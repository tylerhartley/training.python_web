import socket
import sys

# Create a TCP/IP socket
client = socket.socket(2,1,0)
# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', 50000)
#server_address = ('208.85.148.104',50000)
#server_address = ('block647050-tha.blueboxgrid.com',50000)

client.connect(server_address)

try:
    # Send data
    message = raw_input("Enter two numbers separated by a space: ")
    #message = '2 5'
    out = client.sendall(message)
    response = client.recv(1024)
    # print the response
    print response
    
finally:
    # close the socket to clean up
    client.close()
    

