import socket
import sys

#read file
filename = 'file1.txt'
# client program using python
while True:
    try:
        s = socket.socket()
        ip = '192.168.43.162'
        port = 8500
        s.connect((ip,port))
        print("Successfully kconnected to ",ip)
        with open(filename,'r') as fd:
            str= fd.read(1024)
            s.sendall(bytes(filename,'utf-8'))
            print("Last Modified time",s.recv(1024))
            while(str):
                s.send(bytes(str,'utf-8'))
                str=fd.read(1024)	
                print(str)
        fd.close()	
        print("server 1 is closing")
        s.close()
        sys.exit(0)
    except:
        s1 = socket.socket()
        print("backup process")
        ip = '192.168.43.162'
        port = 8783
        s1.connect((ip,port))
        print("Successfully connected to ",ip)
        status="not ready"
        s1.send(bytes(status,'utf-8'))
        print("connecting to server2 for backup")
        #while True:
        #    bi = s1.recv(1024)
        #    if not bi:
         #       break
        #    print(bi)
        s1.close()
        break
s.close()
            