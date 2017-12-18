#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ind_str = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        number = 0
        for ch in s:
            number = number * 26 + ind_str.index(ch)
        return number





