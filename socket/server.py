# -*- coding: utf-8 -*-

import socket, time, threading, sys

def tcplink(sock, addr):
	print('Accept new connection from %s:%s...' % addr)
	sock.send(b'Welcome!')

	while True:
		data = sock.recv(1024)
		time.sleep(1)

		if not data or data.decode('utf-8') == 'exit':
			break
		sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
	sock.close()
	print('Connection from %s:%s closed.' % addr)



try:
	# 创建socket，AF_INET指定使用IPv4协议,SOCK_STREAM指定使用面向流的TCP协议
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# 监听端口
	s.bind(('127.0.0.1', 9999))
except socket.error as e:
	sys.exit()
else:
	# 开始监听，指定等待连接的最大数量
	s.listen(5)
	print('waiting for connection...')


while True:
	sock, addr = s.accept()	# 接受一个新连接
	# 创建新线程来处理TCP连接:
	t = threading.Thread(target = tcplink, args = (sock, addr))
	t.start()
