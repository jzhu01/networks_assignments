# TCPclient.py
# Author: Jen Zhu
# Date: Sept 19, 2016

from socket import *
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
htmlfile = input("Enter a Path to HTML File: ")
httpRequest = "GET "+ htmlfile + "HTTP/1.1\nHost: "+serverName+"\nConnection: close\n"
print(httpRequest)
clientSocket.send(httpRequest.encode())
modifiedSentence = clientSocket.recv(1024)
print("From Server: ", modifiedSentence.decode())
clientSocket.close()
