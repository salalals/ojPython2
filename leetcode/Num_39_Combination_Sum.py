#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        '''
        递归
        '''
        candidates = sorted(list(set(candidates)))
        return self.combination_sum(candidates, target)

    def combination_sum(self, candidates, target):
        solutions = []
        for i in range(len(candidates)):
            if candidates[i] > target:
                break
            elif candidates[i] == target:
                solutions.append([candidates[i]])
                break
            else:
                sub_solution = self.combination_sum(candidates[i:], target - candidates[i])
                solutions = solutions + map(lambda sol: [candidates[i]] + sol, sub_solution)
        return solutions

