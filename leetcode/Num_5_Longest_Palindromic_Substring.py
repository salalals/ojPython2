#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''
        brute force递归
        肯定超时了
        注意string的reverse可以这样写 s[::-1]
        '''
        if s == s[::-1]:
            return s
        left = self.longestPalindrome(s[:-1])
        right = self.longestPalindrome(s[1:])
        return left if len(left) > len(right) else right


class Solution2(object):
    def longestPalindrome(self, s):
        '''
        动态规划
        纵轴为start index, i
        横轴为end index, j
        递归的规律为: P(i, j) = P(i + 1, j - i) && s[i] == s[j]
        '''

        '''
        初始化一个len(s) * len(s)的matrix，左下到右上初始化true，再往上的一条线也是true，然后开始递归
        debug的边界条件可能多一个少一个越界，没啥意思
        '''

        # python初始化 Matrix 不能写成[[0] * len(s)] * len(s)，否则每个row都指向同一个向量
        # https://stackoverflow.com/questions/2397141/how-to-initialize-a-two-dimensional-array-in-python
        matrix = [[0 for x in range(len(s))] for y in range(len(s))]
        for i in range(len(s)):
            matrix[i][i] = 1
            if i + 1 < len(s):
                matrix[i + 1][i] = 1

        longest_length = 0
        longest_length_i = 0
        longest_length_j = 0

        for i in range(len(s) - 2, -1, -1):
            for j in range(len(s) - 1, i, -1):
                matrix[i][j] = 1 if ((matrix[i + 1][j - 1]==1) and (s[i]==s[j])) else 0
                if matrix[i][j] == 1 and (j-i+1 > longest_length):
                    longest_length = j-i+1
                    longest_length_i = i
                    longest_length_j = j
        return s[longest_length_i:longest_length_j+1]

