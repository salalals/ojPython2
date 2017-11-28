#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        '''
        没意思, brute force n^2 超时 
        '''
        max_area = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                area = min([height[i], height[j]]) * (j - i)
                max_area = max([max_area, area])
        return max_area



class Solution2(object):
    def maxArea(self, height):
        '''
        哪一边短就缩短哪一边，如果一样长就随便缩短一边。
        正确性懒得验证。
        '''
        max_area = 0
        i = 0
        j = len(height) - 1
        while j > i:
            max_area = max([max_area, min([height[i], height[j]]) * (j - i)])
            if height[i] > height[j]:
                j = j - 1
            else:
                i = i + 1
        return max_area
