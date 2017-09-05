# -*- coding: utf-8 -*-

import socket, logging

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('127.0.0.1', 9999))
except socket.error as e:	
	logging.exception(e)
else:
	print(s.recv(1024).decode('utf-8'))


s.send(input().encode('utf-8'))
print(s.recv(1024).decode('utf-8')) 


