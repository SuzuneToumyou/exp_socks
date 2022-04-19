#!/usr/bin/python3
# -*- coding: utf-8 -*

import socket

server_ip = "192.168.0.1"
server_port = 80
listen_num = 5

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), server_port))  # IPとポート番号を指定します
s.listen(listen_num)

clientsocket, address = s.accept()
print(f"Connection from {address} has been established!")
clientsocket.send(bytes("SET:0,0,0,0,0,0,0", 'utf-8'))
clientsocket.close()
