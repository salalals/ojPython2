#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''
        从后向前做动态规划，超时了
        '''
        bools = [False for i in range(len(nums) - 1)] + [True]
        for i in range(len(bools) - 2, -1, -1):
            bools[i] = any(bools[i:i + nums[i] + 1])
        return bools[0]


class Solution2(object):
    def canJump(self, nums):
        '''
        因为题目说都是non-negative的数字，所以从最后搜索0，然后看是否能跨过0
        '''
        can = True
        i = len(nums) - 2
        zero_index = None
        while i >= 0:
            if can:
                if nums[i] == 0:
                    zero_index = i
                    can = False
            else:
                if i + nums[i] > zero_index:
                    can = True
            i = i - 1
        return can







