#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
这个是2013年实习面试题目
'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        超时了
        '''
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max([self.rob(nums[1:]), nums[0] + self.rob(nums[2:])])


class Solution2(object):
    '''
    当年憋了半个多小时也没写出来的DP，现在一下子就弄出来了
    '''
    def rob(self, nums):
        if not nums:
            return 0

        dp_array = [0] * len(nums)
        for ind in range(len(dp_array))[::-1]:
            if ind == len(dp_array) - 1:
                dp_array[ind] = nums[ind]
            elif ind == len(dp_array) - 2:
                dp_array[ind] = max([nums[ind], nums[ind + 1]])
            else:
                dp_array[ind] = max([nums[ind] + dp_array[ind + 2], dp_array[ind + 1]])
        return dp_array[0]





