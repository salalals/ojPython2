#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        sub_triangle = self.generate(numRows - 1)
        last_line = list()
        for i in range(len(sub_triangle[-1]) - 1):
            last_line.append(sub_triangle[-1][i] + sub_triangle[-1][i+1])
        last_line = [1] + last_line + [1]
        sub_triangle.append(last_line)
        return sub_triangle




