import socket,sys,select,SocketServer
 
HOST = ''
PORT = 5001

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
					data = sk.recv(4096)
					if not data:
						break;
					else:
						sys.stdout.write(data)
						sys.stdout.write('Enter something bro: ')
						sys.stdout.flush()
				except:
					print "Error occured..possible server crashed"
					s.close()
			else: #user entered something
				s.send(sys.stdin.readline())
				sys.stdout.write('Enter something bro: ')
				sys.stdout.flush()

	except:
		s.close()
		print "\nClosing client. Bye!\n"
		break
