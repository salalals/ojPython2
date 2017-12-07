#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        '''
        和 Num_77 类似，采用尾递归运算
        sol = sol_exclude_first + sol_include_first
        '''
        return self.compute_subsets(nums)

    def compute_subsets(self, nums):
        if not nums:
            return [nums]

        subsets = self.compute_subsets(nums[1:])
        subsets_copy = [[ele for ele in sub] for sub in subsets]
        return subsets_copy + map(lambda sub: [nums[0]] + sub, subsets)


