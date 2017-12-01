#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        '''
        没意思，原位动态规划
        '''
        for i, j in [(i, j) for i in range(len(grid)) for j in range(len(grid[0]))]:
            if i == 0 and j == 0:
                pass
            elif i == 0:
                grid[i][j] = grid[i][j - 1] + grid[i][j]
            elif j == 0:
                grid[i][j] = grid[i][j] + grid[i - 1][j]
            else:
                grid[i][j] = min([grid[i][j] + grid[i - 1][j], grid[i][j] + grid[i][j - 1]])
        return grid[i][j]


