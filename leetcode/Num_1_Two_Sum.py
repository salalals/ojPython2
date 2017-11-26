#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        pass


class Solution2(object):
    def twoSum(self, nums, target):
        """
        这解法耍了个巧，如果一个数字出现了两次以上，那么第二次或以后也的value值是index
        所以在做hash搜索的时候搜到的肯定不是现在的自己
        """
        num_dict = dict(zip(nums, range(len(nums))))
        for i in range(len(nums)):
            left = target - nums[i]
            if num_dict.has_key(left) and num_dict.get(left) != i:
                return [i, num_dict.get(left)]
        raise Exception()






