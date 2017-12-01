#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        '''
        动态规划可以，但是简单来讲就是组合 C(m - 1, m + n - 2) == C(n - 1, m + n - 2)
        (m+n-2)! / (m-1)! * (n-1)!
        '''
        return 1 if m == 1 or n == 1 else self.factorial(m+n-2) / self.factorial(m-1) / self.factorial(n-1)

    def factorial(self, n):
        return reduce(lambda x, y: x * y, range(1, n+1))
