#!/usr/bin/python
#This will be the main server code..GG
#Authors: Yash and Chinmay
#Reviewers: Dhaval and Ashutosh

import sys
import socket
import SocketServer
import select

PORT = 5001
BUF_SIZE = 4096
HOST = '' #Leaving it blank means it applies to all avaiable hardware interfaces...
NUMBER_OF_CLIENTS = 5
CONNECTED_CLIENTS = []
ccount = 0;

def send_to_all(sock,message):
	#go through all of the client list
	for sk in CONNECTED_CLIENTS:
		if sk != main_socket and sk != sock:
			sk.send(message)

#From python documents..server goes through 4 steps
#(1)socket(),bind(),listen(),accept()
#Create the var to hold the socket stream

main_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
main_socket.bind((HOST,PORT))
main_socket.listen(NUMBER_OF_CLIENTS) #represents the number of clients it listens to

#Create an arraylist to hold all of the connections
CONNECTED_CLIENTS.append(main_socket)

print "started on port 5001 GG\n"

while 1:

    #go through all of the readable connections
    #print "Right before going into the read loop.."

    readable,writeable,error = select.select(CONNECTED_CLIENTS,[],[])

    #print "Right after select.select"

    for read in readable:

	if read == main_socket:
		#when a client connects for the first time
		#keep adding to connected_client list since more conncted
		newClient,add = main_socket.accept()
		CONNECTED_CLIENTS.append(newClient)
		ccount = ccount + 1
		print 'Client number' + str(ccount) + ' connected'
	
		#only need to send the welcome message to new clients..
		newClient.send("Welcome to kanata chat box!\n")
	elif read == sys.stdin:
		#input from server side...for convinience
		print "WHAT YOU DOING BRO\n"
	else:
		#data from client
		data = read.recv(1024)
		send_to_all(read,data)
main_socket.close()
