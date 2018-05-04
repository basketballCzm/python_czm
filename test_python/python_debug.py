# -*- coding : utf-8 -*-
#python可以使用pdb来进行单步调试方式来执行代码

#发生错误那么就返回指定的错误码
#解决错误码和正常代码混合在一起的问题

#这样的解决方式使得发生错误时会一级级往上进行报错
def foo():
	r = some_function()
	if r == (-1):
		return (-1)

	return r

def bar():
	r = foo()
	if r == (-1):
		print ('Error!')
	else:
		pass

# 使用python内置的一套try...except...finally...的错误处理机制
#当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，
#则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，执行完except后，
#如果有finally语句块，则执行finally语句块，至此，执行完毕。
try:
	print('try...')
	r = 10/int('2')
	#这里其实有语法错误，但是不执行就不会报错
	print('result:', r)
except ValueError as e:
	print('ValueError:', e)
#Python的错误其实也是class，所有的错误类型都继承自BaseException
#UnicodeError永远不能捕获错误，因为它是ValueError的子类
except UnicodeError as e:
	print('UnicodeError', e)
except ZeroDivisionError as e:
	print('except:', e)
else:
	print('No Error!')
#如果有finally语句，则该语句一定会被执行
finally:
	print('finally...')
print('END')


#使用try...except捕获错误还有一个巨大的好处，
#就是可以跨越多层调用，比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，
#这时，只要main()捕获到了，就可以处理：

#这样写不需要在每一个可能出现错误的地方进行校验
#只要在合适的层次去捕获错误就可以了
def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s)*2

"""这样做的好处是会显示调用栈
def main():
	bar('0')
main()

def main():
	try:
		bar('0')
	except Exception as e:
		print('Error:', e)
	finally:
		print('Finally...')
main()
"""

#抛出自己定义的错误,尽量使用python内置的错误，如ValueError TypeError
class FooError(ValueError):
	pass

def foo(s):
	n = int(s)
	if n==0:
		raise FooError('invalid value: %s' % s)
	return 10/n

def bar():
	try:
		foo('0')
	except ValueError as e:
		print('ValueError!')
		#在这里又把错误重新抛了出去
		raise
#其实这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记录一下，便于后续追踪。
#但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，
#让顶层调用者去处理。好比一个员工处理不了一个问题时，
#就把问题抛给他的老板，如果他的老板也处理不了，就一直往上抛，最终会抛给CEO去处理
#bar()

#此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：
"""
try:
	10/0
except ZeroDivisionError:
	raise ValueError('input error!')
"""
from functools import reduce

def str2num(s):
	return int(s)

def calc(exp):
	ss = exp.split('+')
	ns = map(str2num,ss)
	return reduce(lambda acc, x: acc+x, ns)

def main():
	try:
		r = calc('100 + 200 + 345')
		print('100 + 200 + 345 = ',r)
		r = calc('99 + 88 + 7.6')
		print('99 + 88 + 7.6 = ',r)
	except ValueError as e:
		print("ValueError",e)
		raise
main()
