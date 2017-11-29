#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        '''
        使用方法调用栈 深搜
        '''
        if self.solve_sudoku(board):
            pass
        else:
            raise Exception()

    def solve_sudoku(self, board):
        for (i, j) in [(i, j) for i in range(9) for j in range(9)]:
            if board[i][j] == '.':
                existed = self.existed_nums(board, i, j)
                potential_values = [item for item in map(str, range(1, 10)) if item not in existed]
                for po in potential_values:
                    board[i][j] = po
                    if self.solve_sudoku(board):
                        return True
                board[i][j] = '.'
                return False
        return True

    def existed_nums(self, board, i, j):
        return \
            filter(lambda po: po != '.', board[i]) + \
            filter(lambda po: po != '.', [board[m][j] for m in range(9)]) + \
            filter(lambda po: po != '.', [board[m][n] for m in range(i/3*3, i/3*3+3) for n in range(j/3*3, j/3*3+3)])
