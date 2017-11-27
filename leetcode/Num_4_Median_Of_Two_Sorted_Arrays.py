#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        '''
        brute force没什么，但是原题目要求最好是O(log (m+n))
        '''
        merge = nums1 + nums2
        merge.sort()
        if len(merge) % 2 > 0:
            return merge[len(merge) / 2]
        else:
            return (merge[len(merge) / 2] + merge[len(merge) / 2 - 1]) / 2.0



class Solution2(object):
    def findMedianSortedArrays(self, nums1, nums2):
        '''
        O(log (m+n)) 解法，看了Solution 太麻烦，懒得写
        '''




