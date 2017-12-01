#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        '''
        按照是否包含第一个元素做 尾递归 即可
        sol = include_first + exclude_first
        '''

        return self.combine_arr(range(1, n + 1), k)


    def combine_arr(self, arr, k):
        if not arr or len(arr) < k:
            return []

        if k == 1:
            return [[ele] for ele in arr]

        include_first = self.combine_arr(arr[1:], k - 1)
        include_first = map(lambda sol: [arr[0]] + sol, include_first)

        exclude_first = self.combine_arr(arr[1:], k)
        return include_first + exclude_first



