#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        brute force 超时
        '''
        max_sum = None
        for i, j in [(i, j) for i in range(len(nums)) for j in range(i + 1, len(nums) + 1)]:
                max_sum = sum(nums[i:j]) if max_sum is None else max([max_sum, sum(nums[i:j])])
        return max_sum


class Solution2(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        O(N) 解法还没想明白
        '''



print Solution().maxSubArray([-1, -2])