#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        '''
        python 的 list 有pop()方法，完全可以做 stack 来用
        '''
        parenthese_dict = {
            ")": "(",
            ']': '[',
            '}': '{'
        }
        stack = list()
        for ch in s:
            if len(stack) == 0 or stack[-1] != parenthese_dict.get(ch):
                stack.append(ch)
            else:
                stack.pop()
        return not stack

