#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        '''
        动态规划，三个方向递归即可
        '''
        if not word1 or not word2:
            return max([0 if word1 is None else len(word1), 0 if word2 is None else len(word2)])

        if len(word2) > len(word1):
            word1, word2 = word2, word1
        matrix = [[0 for x in range(len(word1))] for y in range(len(word2))]
        for i, j in [(i, j) for i in range(len(word2)) for j in range(len(word1))]:
            if i == 0 and j == 0:
                matrix[i][j] = 0 if word1[0] == word2[0] else 1
                continue
            if i == 0:
                matrix[i][j] = j if word2[0] in word1[:j+1] else j + 1
                continue
            if j == 0:
                matrix[i][j] = i if word1[0] in word2[:i+1] else i + 1
                continue
            from_top_left = matrix[i - 1][j - 1]
            from_top_left = from_top_left if word1[j] == word2[i] else from_top_left + 1
            matrix[i][j] = min([from_top_left, matrix[i][j - 1] + 1, matrix[i - 1][j] + 1])

        return matrix[len(word2) - 1][len(word1) - 1]
