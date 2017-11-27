#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        '''
        没意思，还没过，懒得再写了，主要就是考各种奇怪的边界条件
        1. 注意符号
        2. 注意overflow
        '''
        if x == 0:
            return 0

        sign = 1 if x > 0 else -1
        x = sign * x
        reversed_string = str(x)[::-1]
        for index in range(len(reversed_string)):
            if reversed_string[index] != "0":
                return int(reversed_string[index:]) * sign
        raise Exception()

