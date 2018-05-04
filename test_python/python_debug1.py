# -*- coding : utf-8 -*-

#使用print来调试程序，但是这样会产生很多的垃圾信息
def foo(s):
	n = int(s)
	print('>>> n = %d' %n)
	return 10/n

#使用断言来进行调试程序
def foo(s):
	n = int(s)
	#如果断言是false打印后面的报错，并且抛出AssertionError
	#使用 -O 来关闭断言
	assert n != 0, 'n is zero'
	return 10/n
'''
import logging
logging.basicConfig(level=logging.INFO)
def foo(s):
	n = int(s)
	logging.info('n = %d' % n)
	return 10/n
'''
"""
这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，
当我们指定level=INFO时，logging.debug就不起作用了。
同理，指定level=WARNING后，debug和info就不起作用了。
这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。
"""

#使用pdb来调试程序 python-m pdb python_debug1.py
import pdb
def foo1(s):
	n = int(s)
	#在可能出错的地方设置断点
	pdb.set_trace()
	return 10/n

#设置断点
def main():
	foo1('0')
main()

#但是最后你会发现，logging才是终极武器。