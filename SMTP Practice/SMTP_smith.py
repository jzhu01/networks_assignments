# q2_smtp_gmail.py
# Author: Jen Zhu
# Date: Sept 19, 2016

from socket import *
import base64

message = "\r\n I love computer networks!"
endMessage = "\r\n.\r\n"

recipient = "<jzhu@smith.edu>"
sender = "<jzhu@smith.edu>"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailServer = "smtp.smith.edu"
serverPort = 25

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((mailServer, serverPort))
recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
	print '220 reply not received from server.'

# Send HELO command and print server response.
heloCmd = 'HELO Alice\r\n'
clientSocket.send(heloCmd)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server.'

# Send MAIL FROM command and print server response.
mailFromCmd = 'MAIL FROM: ' + sender + '\r\n'
clientSocket.send(mailFromCmd)
recv2 = clientSocket.recv(1024)
print recv2
if recv2[:3] != '250':
    print 'mail from 250 reply not received from server.'

# Send RCPT TO command and print server response.
rcptToCmd = 'RCPT TO: ' + recipient + '\r\n'
clientSocket.send(rcptToCmd)
recv3 = clientSocket.recv(1024)
print recv3
if recv3[:3] != '250':
    print 'rcpt to 250 reply not received from server.'

# Send DATA command and print server response.
dataCmd = 'DATA\r\n'
clientSocket.send(dataCmd)
recv4 = clientSocket.recv(1024)
print recv4
if recv4[:3] != '250':
    print 'data 250 reply not received from server.'


# Message ends with a single period.
clientSocket.send(endMessage)
recv5 = clientSocket.recv(1024)
print recv5
if recv5[:3] != '250':
    print 'end msg 250 reply not received from server.'

# Send QUIT command and get server response.
quitCmd = 'Quit\r\n'
print(quitCmd)
clientSocket.send(quitCmd)
recv6 = clientSocket.recv(1024)
print recv6
if recv6[:3] != '250':
    print 'quit 250 reply not received from server.'

clientSocket.close()
