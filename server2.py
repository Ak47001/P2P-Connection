# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 21:04:25 2019

@author: Admin
"""
import socket
import os
import time
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.43.162',8783))
s.listen(20)
c,addr = s.accept()
print("Connected sucesfully ",c,addr)
file2="file3.txt"
d=c.recv(1024).decode('utf-8')
if d=='okay':#copying the contents
    with open(file2,'w+') as f:
        while True:
            bi=c.recv(1024)
            if not bi:
                break
            print(bi)
            f.write(bi.decode('utf-8'))
        f.close()
    c.close()
else:#displaying the contents
    print("contents are:")
    with open(file2,"r") as f:
        for i in f.readlines():
            print(i)
        f.close()
    c.close()
            