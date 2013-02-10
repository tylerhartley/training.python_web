#!/usr/bin/env python

import socket 
import email, os

host = '' # listen on all connections (WiFi, etc) 
port = 50000 
backlog = 5 # how many connections can we stack up
size = 1024 # number of bytes to receive at once

## create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# set an option to tell the OS to re-use the socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# the bind makes it a server
s.bind( (host,port) ) 
s.listen(backlog) 

def ok_response(body):
    return ( "HTTP/1.1 200 OK\r\n"
           + "Content-Type: text/html\r\n" 
           + "Date: %s\r\n"%(email.Utils.formatdate())
           + "\r\n"
           +  body         )


def parse_request(request):
    line1 = request.split('\r\n')[0].split()
    requesttype = line1[0]
    uri = line1[1]
    return requesttype, uri

def resolve_uri(uri):
    #strip any leading /
    if uri.startswith('/'): uri = uri[1:]
    #if directory
    if os.path.isdir(uri):
        list_content = os.listdir(uri)
        return ok_response('\r\n'.join(list_content))
    #if a file
    #if not found
    
    else: raise ValueError, 'URI not found'
    
    
while True: # keep looking for new connections forever
    client, address = s.accept() # look for a connection
    data = client.recv(size)
    req, uri = parse_request(data)
    
    print req, uri

    if req != 'GET':
        raise ValueError, "The request was not of type GET"
    
    if data: # if the connection was closed there would be no data
        print data, '\r\n'
        client.send(resolve_uri(uri)) 
        client.close()
        
        
        
