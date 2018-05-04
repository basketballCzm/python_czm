# -*- coding: utf-8 -*- 
ind = 1
trainset = []
dataset = []
for line in open('wifi_data.txt','r').readlines():
	print ('line: ',ind)
	m = line.split('\t')
	for item in m:
		if item.replace('.','').replace('-','').replace('\n','').isdigit():
			if item.count('.')>0:
				print ('float:')
				print (isinstance(item,str))
				dataset.append(float(item))
			else:
				print ('int:')
				print (isinstance(item,str))
				dataset.append(int(item))
		else:
			print ('string:')
			print (isinstance(item,str))
			dataset.append(item)
	trainset.append(dataset)
	dataset = []
    #python里面的数组下表也是从0开始的
	print (trainset[ind-1])
	ind += 1
