#!/usr/bin/python3
# -*- coding: utf-8 -*

import socket
import RPi.GPIO as GPIO

port_quant = 7
port_list=[17,18,22,23,24,25,27]

server_ip = "0.0.0.0"
server_port = 8080
listen_num = 5
buffer_size = 1024

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind((server_ip, server_port))
tcp_server.listen(listen_num)

GPIO.setmode(GPIO.BCM)

for i in range(0,port_quant):
    GPIO.setup(port_list[i], GPIO.OUT)

while True:

    client,address = tcp_server.accept()
    data = client.recv(buffer_size)
    #print (data)
    if (data[:3]==b"SET"):
        data2 = data[4:]
        data2=data2.decode()
        data2.rstrip('/x00')

        data3 = []
        data3.append(data2.split(","))

        for i in range(0,port_quant):
            #print (i)
            tmp=data3[0][i]

            if ("1" in tmp):
                GPIO.output(port_list[i], GPIO.HIGH)
                #print ('on')
                #print (port_list[i])
            elif("0" in tmp):
                GPIO.output(port_list[i], GPIO.LOW)
                #print ('off')
                #print (port_list[i])
            else :
                print ('error')

        client.send(b"OKfarm!!")
    client.close()
GPIO.cleanup()
