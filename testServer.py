#!/usr/bin/python
#This will be the main server code..GG
#Authors: Yash and Chinmay
#Reviewers: Dhaval and Ashutosh

import sys
import socket
import SocketServer
import select

PORT = 9001
BUF_SIZE = 4096
HOST = '' #Leaving it blank means it applies to all avaiable hardware interfaces...
NUMBER_OF_CLIENTS = 1
CONNECTED_CLIENTS = []


#From python documents..server goes through 4 steps
#(1)socket(),bind(),listen(),accept()
#Create the var to hold the socket stream
main_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
main_socket.bind((HOST,PORT))
main_socket.listen(NUMBER_OF_CLIENTS) #1 represents the number of clients it listens to

#Create an arraylist to hold all of the connections
CONNECTED_CLIENTS.append(main_socket)

#Get a list of connections and check validity
readable,writeable,error = select.select(CONNECTED_CLIENTS,[],[])

#go through all of the readable connections

for read in readable:
    #Accept the client connection
    connection,address = main_socket.accept()
    print 'Connected dog to address:',address
    while 1:
        data = connection.recv(1024)
        if not data: continue
        connection.sendall(data)
