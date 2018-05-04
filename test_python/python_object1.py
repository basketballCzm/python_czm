# -*- coding: utf-8 -*-

#注意实例属性和类属性的区别
#Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性

def set_age(self,age):
	self.age = age

class Student(object):
	pass

from types import MethodType
#给实例绑定一个方法
s = Student()

s.set_age = MethodType(set_age,s)

s.set_age(25)
print (s.age)

#新添加的属性属性是实例属性而不是类属性
#实例属性只在创建的那个实例中起作用
s1 = Student()
if (hasattr(s1,'set_age')):
	s1.set_age(30)
else:
	print('s1 no exist set_age()')

#为了给所有实例都绑定方法，可以给class绑定方法：
Student.set_age = set_age

s2 = Student()
if (hasattr(s2,'set_age')):
	s2.set_age(30)
	print (s2.age)
else:
	print('s2 no exist set_age()')

#__slots__仅对当前的类实例起作用，对其子类的实例不起作用
#子类的slots也会继承父类的slots
#限制添加的属性
class Student(object):
	__slots__ = ('name','age') #用tuple定义允许绑定的属性名称

s = Student()
s.name = 'czm'
s.age = 19
#s.score = 99
#@property to deal the problen get()andset()
class Student(object):
	def __init__(self,score):
		self._score = score

	def get_score(self):
		return self._score

	def set_score(self, value):
		if not isinstance(value,int):
			raise ValueError("score must be an integer!")
		if value < 0 or value > 100:
			raise ValueError("score must between 0~100!")
		self._score = value
s = Student(50)
s.set_score(60)
print (s.get_score())
#s.set_score(99999)

# to resolve this question. make the way to be simple
#与装饰器decorator类似，python内置@property装饰器就是
#负责把一个方法变成属性调用


class Student(object):
	@property
	def score(self):
		return self._score

    #Mark拼写注意
	@score.setter
	def score(self, value):
		if not isinstance(value,int):
			raise ValueError("score should be an integer!")
		if value < 0 or value > 100:
			raise ValueError("score must between 0~100!")
		self._score= value

s = Student()
s.score = 60
print (s.score)
#s.score = 99999

#把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又
#创建了另一个装饰器@score.setter，负责把一个setter方法变
#成属性赋值，于是，我们就拥有一个可控的属性操作：

class Student(object):
	@property
	def birth(self):
		return self._birth

	@birth.setter
	def birth(self,value):
		self._birth = value

	@property
	def age(self):
		return 2018-self._birth

s = Student()
s.birth = 2000

#practice
class Screen(object):
	@property
	def width(self):
		return self._width

	@property
	def height(self):
		return self._height

	@width.setter
	def width(self,value):
		if not isinstance(value,(int,float)):
			raise ValueError("Input correct value!")
		self._width = value

	@height.setter
	def height(self,value):
		if not isinstance(value,(int,float)):
			raise ValueError("Input correct value!")
		self._height = value

	@property
	def resolution(self):
		return self._width*self._height

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
