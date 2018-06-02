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

#set type. is also a collection of key but does not store value
#need to provice the list variable
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

import re

str1 = '1,21,34'

L = re.findall(r'\-?\d+\.?\d*',str1)
print (L)

from functools import reduce
def fn(s,s1):
	return str(s) + ',' + str(s1)

#reduce的第一个参数必须是带有2个参数的函数
str2 = reduce(lambda s,s1: str(s) + ',' + str(s1), L)
print str2

#test json
import json
from pprint import pprint
print json.dumps(False)
d = {'a':True, 'b':'Hello', 'c':None}
#将字典类型进行编码成json
st = json.dumps(d)
print (type(st))
print (st)

d1 = json.loads(st)
print (type(d1))
print (d1)

'''
str to byte
'''
my_str = 'hello world'
my_str_as_bytes = str.encode(my_str)
print (type(my_str_as_bytes))

my_decoded_str = my_str_as_bytes.decode('utf-8')
print (type(my_decoded_str))

#，list里面的项是整形
d = {'K':-10, 'S':-11}
L = [-10,-20]
d['M'] = L[0] + 100
print d['M']
for item in L:
	print (isinstance(item,str))
for k in d:
	print (isinstance(d[k], int))
	print (d[k])


L = [1,2,3,4,5]
print (L[-1])
print (L[-2])

def changeZero(L):
	for x in range(len(L)):
		if L[x] == 0:
			L[x] = -100

def changeBack(L):
	for x in range(len(L)):
		if L[x] == 100:
			L[x] = 0
L = [0,-23,0,-45,0,-35]
changeZero(L)
print (L)	

'''
json.dumps() python object -> str
json.dump()  file ->str
json.loads() str -> python object
json.load() str -> file
'''

'''
python中的前缀意思分别表示
r说明字符串r'XXX'中的XXX是普通字符
即如果是“\n”那么表示一个反斜杠字符，一个字母n，而不是表示换行了。
f= open(r'C:\Program Files\Adobe\Reader 9.0\Setup Files\setup.ini','r')

u表示是一个Unicode的字符

b表示bytes
'''

'''
使用正则表达式进行相应的匹配工作
## 总结
## ^ 匹配字符串的开始。
## $ 匹配字符串的结尾。
## \b 匹配一个单词的边界。
## \d 匹配任意数字。
## \D 匹配任意非数字字符。
## x? 匹配一个可选的 x 字符 (换言之，它匹配 1 次或者 0 次 x 字符)。
## x* 匹配0次或者多次 x 字符。
## x+ 匹配1次或者多次 x 字符。
## x{n,m} 匹配 x 字符，至少 n 次，至多 m 次。
## (a|b|c) 要么匹配 a，要么匹配 b，要么匹配 c。
## (x) 一般情况下表示一个记忆组 (remembered group)。你可以利用 re.search 函数返回对象的 groups() 函数获取它的值。
## 正则表达式中的点号通常意味着 “匹配任意单字符”

解题思路
提取的数字先可能带负号，然后是整数，小数，整数加小数
正则表达式的式子可以写成"\-?\d+\.?\d*"
\-? 匹配负号，可能有也可能没有， \d+匹配一次或者多次数字，不写成\d*是因为
及时是小数前面也会存在0. 。匹配\.?匹配小数点。 \d*匹配小数点之后的数字是0个或者多个
'''