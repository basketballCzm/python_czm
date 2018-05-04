# -*- coding: utf-8 -*- 

def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum
f1 = lazy_sum(1,3,5,7,9)
f2 = lazy_sum(1,3,5,7,9)
print f1==f2
print f1()


#返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
#定义函数！=执行函数
def count():
	fs=[]
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs

def count1():
	def f(j):
		def g():
			return j*j
		return g
	fs = []
	for i in range(1,4):
		fs.append(f(i)) #f(i)立刻被执行，因此i的当前值被传入f()
	return fs

def createCounter():
	i = [0]
	def counter():
		i[0] = i[0]+1
		return i[0]
	return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


f1,f2,f3 = count()
print f1()
print f2()
print f3()

f1,f2,f3 = count1()
print f1()
print f2()
print f3()

#匿名函数lambda x: x * x实际上就是
#冒号前面的x表示函数参数。
#map是后面的数分别作为前面的参数
print list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9]))
f = lambda x: x*x
print f(10)

def build(x,y):
	return lambda: x*x+y*y

print list(filter(lambda x:x%2==1,range(1,20)))

def now():
	print('2015-3-25')
f = now
print f()

print now.__name__
print f.__name__

'''
假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，
但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
'''

#mark  (*args,**kw)参数表表示能接收任意参数
def log(func):
	def wrapper(*args,**kw):
		print('call %s():' %func.__name__)
		return func(*args,**kw)
	return wrapper

#now = log(now)
@log
def now(s):
	print ('2015-3-25')
	print (s)
print now('hello world')
'''
我们来剖析上面的语句，首先执行log('execute')，
返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。
'''

def log1(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print '%s %s():' %(text,func.__name__)
			return func(*args,**kw)
		return wrapper
	return decorator

#now = log('execute')(now)
@log1('execute')
def now():
	print '2015-3-25'

print now()
print now.__name__

import time, functools

def metric(fn):
	@functools.wraps(fn)
	def wrapper(*args, **kw):
		print 'begin call'
		start_time = time.time()
		res =  fn(*args,**kw)  #在这里就已经进行了函数的调用
		stop_time = time.time()
		print 'end call'
		print '%s executed in %s ms' %(fn.__name__,(start_time-stop_time))
		return res
	return wrapper	

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

'''
小结
在面向对象（OOP）的设计模式中，decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来实现，而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。Python的decorator可以用函数实现，也可以用类实现。
'''

print int('12345',16)
#base是按照多少进制进行转换成十进制
def int2(x,base=2):
	return int(x,base)
print int2('100000')
print int2('101010')

#functools.partial 偏函数固定参数
import functools
int2 = functools.partial(int,base=2)
print int2('100000')
#kw={'base':2}
#int('101010',**kw)
print int2('101010')

#这里的max相当于是一个函数
max2 = functools.partial(max,10)

#args = (10,5,6,7)
#max(*args)
print max2(5,6,7)