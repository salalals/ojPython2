#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        '''
        递归
        思路简单，python写清楚实现还是需要练习
        '''
        solutions = []
        self.solve_n_queens(n, 0, [], solutions)
        return map(lambda sol: self.translate_solution(n, sol), solutions)


    def solve_n_queens(self, n, start, part_sol, solutions):
        if start == n:
            solutions.append(part_sol)
        for col in range(n):
            if col not in part_sol and not any(map(lambda prev_col_ind: abs(col - part_sol[prev_col_ind]) == start - prev_col_ind, range(len(part_sol)))):
                self.solve_n_queens(n, start + 1, part_sol[:] + [col], solutions)

    def translate_solution(self, n, solution):
        """
        :param solution: list[int]
        :return: List[str]
        """
        return map(lambda ind: "." * ind + "Q" + "." * (n - ind - 1), solution)

