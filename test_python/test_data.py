ind = 1
for line in open('data.txt','r').readlines():
	print 'line: ', ind
	ind += 1
	m = line.split('\t')
	for item in m:
		if item.replace('.','').replace('-','').replace('\n','').isdigit():
			if item.count('.')>0:
				print 'float: ',float(item)
			else:
				print 'integer: ',int(item)
		else:
			print 'string: ',item
import python_module
python_module.test()