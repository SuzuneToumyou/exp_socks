#!/usr/bin/python3
# -*- coding: utf-8 -*
import socket

server_ip = "0.0.0.0"
server_port = 8080
listen_num = 5
buffer_size = 1024

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind((server_ip, server_port))
tcp_server.listen(listen_num)

while True:
    client,address = tcp_server.accept()
    #print(address)
    data = client.recv(buffer_size)
    #print(data)
    if (data[:3]==b"SET"):
        data2 = data[4:]    
        data2=data2.decode()
        
        data3 = []
        data3.append(data2.split(","))
    
        for i in range(0,7):
            print(data3[0][i])

        client.send(b"OKfarm!!")
    client.close()
