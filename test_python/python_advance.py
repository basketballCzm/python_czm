# -*- coding: utf-8 -*- 
#Slice 操作符
L = ['Michael','Sarah','Tracy','Bob','Jack']
#print L[0] but not print L[3]
print L[0:3]
print L[:3]
#print L[-2] and L[-1]
print L[-2:]
#print L[-2] but not print L[-1]
print L[-2:-1]
print L[:5:2]

print 'ABCDEFG'[:3]
print 'ABCDEFG'[::2]

def trim(s):
	if len(s) == 0:
		return s
	while s[:1] == ' ':
		s = s[1:]
	while s[-1:] == ' ':
		s = s[:-1]
	return s

# go over dictionary 
d = {'a':1,'b':2,'c':3}
for key in d:
	print key
for value in d.values():
	print value
for item in d.items():
	print item
for k,v in d.items():
	print k,v

#judge an object if can be iterate
#方法是通过collections模块的Iterable类型判断
from collections import Iterable
print isinstance('abc',Iterable)
print isinstance([1,2,3],Iterable)

print isinstance(123,Iterable)

#list to achieve index-element use enumerate function 
for i,value in enumerate(['A','B','C']):
	print i,value

for x,y in [(1,2),(2,4),(4,6)]:
	print x,y

def findMinAndMax(L):
	if 0 == len(L):
		return (None,None)
	min1 = min(L)
	max1 = max(L)
	return (min1,max1)

import os
print [d for d in os.listdir('.')]

L1 = ['Hello','World','IBM','Apple']
print [s.lower() for s in L1]

L2 = ['Hello','World',18,'Apple',None]
L3 = [s.lower() for s in L2 if isinstance(s,str)]

#generator
#the diffience is [] and ()
print [x*x for x in range(10)]
g = (x*x for x in range(10))
print g
for n in g:
	print n

# generate list
print list(range(1,11))
print [x*x for x in range(1,11)]
print [x*x for x in range(1,11) if x%2 == 0]
print [x+y for x in 'ABC' for y in 'XYZ']

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')


if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

print(L3)
if L3 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

#one step to study generator
def fib(max):
	n,a,b = 0,0,1
	while n < max:
		print b
		a,b = b,a+b
		n = n+1
	return 'done'

def fib1(max):
	n,a,b = 0,0,1
	while n < max:
		#to provide a generator
		yield b
		a,b = b,a+b
		n = n+1
'''
这里，最难理解的就是generator和函数的执行流程不一样。
函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
而变成generator的函数，在每次调用next()的时候执行，
遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
'''
print fib(6)

#generator
for n in fib1(6):
	print n
g = fib1(6)
'''
while True:
	try:
		x = next(g)
		print 'g',x
	except StopIteration as e:
		print 'Generator return value:',e.value
		break 
'''

def odd():
	print 'step1'
	yield 1
	print 'step2'
	yield 3
	print 'step3'
	yield 5

# 遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
o = odd()
print next(o)
print next(o)
print next(o)

'''
yield lst
lst = [1] + [(lst[i - 1] + lst[i]) for i in range(1, len(lst))] + [1]
count += 1
'''

def triangles():
	n,b = 0,[1]
	while n < 10:
		yield b
		'''
		c = []
		for x in range(len(b)):
			if x == 0:
				c.append(1)
			else:
				c.append(b[x]+b[x-1])
		c.append(1)
		b = c'''
		b = [1] + [(b[i-1]+b[i]) for i in range(1,len(b))] + [1]
		n=n+1

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')


'''
我们已经知道，可以直接作用于for循环的数据类型有以下几种：

一类是集合数据类型，如list[]、tuple()、dict{}、set([])、str''等；

一类是generator，包括生成器和带yield的generator function。

这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。

可以使用isinstance()判断一个对象是否是Iterable对象：
'''

from collections import Iterator
#tuple true
print isinstance((x for x in range(10)),Iterator)
#list false
print isinstance([],Iterator)
print isinstance([],Iterable)
#dict false
print isinstance({},Iterator)
print isinstance({},Iterable)
#str false
print isinstance('abc',Iterator)
print isinstance('abc',Iterable)
'''
生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。

把list、dict、str等Iterable变成Iterator可以使用iter()函数：

你可能会问，为什么list、dict、str等数据类型不是Iterator？

这是因为Python的Iterator对象表示的是一个数据流，
Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。
可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，
只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，
只有在需要返回下一个数据时它才会计算。

Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。


小结
凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

在这里就只要记住能用for循环的对象统称为可以迭代对象Iterable
Iterable 和 Iterator
可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator

'''


it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print x
    except StopIteration:
        # 遇到StopIteration就退出循环
        break