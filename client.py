# client.py

import socket                   # Import socket module
import cv2
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60000                    # Reserve a port for your service.

s.connect(("127.0.0.1", port))
s.send(bytes("Done connection .","utf-8"))

with open('received.png', 'wb') as f:
    print ('file opened')
    print('receiving data...')
    while True:
        
        data = s.recv(70656)
        #print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()

print('The file was obtained successfully')

image_cv2= cv2.imread('received.png')
cv2.imshow("Image", image_cv2)
cv2.waitKey(5000)
cv2.destroyWindow("Image")
s.close()
print('connection closed')
