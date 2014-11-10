import socket

HOST = ''
PORT = 9001

#According to docs the client sequence is
#1)socket(),connect(),
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('Hello, world')
data = s.recv(1024)
s.close()
print 'Received', repr(data)
