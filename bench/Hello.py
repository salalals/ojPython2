#!/usr/bin/python
# -*- coding: utf-8 -*-

# 上边 header 第二行注释为保证python文件中可以有中文



### Hello world ###

print "Hello python!", "Hello", "中文"

# '''或"""生成多行string，在方法里面做为document注释，也即python多行注释
print '''
multiline 1
multiline 2
multiline 3
'''

# python一行写不下就用 \ 收尾换行
print "1 + 2 + 3 + 4 == ", 1 + 2 + \
    3 + 4

# python字符串不能和数字直接相加
print "string" + str(123)



### string 与常用方法 (不包括正则)
string_var = "  hellopython again!"

# strip()去掉空白
print string_var.strip()

# join()连接
print ".".join(["a", 'b', 'c'])

# slice操作和list类似
print string_var[1:]    # 切片
print "->" + string_var[200:] + "<-"  # 空串，不会报错
print string_var[::-1]  # 反转，这个和list操作一样

# r开头不做转义
print r'abcd\t"'

# string为immutable，所有的操作都返回新string
string_var_capitalized = string_var.capitalize()



### list 与常用方法
array_var = list()
array_var = [1, "hello", 3.14, "string"]

# index -1 为最后一个元素，依次类推
print array_var[-1]

# slice 反转
print array_var[::-1]
array_var.append("new element")

# in 判断是否contains
print "hello" in array_var

# 两个list相连 [1,2,3,4,5,6]
print [1,2,3] + [4,5,6]

# list是mutable的，所以有些操作是原位的
sort_list = [3,2,1]
sort_list.sort()
print sort_list

# 如果使用内置的sorted()方法，则返回新list，原list不变
sort_list = [3,2,0]
print sorted(sort_list)
print sort_list



### tuple 元组与常用方法
tuple_var = tuple()
tuple_var = (1, "config", True, False)

# tuple为immutable，二次赋值会报错, 如以下被注释掉的这行
# tupleVar[0] = 123

# tuple 里面只有一个元素的时候以,结束
single_tuple_var = (1,)

# tuple由于不可变，所以可以做hash，所以tuple可以放倒set()里面，也可以做dict的key



### set 集合与常用方法
set_var = set()
set_var = {1,2,3}

# set 可以做集合操作
set1 = {1,2,3}
set2 = {2,3,4}
print set1 - set2
print set1.union(set2)



### dictionary 字典与常用方法
dict_var = dict()

# 字典的key必须是immutable的，如int, string, tuple
dict_var = {1: 'one', "two": 2L}

# dict使用[]访问，如果元素不存在会报错
print dict_var["two"]
# dict使用get()访问，如果元素不存在则返回None
print dict_var.get("two")

print dict_var.has_key(1)




### is, is not, ==
# is 判断是否是同一个对象, 类似于Java里面==
# == 判断是否是同一个值，类似于Java里面equals
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = None
print "(list1 is list2)", (list1 is list2)
print "list1 == list2", list1 == list2
print list3 is None



### pass
# 不做任何事情，比如在定义了空方法或者在if branch里面
if True:
    pass



### 异常处理 try, except, else, finally, raise
try:
    raise Exception()
except:
    print "Exception()"
else:
    print "fine"
finally:
    print "finally"




### 在脚本内定义方法
# 在调用时，param为必填参数，var有默认
def general_method(param, var=1):
    print param
    print var
    # 只写return或没有return，则返回None
    return str(param) + str(var)

general_method("parameter string", var=123)
general_method("parameter string", 123)





### 定义类对象 python里面好像并不常用

# 继承根类object
class Student(object):
    # 定义在这里的都是静态变量
    static_count = 0
    __private_static_attribute = "__private_static_attribute"

    # 构造方法
    def __init__(self, name, age=0):
        # 成员变量都要用self.访问
        self.name = name
        self.age = age
        self.__private_attr = "private attribute"
        Student.static_count = Student.static_count + 1

    # toString方法
    def __repr__(self):
        return "(name: " + self.name + ", age: " + str(self.age) + ")"

    # 所有方法都要有参数self, 以便访问成员变量
    # 在调用时不必填写self
    def intro(self):
        print self.name, self.__private_attr

    # __双下滑线开头(但没有双下划线结尾)表示私有方法，外部不能访问
    def __private(self):
        print "private"

student1 = Student("Zhang")
student2 = Student("Li", 20)
print student1
print student2.name
print Student.static_count
print student1.intro()
















# range(): [0,1,2,3,4]
print range(5)

topList = [range(5), range(10, 20)]
for ele in [n for subList in topList for n in subList]:
    print ele

lower_case = "abcde"
print lower_case.capitalize()
print lower_case



print [[0 for x in range(5)] for row in range(3)]

import time



print [1,2,3,5,76].index(76)


lam = lambda x, y, z: sum([x,y,z])/3.0

print lam(1,5,7)


print __name__ == '__main__'

li = [13,5]
print li.reverse()
print li



ax = [1,1,1,3]
bx = [6,7,8,9]
print dict(zip(ax, bx))

print str(123)
print int(str(012))

import re
print re.match("abc", "abcdeabc").span()


phone = "123-456-7890"
print phone
p2 = phone.replace("-", "")
print p2
p3 = phone.replace(r"\D", "")
print p3
print re.sub(r"\D", "", phone)



'''
如果不使用itertools.product()函数，python可以支持更短的写法
注意下面python的for循环的写法
'''


'''
同时遍历两个list，双重for循环在一行内完成:
expression = a * b
for a in x:
    for b in y:
        expression
'''
x = [1,2,3]
y = [9,8,7]
print [a * b for a in x for b in y]



'''
flatten 一个 list[list]
expression = c
for sub in z:
    for c in sub:
        expression
'''
z = [[1,2,3], [4,5,6]]
print [c for sub in z for c in sub]


'''
以此类推，flatter 一个 list[list[list]]
expression = c
for sub in z:
    for sub2 in sub:
        for c in sub2:
            expression
'''
z = [[[1,2],[3,3]], [[4],[5,6]]]
print [c for sub in z for sub2 in sub for c in sub2]


'''
python for loop partition
[partition[i:i + 2] for i in range(0, len(partition), 2)]
'''

# list comprehensive:
# https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions
# https://docs.python.org/2/tutorial/index.html

# list 做diff
# [item for item in map(str, range(1, 10)) if item not in existed]
# set(list1) - set(list2)

# set直接做diff
a = {1,2,3,4}
b = {3,2,5}
print a - b

print sorted([3,1,2])
print any(["", 0, []])

with open("testdata/testdata.txt") as f:
    print f.readline().strip()
    print f.readline()

def to_int(s):
    return int(s)

print to_int("123")
print map(to_int, ["1", '23'])

