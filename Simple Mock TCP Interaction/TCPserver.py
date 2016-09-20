# TCPserver.py
# Author: Jen Zhu
# Date: Sept 19, 2016

from socket import *
from pathlib import Path
import sys

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready is ready to receive")
while True:
    connectionSocket, addr = serverSocket.accept()
    httpRequest = connectionSocket.recv(1024).decode()
    stopParse = httpRequest.find("HTTP/1.1")
    beginParse = httpRequest.find("GET") + 14
    pathToLocate = "./"+httpRequest[beginParse:stopParse]
    #print(pathToLocate) #simply for debugging
    file = Path(pathToLocate)
    if file.is_file():
        #print(file)    #debugging
        htmlfile = open(pathToLocate, "rt")
        htmltxt = htmlfile.read()
        responseMessage = "HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\n"+htmltxt
        connectionSocket.send(responseMessage.encode())
        print("Closing connection...")
        connectionSocket.close()
    else:
        responseMessage = "HTTP/1.1 404 Not Found\nConnection: close\n"
        connectionSocket.send(responseMessage.encode())
        print("Closing connection...")
        connectionSocket.close()

    sys.exit(0)
