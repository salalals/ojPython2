#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        '''
        没意思，
        使用方法调用栈做 深度搜索
        使用全局set记录访问过的节点
        '''
        used_set = set()
        for i, j in [(i, j) for i in range(len(board)) for j in range(len(board[0]))]:
            if self.check_exist(board, word, used_set, i, j):
                return True
        return False


    def check_exist(self, board, word, used_set, next_i, next_j):
        if not word:
            return True
        if next_i < 0 or next_i >= len(board) or next_j < 0 or next_j >= len(board[0]):
            return False

        if word[0] == board[next_i][next_j] and (next_i, next_j) not in used_set:
            used_set.add((next_i, next_j))
            if self.check_exist(board, word[1:], used_set, next_i, next_j + 1) \
                or self.check_exist(board, word[1:], used_set, next_i + 1, next_j) \
                or self.check_exist(board, word[1:], used_set, next_i, next_j - 1) \
                or self.check_exist(board, word[1:], used_set, next_i - 1, next_j):
                return True
            else:
                used_set.remove((next_i, next_j))
        return False


