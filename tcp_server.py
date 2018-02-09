#!usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:kevinlee 
@file: tcp_server.py 
@time: 2018/02/09 
"""
import socket, time, threading

inputs = []


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data.decode('utf-8') == 'bye':
            sock.send(b'bye')
            inputs.remove(sock)
            break
        for other in inputs:
            other.send(b'%s say: %s' % (str(addr[0]).encode('utf-8'), str(data).encode('utf-8')))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 9999))
s.listen(5)
while True:
    sock, addr = s.accept()
    inputs.append(sock)
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
