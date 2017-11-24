#!/usr/bin/python
# -*- coding: utf-8 -*-

print "Hello python!", "Hello", "中文"

print '''
multiline 1
multiline 2
multiline 3
'''

stringVar = "hellopython again!"
print stringVar[:]
print stringVar[1:]
print stringVar[:5]
print stringVar[2:6]
print "->" + stringVar[200:] + "<-" # 空串，不会报错

# array 数组
longVar = 123L
arrayVar = [1, "hello", 3.14, "string", longVar]
print arrayVar[1:] + arrayVar[:-1]

# tuple 元组
tupleVar = (1, "config", "value")
# tuple二次赋值会报错
# tupleVar[0] = 123


# dictionary 字典
dictVar = {1: 'one', "two": 2L}
print dictVar[1]
print dictVar.keys()

# in, not in 成员运算符
print ("hello" in arrayVar)

# is, is not, ==
# is 判断是否是同一个对象, 类似于Java里面==
# == 判断是否是同一个值，类似于Java里面equals
array1 = [1,2,3]
array2 = [1,2,3]
print (array1 is array2)
print array1 == array2


# pass
# 不做任何事情，比如在定义了空方法或者在if branch里面
flag = False
if flag:
	print "this is doing something"
else:
	pass

# range(): [0,1,2,3,4]
print range(5)

topList = [range(5), range(10, 20)]
for ele in [n for subList in topList for n in subList]:
	print ele

lower_case = "abcde"
print lower_case.capitalize()
print lower_case

print r'abcd\t"'

print [[0 for x in range(5)] for row in range(3)]

print None
non = None
print non is None
print non == None
print non != None






