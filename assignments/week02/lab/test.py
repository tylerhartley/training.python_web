    #!/usr/bin/env python

import socket 
import email, os, time

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
   
xx = '''
<html>
    <body>
        <h1>This is a header</h1>
        <p>
        and this is some regular text
        </p>
        <p>
        and some more
        <img src="http://localhost:50000/Sample_Scene_Balls.jpg" width="300" height="200">
        </p>
    </body>
</html>
'''
    
while True: # keep looking for new connections forever
    client, address = s.accept() # look for a connection
    
    try:
        data = client.recv(size)

        
        if data: # if the connection was closed there would be no data
            #print data, '\r\n'
            print xx
            client.send(xx) 
            client.close()
        
    except:
        time.sleep(0.1)
        


#<img src="http://localhost/balls.jpg" alt="balls" width="304" height="228">