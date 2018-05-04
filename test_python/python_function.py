# -*- coding: utf-8 -*- 
import math
print abs(-13.5)
print hex(12)

def my_abs(x):
	if not isinstance(x,(int, float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x

#empty function ,this is a habit to build overall framework
def nop():
	pass

def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx,ny

def quad(a,b,c):
	if (b*b-4*a*c) < 0:
		return -1
	x1 = (-b+math.sqrt(b*b-4*a*c))/2*a
	x2 = (-b-math.sqrt(b*b-4*a*c))/2*a
	return x1,x2

#the default parameters of the function 
def enroll(name, gender, age=6, city='Beijing'):
	print name
	print gender
	print age
	print city

# the diffience between two function
def add_end(L=[]):
	L.append('END')
	return L

#one thing to keep in mind when define default paraments:
#the default parameters must point to None
#correct add_end(list)
#error   add_end()
def add_end1(L=None):
	if L is None:
		L = []
	L.append('END')
	return L

#function variable parameters
def calc(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n*n
	return sum

def calc1(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n*n
	return sum

#**kw in order to meet the need user registration optional information
def person(name, age, **kw):
	print 'name:',name,'age:',age,'other:',kw

def person1(name, age,city, job):
	print (name, age, city, job)

#parameter combination is difficult for me

# solve the problem of stack overflow
def fact(n):
	if 1 == n:
		return 1
	return n*fact(n-1)

def fact1(n):
	return fact_iter(n,1)

def fact_iter(num, product):
	if 1 == num:
		return product
	return fact_iter(num-1,num*product)

#the problem of the hanota
def move_iter(n,a,b,c):
	if 1 == n:
		print a,'->',c
	else:
		move_iter(n-1,a,c,b)
		print a,'->',c
		move_iter(n-1,b,a,c)



print my_abs(-99)
#print my_abs('a')
x,y = move(100,100,60,math.pi/6)
#return type is tuple
r = move(100,100,60,math.pi/6)
print r
print (x,y)

print quad(2,3,1)
print quad(1,3,-4)
enroll('czm','boy')

#pay attention to the diffience betweeen two function
print add_end()
print add_end()
print add_end()

print add_end1()
print add_end1()
print add_end1()

#tuple
print calc((1,3,5,7))
#list
print calc([1,3,5,7])

#deliever individual elements in list
nums = [1,3,5,7]
print calc1(*nums)
#variable paraments
print calc1(1,3,5,7)

## **kw == dictionary
person('czm',18,city='beijing')
extra = {'city':'Beijing','job':'Engineer'}
person('czm',18,**extra)

person1('sy',20,city="beijng",job="student")

print fact(100)
print fact1(100)

L1 = [0,1,2]
add_end(L1)
add_end(L1)
print L1

move_iter(3,'A','B','C')


'''
*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。




使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。

针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。

Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。

'''