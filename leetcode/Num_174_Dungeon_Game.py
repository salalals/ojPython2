#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        '''
        并不难，只是需要一点点计算
        1. 算右下角
        2. 算最后一行
        3. 算最后一列
        返回 0,0 的hp值
        '''
        hp_matrix = [[0 for x in range(len(dungeon[0]))] for y in range(len(dungeon))]
        r, c = len(dungeon) - 1, len(dungeon[0]) - 1
        hp_matrix[r][c] = 1 if dungeon[r][c] > 0 else (dungeon[r][c] * -1) + 1

        for col in range(c - 1, -1, -1):
            right = hp_matrix[r][col + 1]
            if dungeon[r][col] >= right:
                hp_matrix[r][col] = 1
            elif 0 <= dungeon[r][col] and dungeon[r][col] < right:
                hp_matrix[r][col] = right - dungeon[r][col]
            else:
                hp_matrix[r][col] = right + dungeon[r][col] * -1

        for row in range(r - 1, -1, -1):
            down = hp_matrix[row + 1][c]
            if dungeon[row][c] >= down:
                hp_matrix[row][c] = 1
            elif 0 <= dungeon[row][c] and dungeon[row][c] < down:
                hp_matrix[row][c] = down - dungeon[row][c]
            else:
                hp_matrix[row][c] = down + dungeon[row][c] * -1

        for row, col in [(row, col) for row in range(r - 1, -1, -1) for col in range(c - 1, -1, -1)]:
            mini = min([hp_matrix[row + 1][col], hp_matrix[row][col + 1]]);
            if dungeon[row][col] >= mini:
                hp_matrix[row][col] = 1
            elif 0 <= dungeon[row][col] and dungeon[row][col] < mini:
                hp_matrix[row][col] = mini - dungeon[row][col]
            else:
                hp_matrix[row][col] = mini + dungeon[row][col] * -1

        return hp_matrix[0][0]





