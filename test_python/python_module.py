# -*- coding: utf-8 -*- 
'a test module'
__author__ = 'czm'

import sys

def test():
	args = sys.argv
	if 1==len(args):
		print 'Hello,world!'
	elif 2==len(args):
		print 'Hello, %s!' % args[1]
	else:
		print 'Too many arguments!'

#当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，
#而如果在其他地方导入该hello模块时，if判断将失败，
#因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
if __name__ == '__main__':
	test()

#类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；


'''
模块是一组Python代码的集合，可以使用其他模块，也可以被其他模块使用。

创建自己的模块时，要注意 ：

模块名要遵循Python变量命名规范，不要使用中文、特殊字符；
模块名不要和系统模块名冲突，最好先查看系统是否已存在该模块，检查方法是在Python交互环境执行import abc，若成功则说明系统存在此模块。
'''
#私有函数可以被共有函数调用
#_和__表示私有函数或私有变量
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)