# server.py

import socket                   # Import socket module
import cv2

port = 60000                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind (("127.0.0.1", port))           # Bind to the port
s.listen(5)                     # Now wait for client connection.

print ("Server listening....")

image = ('pic.png')
image_cv2= cv2.imread(image)

while True:
    conn, addr = s.accept()     # Establish connection with client.
    
    data = conn.recv(70656)
    print('Server received', repr(data))
    
    #image= cv2.imread('pic.png')
    #img_encode = cv2.imencode('.jpg', image)[1]
    filename=image
    f = open(filename,'rb')
    l = f.read(70656)
    while (l):
       conn.send(l)
       
       l = f.read(70656)
    f.close()

    print('Done sending')
    #conn.send('Thank you for connecting')
    conn.close()
    exit()
    
