import socket
import threading
import time
import json

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#resolve the port be occuped for four minutes
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('172.18.39.19',6666))
s.listen(5)
print('waiting for connection ...')

def tcplink(sock, addr):
	print("Accept new connection from %s:%s" % addr)
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8') == 'exit':
			break

		d = json.loads(data)
		L = d

		print (L)
		sendData = (json.dumps(L)+'\n').encode('utf-8')
		sock.send(sendData)
	sock.close()
	print('Connection from %s:%s closed ' % addr)

while True:
	sock, addr = s.accept()
	#create new thread to deal with TCP connection
	t = threading.Thread(target=tcplink, args=(sock, addr))
	t.start()
