
import socket
import os
import time
import signal
import sys
#signal.signal(signal.SIGINT,SigHandler)
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.43.162',8500))
s.listen(5)
c,addr = s.accept()
print("Connected sucesfully ",c,addr)
file1= c.recv(1024).decode('utf-8')
print(file1)
file2="file2.txt"
with open(file2,'w+') as f:
	c.sendall(bytes(time.ctime(os.path.getmtime(file1)),'utf-8'))
	while True:
		bi = c.recv(1024)
		if not bi:
			break
		print(bi)
		f.write(bi.decode('utf-8'))
	f.close()
c.close()
s1= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip='192.168.43.100 '
port=8783
s1.connect((ip,port))
status="okay"
s1.send(bytes(status,'utf-8'))
with open(file2,'r') as fd:
	str = fd.read(1024)
	while(str):
		s1.sendall(bytes(str,'utf-8'))
		str=fd.read(1024)	
fd.close()
s1.close()
