# import socket module
from socket import *
import sys  # library imported in order to terminate the program
def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Prepare a server socket
    serverSocket.bind(('', port))
    serverSocket.listen(1)
    while True:
        connectionSocket, addr = serverSocket.accept()
            message = connectionSocket.recv(1024)
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()
            f.close()
            connectionSocket.send('HTTP/1.1 200 OK\r\n'.encode())
            # outputdata = b"Content-Type: text/html;\r\n"
            connectionSocket.send('\r\n'.encode())
            # Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
        except IOError:
            connectionSocket.send('HTTP/1.1 404 not found \r\n'.encode())
            connectionSocket.close()
        except BrokenPipeError:
            break
            # Close client socket
    # Commenting out the below, as its technically not required and some students have moved it erroneously in the While loop. DO NOT DO THAT OR YOURE GONNA HAVE A BAD TIME.
    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data
if __name__ == "__main__":
    webServer(port=13331)
