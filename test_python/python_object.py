# -*- coding: utf-8 -*- 

class Student(object):
	#注意到__init__方法的第一个参数永远是self
	#__在变量前面加__表示该成员变量为私有属性
	#__name__是特殊的变量名可以直接访问，不能使用
	#_name虽然我在外部可以访问请把我当成私有变量
	#解释器__name变成_Student__name根据各个编译器不同而不同
	def __init__(self, name, score):
		self.__name = name
		self.__score = score

	def print_score(self):
		print ('%s:%s' %(self.__name,self.__score))

	def get_grade(self):
		if self.__score >= 90:
			return 'A'
		elif self.__score >= 60:
			return 'B'
		else:
			return 'C'
	def get_name(self):
		return self.__name

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa simpson',87)

bart.print_score()
lisa.print_score()

lisa = Student('Lisa', 99)
bart = Student('Bart', 59)

#不建议这样干
print (bart._Student__name)
print(lisa.get_name(), lisa.get_grade())
print(bart.get_name(), bart.get_grade())

#error way to write
bart.__name = 'New way'
#python new add a variable __name
print (bart.__name)
print (bart.get_name())

#继承和多态
class Animal(object):
	def run(self):
		print ('Animal is running...')

class Dog(Animal):

	#多态
	def run(self):
		print ('Dog is running...')
	def eat(self):
		print ('Dog eat meat...')

class Cat(Animal):
	def run(self):
		print ('Cat is running...')
	def eat(self):
		print ('Cat eat fish...')

animal = Animal()
dog = Dog()
dog.run()

cat = Cat()
cat.run()

print (isinstance(cat,Cat))
print (isinstance(cat,Animal))

#use base class to receive the child object
#对于python只要保证传入的对象有一个run()方法就能使用多态
#对于java规定传入的对象必须是基类的子类
def run_twice(animal):
	animal.run()
	animal.run()

run_twice(dog)
run_twice(cat)

print (type(animal))
print (type(dog))

if (type(123) == int):
	print (True)

#判断函数的类型
import types

def fn():
	pass
#fn:types.FunctionType
#abs:types.BuiltinFunctionType
#lambda x:x  :  types.LambdaType
#(x for x in range(10)): types.GeneratorType
print (type(fn))
print (isinstance(b'a',bytes))
print (isinstance([1,2,3],(list,tuple)))
print (isinstance((1,2,3),(list,tuple)))

print (dir('ABC'))
print (len('ABC'))
print ('ABC'.__len__())

#覆盖一个已有的系统函数
class MyDog(object):
	def __len__(self):
		return 100

mydog = MyDog()
#two method is equal
print (mydog.__len__())
print (len(mydog))

#对一个类中的属性进行相应的操作
class MyObject(object):
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x*self.x


obj = MyObject()
print (getattr(obj,'z',404))
print (setattr(obj,'z',19))
print (hasattr(obj,'z'))
print (getattr(obj,'z',404))

print (hasattr(obj,'power'))
fn = getattr(obj,'power')
print (fn())

#一个类的函数和成员变量都是其属性hasattr setattr getattr

#能写简化就不写
#sum = getattr(obj, 'x') + getattr(obj, 'y')

def readImage(fp):
	if hasattr(fp,'read'):
		return readData(fp)
	return None

#实例属性和类属性
#对于一个实例而言，是先找实例属性然后再找类属性
class Student1(object):
	name = 'Student'
s = Student1()
print (s.name)
print (Student1.name)
s.name = 'Michael'
print (s.name)
print (Student1.name)
del s.name
print (s.name)


class Student(object):
	count = 0
	def __init__(self,name):
		self.name = name
		#注意这里的count是类属性不是实例属性
		Student.count += 1

# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')