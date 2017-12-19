# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 21:44:42 2017

@author: Pistachio
"""

import socket
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
html = ""
html = html.encode()
while (True):
    data = mysock.recv(20)
    if (len(data) < 1):
            break
    html += data
mysock.close()
print(html.decode())

#import socket
#
#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#mysock.connect(('data.pr4e.org', 80))
#cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
#mysock.send(cmd)
#
#while True:
#    data = mysock.recv(20)
#    if (len(data) < 1):
#        break
#    print(data.decode(),end='')
#    print('data type is',type(data))
#    print(type(data.decode()))
#
#mysock.close()
