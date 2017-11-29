#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        '''
        递归
        '''
        if not nums:
            return []
        return self.compute_permute(nums)

    def compute_permute(self, nums):
        if len(nums) == 1:
            return [[nums[0]]]
        solutions = []
        for i in range(len(nums)):
            sub_solution = self.compute_permute(nums[0:i] + nums[i+1:])
            solutions = solutions + map(lambda sol: [nums[i]] + sol, sub_solution)
        return solutions


# 使用 itertools
import itertools
print list(itertools.permutations([1,2,3]))