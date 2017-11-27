#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        '''
        没意思，把numRows个数组创建好，for循环往里边加
        '''
        matrix = ["" for x in range(numRows)]
        incrementor = 1
        row = 0
        for char in s:
            matrix[row] = matrix[row] + char
            row = row + incrementor
            if row >= numRows or row < 0:
                incrementor = incrementor * (-1)
                row = row + incrementor + incrementor
        return reduce(lambda s1, s2 : (s1 + s2), matrix)



