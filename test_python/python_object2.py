# -*- coding : utf-8 -*-
#多重继承
#正规的命名方式是RunnableMixIn

class Runnable(object):
	def run(self):
		print("Running ...")

#FlyableMixIn
class Flyable(object):
	def fly(self):
		print("Flying ...")

class Animal(object):
	pass

class Mammal(Animal):
	pass

class Bird(Animal):
	pass

#这种设计称为MixIn RunnableMixIn
class Dog(Mammal,Runnable):
	pass

class Bat(Mammal,Flyable):
	pass

class Parrot(Bird,Flyable):
	pass

class Ostrich(Bird,Runnable):
	pass

dog = Dog()
dog.run()

"""需要导入相对应的包
#多线程的TCP 和 UDP服务
class MyTCPServer(TCPServer, ForkingMixIn):
	pass

class MyUDPServer(UDPServer,ThreadingMinIn):
	pass

class MyTCPServer(TCPServer,CoroutineMixIn):
	pass
"""
#必须要庞大的继承链，只要组合不同的类的功能，就可以快速的
#构造出所需要的子类 C++支持多继承，Java支持单继承

#__str__的用法
class Student(object):
	def __init__(self,name):
		self.name = name

	def __str__(self):
		return "Student object (name: %s)" % self.name
	__repr__ = __str__

print (Student("Michael"))

#这里相当于是直接显示实例，
#直接 print (Student(name))调用的是__repr__(),返回的是开发者看到的字符串。
#调用__str__(),返回的是用户看到的字符串
#打印出来的字符还是不好看
Student("Jack")

#__iter__的用法,如果一个类想被for...in循环使用
#就必须使用__iter__()方法进行实现
#python的for循环就会一直调用该迭代器的__next__()
#方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环

class Fib(object):
	def __init__(self):
		self.a,self.b = 0,1

	def __iter__(self):
		return self #实例本身就是迭代对象，故返回自己回去

	def __next__(self):
		self.a,self.b = self.b ,self.a+self.b #计算下一个值
		if self.a > 10000:
			raise StopIteration()
		return self.a

for n in Fib():
	print(n)

#__iter__虽然能够迭代，但是还不能当list进行使用Fib()[5]
#__getitem__解决这个问题

class Fib(object):
	def __getitem__(self,n):
		a,b = 1,1
		for x in range(n):
			a,b = b, a+b
		return a 

f = Fib()
print (f[0])
print (f[10])

#进一步添加list的切片功能,传入的参数可能是一个int
#也可能是一个切片对象slice,所以要做判断
#在写python代码时要注意tab键和空格键两者不能进行混合使用
class Fib(object):
	def __getitem__(self,n):
		if isinstance(n, int):
			a,b = 1,1
			for x in range(n):
				a,b = b, a+b
			return a
		#[4:6] [:8]切片对象
		if isinstance(n, slice):
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a,b = 1,1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a,b = b,a+b
			return L

f = Fib()
print (f[:5])

#__getattr__()返回一个动态属性,当使用python调用的属性不存在在时
#会调用__getattr__方法返回一个动态属性
#只有在没找到该属性的基础上才会调用__getattr__方法
#__getattr__方法会默认返回None,如果只响应特定的属性，抛出AttributeError的错误
class Student(object):
	def __init__(self):
		self.name = "Michael"

	def __getattr__(self,attr):
		if attr == "score":
			return 99
		#返回一个函数
		if attr == 'age':
			return lambda:25
		raise AttributeError("\'Student\' object has no attr \'%s\'" % attr)


s = Student()
print (s.name)
print (s.score)
print (s.age())
#print (s.sex)

"""
以上的例子实际上可以把一个类的所有属性和方法都动态化处理不需要任何特殊的手段
这种完全动态调用的特性有什么实际作用呢？
作用就是，可以针对完全动态的情况作调用。
"""

#利用完全动态的__getattr__，实现一个完全动态的链式调用

class Chain(object):
	def __init__(self, path=""):
		self._path = path

	def __getattr__(self, path):
		return Chain("%s/%s" % (self._path,path))

	def __str__(self):
		return self._path

	__repr__ = __str__

print (Chain().status.user.timeline.list)

#print (Chain().users('michael').repos)

#__call__使用方法
#一个对象实例可以有自己的属性和方法，
#当我们调用实例方法时，我们用instance.method()来调用。
#能不能直接在实例本身上调用呢？
class Student(object):
	def __init__(self, name):
		self.name = name

	#对实例进行直接调用就好比对一个函数进行调用一样，
	#所以你完全可以把对象看成函数，
	#把函数看成对象，因为这两者之间本来就没啥根本的区别
	def __call__(self):
		print ("My name is %s." % self.name)

s = Student("Michael")
s()

#怎样判断一个变量是对象还是函数？
#看一个对象能否被调用，能被调用的对象就是Callable对象
#通过callable我们能够判断一个对象是否是"可调用"对象
print (callable(Student("czm")))
print (callable(max))
print (callable([1,2,3]))

#使用枚举类
from enum import Enum

Month = Enum("Month",("Jan","Feb","Mar","Apr","May","Jun",
	"Jul","Aug","Sep","Oct","Nov","Dec"))

for name, member in Month.__members__.items():
	print (name, "=>", member, ",", member.value)

from enum import Enum, unique

#@unique 可以检查保证没有重复值
@unique
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6

#访问这些枚举值的若干方法
print (Weekday.Sun)
print (Weekday["Mon"])
print (Weekday(1))
# erroe way to write this print (Weekday[1])
# stackover print (Weekday(7))
print (Weekday.Tue.value)

#把Student的gender属性改造成为枚举类型，可以避免使用字符串
class Gender(Enum):
	Male = 0
	Female = 1

#__name 表示其属性为私有属性，外部不能直接进行访问
class Student(object):
	def __init__(self, name, gender):
		self.__name = name
		self.__gender = gender
# 测试:
bart = Student('Bart', Gender.Male)
if bart._Student__gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')

#使用元类type()
#动态语言和静态语言最大的不同，就是函数和类的定义，
#不是编译时定义，而是运行时动态创建的

from hello import Hello
h = Hello()
h.hello()

#type()函数可以查看一个类型或变量的类型，Hello是一个class，
#它的类型就是type，而h是一个实例，它的类型就是class Hello。
#<class 'type'>
print (type(Hello))
#<class 'hello.Hello'>
print (type(h))

#type()函数既可以返回一个对象的类型，又可以创建出新的类型，
#比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：

def fn(self, name = "world"):
	print ("Hello, %s" % name)

#使用type创建一个类 Hello class
#tuple单元素的写法

#要创建一个class对象，type()函数依次传入3个参数：

#1.class的名称；
#2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
#3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
#python 使用class创建类也是扫描class的写法后调用type
#通过type()动态创建出类
Hello = type("Hello",(object,),dict(hello=fn))
h = Hello()
h.hello()

print (type(Hello))

#<class "__main__.Hello"> ? 为什么不是hello.Hello。绑定的hello只是对fn函数进行了绑定
print (type(h))

#除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
#metaclass 直译为元类，如果想创建出类就必须根据metaclass创建出类
#所以:先定义metaclass，然后创建类
#先定义metaclass，就可以创建类，最后创建实例。

#__new__()方法接收到的参数依次是：
#1.当前准备创建的类的对象；
#2.类的名字；
#3.类继承的父类集合；
#4.类的方法集合。
class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):
		attrs["add"] = lambda self,value: self.append(value)
		return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
	pass

L = MyList()
L.add(1)
print (L)