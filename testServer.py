#!/usr/bin/python
#This will be the main server code..GG
#Authors: Yash and Chinmay
#Reviewers: Dhaval and Ashutosh

import sys
import socket
import SocketServer

PORT = 9001
BUF_SIZE = 4096
HOST = '' #Leaving it blank means it applies to all avaiable hardware interfaces...

#From python documents..server goes through 4 steps
#(1)socket(),bind(),listen(),accept()
#Create the var to hold the socket stream
main_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
main_socket.bind((HOST,PORT))
main_socket.listen(1) #1 represents the number of clients it listens to

#Accept the client connection
connection,address = main_socket.accept()

print 'Connected dog to address:',address

while 1:
    data = connection.recv(1024)
    if not data: break
    connection.sendall(data)
connection.close()
