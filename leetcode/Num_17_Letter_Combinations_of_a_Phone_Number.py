#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        '''
        笛卡尔积 Cartesian
        '''
        phone_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        if not digits:
            return list()
        result = [""]
        strings = map(lambda digit: phone_dict.get(digit), digits)
        for string in strings:
            result = self.cartesian(result, string)
        return result

    def cartesian(self, string_list, next_string):
        result = list()
        for s in string_list:
            for ch in next_string:
                result.append(s + ch)
        return result

class Solution2(object):
    def letterCombinations(self, digits):
        '''
        笛卡尔积 Cartesian 自己写的lambda版，无法再读懂
        这个写法是在不熟悉python的for循环的前提下弄出来的
        '''
        phone_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        return list() if not digits else reduce(
            lambda a, b: map(lambda (x, y): x + y, zip(a * len(b), "".join(map(lambda ch: ch * len(a), b)))),
            [[""]] + map(lambda digit: phone_dict.get(digit), digits)[:]
        )


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
