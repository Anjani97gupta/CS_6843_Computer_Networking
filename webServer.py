#import socket module
from socket import *
import sys # library imported in order to terminate the program

def webServer(port=13331):
   
   serverSocket = socket(AF_INET, SOCK_STREAM)
   #Prepare a server socket
   serverSocket.bind(('',13331))
   serverSocket.listen(1)
   
   while True:

       #print('Ready to serve...')
       connectionSocket, addr = serverSocket.accept()
       try:
           message = connectionSocket.recv(1024)
           filename = message.split()[1]
           #opens the client requested file. 
           #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
           f = open(filename[1:]) #fill in start 
           outputdata = f.read()
           f.close()

           connectionSocket.send('HTTP/1.1 200 OK\r\n'.encode())  # http OK message
           #outputdata = b"Content-Type: text/html;\r\n"
           connectionSocket.send('\r\n'.encode())
           #Send the content of the requested file to the client
           for i in range(0, len(outputdata)):
               connectionSocket.send(outputdata[i].encode())
           connectionSocket.send("\r\n".encode())
           connectionSocket.close()

       except IOError:
           #Send response for file not found (404)
           connectionSocket.send('HTTP/1.1 404 not found \r\n'.encode())
           connectionSocket.close()

       except BrokenPipeError:
           break
           #Close client socket
  
   serverSocket.close()
   sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
   webServer(port=13331)
