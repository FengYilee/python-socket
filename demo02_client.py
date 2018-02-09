#!usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:kevinlee 
@file: demo02_client.py 
@time: 2018/02/09 
"""
import socket, threading, time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('192.168.1.103', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))


def sendmsg(sock):
    while True:
        data = input()
        if data == 'bye':
            sock.send(b'bye')
            break
        sock.send(bytes(data.encode('utf-8')))


def readmsg(sock):
    while True:
        data = sock.recv(1024).decode('utf-8')
        if data == 'bye':
            break
        print(data)
    sock.close()


sendthread = threading.Thread(target=sendmsg, args=(s,))
readthread = threading.Thread(target=readmsg, args=(s,))

sendthread.start()
readthread.start()
