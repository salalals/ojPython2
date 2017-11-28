#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        '''
        搞了半天还是超时, 懒得弄了，解法没错，最优解就是n^2 
        先排序，然后3个index变化的时候可以直接检验重复
        '''
        if len(nums) < 3:
            return []
        nums.sort()
        result = list()

        first_num_index = 0
        while first_num_index < (len(nums) - 2):
            left_index = first_num_index + 1
            right_index = len(nums) - 1
            while right_index > left_index:
                triple_sum = sum([nums[first_num_index], nums[left_index], nums[right_index]])
                if triple_sum == 0:
                    result.append([nums[first_num_index], nums[left_index], nums[right_index]])
                    left_index = self.move_index(nums, left_index, 1, right_index)
                    right_index = self.move_index(nums, right_index, -1, left_index)
                elif triple_sum > 0:
                    right_index = self.move_index(nums, right_index, -1, left_index)
                else:
                    left_index = self.move_index(nums, left_index, 1, right_index)

            first_num_index = self.move_index(nums, first_num_index, 1, (len(nums) - 2))
        return result

    def move_index(self, nums, index, direction, limit):
        index = index + direction
        while (index > limit if direction == -1 else index < limit) and nums[index] == nums[index - direction]:
            index = index + direction
        return index

