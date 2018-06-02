# -*- coding: utf-8 -*- 
import operator

trainingSet = []
def loadDataset(filename, trainingSet=[]):
	dataset = []
	for line in open(filename,'r').readlines():
		m = line.split(' ')
		for item in m:
			if item.replace('.','').replace('-','').replace('\n','').isdigit():
				if item.count('.')>0:
					dataset.append(float(item))
				else:
					dataset.append(item)
					#dataset.append(int(item))
			else:
				dataset.append(item)
		trainingSet.append(dataset)
		dataset = []

def main():
	loadDataset('25.txt',trainingSet)
	trainingSet.sort(key=operator.itemgetter(0))
	for x in range(len(trainingSet)):
		print(trainingSet[x])

main()
