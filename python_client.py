# -*- coding: utf-8 -*- 
# you should have a uniform encoding format for the server and client 'utf-8'
import socket
import json
import time
'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('120.79.128.233',6666))
print(s.recv(1024).decode('utf-8'))
for data in [b'陈自民',b'sy',b'tt']:
	s.send(data)
	print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
'''
'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('120.79.128.233',6666))
print(s.recv(1024).decode('utf-8'))
d = {'陈自民':100, 'sy':99}
data = json.dumps(d)
b = data.encode()
s.send(b)
print(s.recv(1024).decode('utf-8'))
time.sleep(2)
s.send(b'exit')
s.close()
'''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('120.79.128.233',6666))
d = {'AP1':-51, 'AP2':-68, 'AP3':-66 , 'AP4':-75 , 'AP5':-74 }
data = json.dumps(d)
b = data.encode()
s.send(b)
print(s.recv(1024).decode('utf-8'))
time.sleep(2)
s.send(b'exit')
s.close()























'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.sina.com.cn',80))

s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

buffer = []
while True:
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data = b''.join(buffer)

s.close()

header,html = data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
with open('sina.html','wb') as f:
	f.write(html)
'''