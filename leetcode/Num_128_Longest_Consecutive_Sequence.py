#!/usr/bin/python
# -*- coding: utf-8 -*-


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        现去重排序，然后前后两个index
        O(nlgn), 不符合O(n)要求
        '''
        if not nums:
            return 0
        nums = sorted(list(set(nums)))

        print nums

        longest_length = 0
        start = 0
        while start < len(nums):
            end = start
            while end < len(nums) - 1 and nums[end + 1] == nums[end] + 1:
                end = end + 1
            longest_length = max([longest_length, end - start + 1])
            start = end + 1
        return longest_length






class Solution2(object):
    def longestConsecutive_brute_force(self, nums):
        '''
        O(n)最优解的思路来自这个brute force解法
        依次查看nums[index] + 1 是否存在于nums中
        '''
        longest_length = 0
        for num in nums:
            end = num
            while end + 1 in nums:
                end = end + 1
            longest_length = max([longest_length, end - num + 1])
        return longest_length

    def longestConsecutive(self, nums):
        '''
        O(n)最优解: 将上边brute force做以下优化
        1. set 去重并且可以hash搜索
        2. 只从longest序列的最小元素开始查找 （关键）
        '''
        nums = set(nums)
        longest_length = 0
        for num in nums:
            if num - 1 not in nums:
                end = num
                while end + 1 in nums:
                    end = end + 1
                longest_length = max([longest_length, end - num + 1])
        return longest_length






