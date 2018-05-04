# -*- coding : utf-8 -*-
import unittest
from python_debug2 import Dict
from python_debug2 import Student

class TestDict(unittest.TestCase):
#以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，
#测试的时候不会被执行。
#setUp和tearDown
#可以在单元测试中编写两个特殊的setUp()和tearDown()方法。
#这两个方法会分别在每调用一个测试方法的前后分别被执行
#相当于以前写C++时候的gtest测试框架。
#注意这里是打印了5次，因为是每个测试方法前后分别打印
	def setUp(self):
		print('setUp...')

	def tearDown(self):
		print('tearDown...')

	def test_init(self):
		d = Dict(a=1,b='test')
		self.assertEqual(d.a,1)
		self.assertEqual(d.b,'test')
		self.assertTrue(isinstance(d,dict))

	def test_key(self):
		d = Dict()
		d['key'] = 'value'
		self.assertEqual(d.key, 'value')

	def test_attr(self):
		d = Dict()
		d.key = 'value'
		self.assertTrue('key' in d)
		self.assertEqual(d['key'], 'value')

	def test_keyerror(self):
		d = Dict()
#另一种重要的断言就是期待抛出指定类型的Error，
#比如通过d['empty']访问不存在的key时，断言会抛出KeyError：
		with self.assertRaises(KeyError):
			value = d['empty']

	def test_attrerror(self):
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.empty

class TestStudent(unittest.TestCase):

    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
        	s1.get_grade()
        with self.assertRaises(ValueError):
        	s2.get_grade()

if __name__ == '__main__':
	unittest.main()

'''
单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。

单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。

单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug。

单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。
'''