# -*- coding: utf-8 -*-
import string 
our_str = 'hello world'

new_str = our_str.replace('world','czm')
print new_str

our_str = 'hello you,you and you!'
new_str = our_str.replace('you','me',1)
print new_str
new_str = our_str.replace('you','me',2)
print new_str
new_str = our_str.replace('you','me',3)
print new_str

#change what to byte
print 'ABC'.encode('ascii')
#print b'中文'.encode('utf-8')
#print '中文'.encode('utf-8',errors = 'ignore')
#print '中文'.encode('ascii')

#change byte to what
print b'ABC'.decode('ascii')
print b'ABC'.decode('utf-8')
print b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

L = [['Apple', 'Google', 'Microsoft'],
['Java', 'Python', 'Ruby', 'PHP'],
['Adam', 'Bart', 'Lisa']]
print L[0][0]
print L[1][1]
print L[2][2]

L[0][0] = 'oppo'
print L[0][0]

#tuple change or no change is vaule to think thing.
Lt = (['Apple', 'Google', 'Microsoft'],
['Java', 'Python', 'Ruby', 'PHP'],
['Adam', 'Bart', 'Lisa'])

Lt[0][0] = 'oppo'
print Lt[0][0]

# range(sum) provice the number from 0 - sum-1
sum = 0
for x in range(101):
	sum = sum +x
print sum

for x in range(len(L)):
	for y in range(len(L[x])):
		print L[x][y]

for x in range(len(L)):
	print L[x]

#list []  tuple () dict {}
#dict is dictionary which is a key-value type
d = {'Michael':95,'Bob':75,'Tracy':85}
print d['Michael']
d['Adam'] = 67
d['Adam'] = 88
print d['Adam']

if 'Adma' in d:
	print 'YES'
else:
	print 'NO'

#according to the key get the value,if no exist return  the special value
print d.get('Thoms',-1)
print d.pop('Bob')

#set type
s = set([1,1,2,2,3,3])
print s
s.add(4)
print s
s.remove(4)
print s

s1 = set([1,2,3])
s2 = set([2,3,4])
print s1 & s2
print s1 | s2

# think the change or no change 
a = ['c','b','a']
a.sort()
print a

a = 'abc'
# no chage a value ,it is only to return a new variable
print a.replace('a','A')
print a