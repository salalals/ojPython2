#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        '''
        空间 O(m + n)
        '''
        rows = set()
        cols = set()
        for i, j in [(i, j) for i in range(len(matrix)) for j in range(len(matrix[0]))]:
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)
        for row in rows:
            matrix[row] = [0] * len(matrix[0])
        for col in cols:
            for r in range(len(matrix)):
                matrix[r][col] = 0
        return


class Solution2(object):
    def setZeroes(self, matrix):
        '''
        没意思，空间 O(1)的解法是将所有的 0 归到第1行，第1列，但是首先要记录下来第一行和第一列是否有 0 ，trick
        '''

        first_row_has_zero = any(map(lambda nu: nu == 0, matrix[0]))
        first_col_has_zero = any(map(lambda nu: nu == 0, [matrix[i][0] for i in range(len(matrix))]))
        for i, j in [(i, j) for i in range(len(matrix)) for j in range(len(matrix[0]))]:
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

        for row, col in [(r,c) for r in range(1, len(matrix)) for c in range(1, len(matrix[0]))]:
            if matrix[row][0] == 0 or matrix[0][col] == 0:
                matrix[row][col] = 0
        if first_row_has_zero:
            matrix[0] = [0] * len(matrix[0])
        if first_col_has_zero:
            for r in range(len(matrix)):
                matrix[r][0] = 0
        return







