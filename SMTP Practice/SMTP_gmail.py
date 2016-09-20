# q2_smtp_gmail.py
# Author: Jen Zhu
# Date: Sept 19, 2016

import socket
import base64

message = "\r\n I love computer networks!"
endMessage = "\r\n.\r\n"

recipient = "<jzhu@smith.edu>"
sender = "<jennifer0zhu@gmail.com>"
username = "jennifer0zhu"
password = '********' # censored for privacy

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailServer = "smtp.gmail.com"
serverPort = 587

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket.socket()
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

# Request an encrypted connection
startTlsCmd = 'STARTTLS\r\n'
clientSocket.send(startTlsCmd)
tls_recv = clientSocket.recv(1024)
print tls_recv
if tls_recv[:3] != '220':
	print '220 reply not received from server'

# Encrypt the socket
ssl_clientSocket = socket.ssl(clientSocket)

# Send the AUTH LOGIN command and print server response.
authCmd = 'AUTH LOGIN\r\n'
ssl_clientSocket.write(authCmd)
auth_recv = ssl_clientSocket.read(1024)
print auth_recv
if auth_recv[:3] != '334':
	print '334 reply not received from server'

# Send username and print server response.
serverUsername = base64.b64encode(username) + '\r\n'
ssl_clientSocket.write(serverUsername)
serverUsername_recv = ssl_clientSocket.read(1024)
print serverUsername_recv
if serverUsername_recv[:3] != '334':
	print '334 reply not received from server'

# Send password and print server response.
serverPassword = base64.b64encode(password) + '\r\n'
ssl_clientSocket.write(serverPassword)
serverPassword_recv = ssl_clientSocket.read(1024)
print serverPassword_recv
if serverPassword_recv[:3] != '235':
	print '235 reply not received from server'

# Send MAIL FROM command and print server response.
mailFromCmd = 'MAIL FROM: ' + sender + '\r\n'
ssl_clientSocket.write(mailFromCmd)
recv2 = ssl_clientSocket.read(1024)
print recv2
if recv2[:3] != '250':
	print '250 reply not received from server.'

# Send RCPT TO command and print server response.
rcptToCmd = 'RCPT TO: ' + recipient + '\r\n'
ssl_clientSocket.write(rcptToCmd)
recv3 = ssl_clientSocket.read(1024)
print recv3
if recv3[:3] != '250':
	print '250 reply not received from server.'

# Send DATA command and print server response.
dataCmd = 'DATA\r\n'
ssl_clientSocket.write(dataCmd)
recv4 = ssl_clientSocket.read(1024)
print recv4
if recv4[:3] != '354':
	print '354 reply not received from server.'

# Send message data.
ssl_clientSocket.write(message)

# Message ends with a single period.
ssl_clientSocket.write(endMessage)
recv5 = ssl_clientSocket.read(1024)
print recv5
if recv5[:3] != '250':
	print '250 reply not received from server.'

# Send QUIT command and get server response.
quitCmd = 'QUIT\r\n'
ssl_clientSocket.write(quitCmd)
recv6 = ssl_clientSocket.read(1024)
print recv6
if recv6[:3] != '221':
	print '221 reply not received from server.'

clientSocket.close()
