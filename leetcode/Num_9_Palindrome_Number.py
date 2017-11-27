#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        '''
        没意思，
        注意边界条件，不使用extra space
        edge case 比如 10001 这种
        '''
        '''
        写法比较tricky，没什么意思
        '''
        if x == 0:
            return True
        if x % 10 == 0:
            return False

        half_reverted = 0

        # 从个位开始把x里面的数字拿到 half_reverted，然后把这个数字从x里面删除掉
        while x > half_reverted:
            half_reverted = half_reverted * 10 + x % 10
            x = x / 10

        return x == half_reverted or x == half_reverted / 10


