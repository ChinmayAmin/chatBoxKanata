import socket,sys,select,SocketServer
 
HOST = ''
PORT = 5001
display_name = ''
count = 0

#According to docs the client sequence is
#1)socket(),connect(),
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while 1:
	
	try:
		#since we need to listen to two things...1)user input 2)server sending messages
		list = [sys.stdin,s]
	
		#same thing as server
		read,write,error = select.select(list,[],[])
	
		for sk in read:
			if sk == s: #server sending messages
				try:
                                        if count == 0:
                                                #first time client connected
                                                data = sk.recv(4096)
                                                if not data:
                                                        break;
                                                else:
                                                        sys.stdout.write(data)
                                                        #somehow putting the rstrip works!
                                                        display_name = sys.stdin.readline().rstrip('\n')
                                                        sys.stdout.write("\r%s: " % display_name)
                                                        sys.stdout.flush()
                                                        s.send(display_name)

                                                        count = 1
                                        else:
                                                data = sk.recv(4096)
                                                if not data:
                                                        break;
                                                else:
                                                        sys.stdout.write(data)
                                                        sys.stdout.write("\r%s: " % display_name)
                                                        sys.stdout.flush()
				except:
					print "Error occured..possible server crashed"
					s.close()
			else: #user entered something
				s.send(sys.stdin.readline())
				sys.stdout.write("\r%s: " % display_name)
				sys.stdout.flush()

	except:
		s.close()
		print "\nClosing client. Bye!\n"
		break
