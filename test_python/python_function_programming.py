# -*- coding: utf-8 -*- 
#function name is a variable
f = abs
print f(-10)

def add(a,b,f):
	return f(a)+f(b)

#map 
def f_map(x):
	return x*x

print add(-4,-5,f)

from collections import Iterator
from collections import Iterable
r = map(f_map,[1,2,3,4,5,6,7,8,9])
#list false
print isinstance(r,Iterator)
print isinstance(r,Iterable)
print list(r)

#reduce
'''
再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
'''
from functools import reduce

def fn(x,y):
	return x*10+y

def char2num(s):
	digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	return digits[s]

print reduce(fn,[1,3,5,7])
#str to list to int
print reduce(fn,map(char2num,'13579'))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

#
def str2int(s):
	def fn(x,y):
		return x*10+y
	def char2num(s):
		return DIGITS[s]
	return reduce(fn,map(char2num,s))

print str2int('12345678')


character1 = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J',
                  'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T',
                  'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'}
character2 = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j',
                  'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't',
                  'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z'}

def normalize(name):
	#name.lower return a new object
	name = name.lower()
	if name[0] in character1:
		y = character1[name[0]]
		name = y + name[1:]
	return name

#求多个数的乘积
def prod(L):
	def fn2(x,y):
		return x*y
	return reduce(fn2,L)

# mark it is difficult to unstance
def str2flt(s):
    digitals = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    s = s.split('.')
    def lnk(x, y):
        return x*10+y
    def chr2num(w):
        return digitals[w]
    return reduce(lnk, map(chr2num, s[0])) + reduce(lnk, map(chr2num, s[1]))/(10**len(s[1]))

sloat = '123.456'

if isinstance(str2flt(sloat), float):
    print(str2flt(sloat))


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

'''
#error
# 计算素数的一个方法是埃氏筛法
# to produce a odd num list from 3 to max
def _odd_iter():
	n = 1
	while True:
		n = n+2
		yield n

# 筛选函数
def _not_divisible(n):
	return lambda x:x%n > 0

def primes():
	yield 2
	it = _odd_iter() #构造序列
	while True:
		n = next(it) #返回序列的第一个数
		yield n
		it = filter(_not_divisible(n),it) # 构造新序列

for n in primes():
	if n < 10:
		print n
	else:
		break
'''

#注意字符串的翻转s[::-1]
def is_palindrome(n):
	s = str(n)
	if len(s) == 0 | len(s) == 1:
		return n
	num = len(s)/2
	if (len(s) % 2) == 0:
		if s[:num] == s[:num-1:-1]:
			return n
	else:
		if s[:num+1] == s[:num-1:-1]:
		    return n 

s= '1'
print s[:(len(s)/2)+1]
print s[:(len(s)/2)-1:-1]
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

print sorted(['bob','about','Zoo','Credit'],key=str.lower)
print sorted(['bob','about','Zoo','Credit'],key=str.lower,reverse=True)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
	pass

def by_value(t):
	pass

'''
filter()的作用是从一个序列中筛出符合条件的元素。由于filter()使用了惰性计算，
所以只有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素。
'''