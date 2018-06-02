# -*- coding: utf-8 -*- 
import csv
import math
import operator
import socket
import threading
import time
import json
#使用正则表达式去解决字符串的匹配问题
import re

trainingSet = []
wifiNum = 8

#加载数据
def loadDataset(filename, trainingSet=[]):
	dataset = []
	for line in open(filename,'r').readlines():
		m = line.split('\t')
		for item in m:
			#isdigit is only include number. it will return true
			if item.replace('.','').replace('-','').replace('\n','').isdigit():
				if item.count('.')>0:
					dataset.append(float(item))
				else:
					dataset.append(int(item))
			else:
				dataset.append(item)
		trainingSet.append(dataset)
		dataset = []

'''
def loadDataset(filename, trainingSet=[]):
	with open(filename,'rb') as csvfile:
		lines = csv.reader(csvfile)
		dataset = list(lines)
		for x in range(len(dataset) - 1):
			m = lines.split('\t')
			for item in m:
				dataset[x][y] = float(dataset[x][y])  
			trainingSet.append(dataset[x])
'''
#计算欧式距离的函数
def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)

def changeZero(L):
	for x in range(len(L)-1):
		if L[x] == 0:
			L[x] = -100

def changeBack(L):
	for x in range(len(L)-1):
		if L[x] == -100:
			L[x] = 0

#得到K个最近邻的数据信号组
def getNeighbors(trainingSet, testInstance, k):
	distance = []
	length = len(testInstance) - 1
	for x in range(len(trainingSet)):
		'''
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		#这里相当于是添加了很多元组，然后每个元组中又存在一个list和dist
		distance.append((trainingSet[x], dist))
		'''
		changeZero(trainingSet[x])
		changeZero(testInstance)
		#对比最强的AP站点信号
		if trainingSet[x].index(max(trainingSet[x][0:8])) == testInstance.index(max(testInstance[0:8])):
			changeBack(trainingSet[x])
			changeBack(testInstance)
			dist = euclideanDistance(testInstance, trainingSet[x], length)
			#这里相当于是添加了很多元组，然后每个元组中又存在一个list和dist
			distance.append((trainingSet[x], dist))
		else:
			changeBack(trainingSet[x])
			changeBack(testInstance)
			distance.append((trainingSet[x], float("inf")))
	distance.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distance[x][0])
	'''
	sumX = 0
	sumY = 0
	for x in range(k):
		sumX = sumX + int(neighbors[x][-2])
		sumY = sumY + int(neighbors[x][-1])
	neighbors[0][-2] = sumX
	neighbors[0][-1] = sumY
	'''
	return neighbors

#对数据K组数据进行数据处理
def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1),
		reverse=True)
	return sortedVotes[0][0]

def tcplink(sock, addr):
	print('Accept new connection from %s:%s' % addr)
	while True:
		data = sock.recv(1024)
		print('receive data success!')
		#change json to dictionary
		d = json.loads(data.decode('utf-8'))
		print('json load data success!')
		locationSet = []
		for k in d:
			locationSet.append(d[k])
		print ('locationSet:',locationSet)
		#time.sleep(1)
		#locationSet = re.finall(r'\-?\d+\.?\d*',data)
		resultSet = getNeighbors(trainingSet, locationSet, 1)
		print ('resultSet:',resultSet)
		sendDict = {} 
		sendDict['x'] = resultSet[0][-2]
		sendDict['y'] = resultSet[0][-1]
		print ('sendDict:',sendDict)
		# json.dumps(dict) is a str. need to use encode() to byte
		# bug 这里是根据客户端的readLine的写法添加的'\n'
		sendData = (json.dumps(sendDict)+'\n').encode('utf-8')
		sock.send(sendData)
		print ("service send Message is success!")
	sock.close()
	print('Connection from %s:%s closed ' % addr)

def serviceInit(address, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind((address, port))
	s.listen(5)
	print ('waiting for connection...')
	while True:
		sock, addr = s.accept()
		#create a new thread to deal with the TCP connection
		t = threading.Thread(target=tcplink, args=(sock, addr))
		t.start()


def main():
	loadDataset('wifi_data_12.txt',trainingSet)
	serviceInit('172.18.39.19',6666)
main()