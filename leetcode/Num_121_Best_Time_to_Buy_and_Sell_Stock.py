#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        '''
        超时了
        '''
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                max_profit = max([max_profit, prices[j] - prices[i]])
        return max_profit



class Solution2(object):
    def maxProfit(self, prices):
        max_profit = 0
        for i in range(len(prices) - 1):
            if prices[i] >= prices[i + 1]:
                continue
            for j in range(i+1, len(prices)):
                max_profit = max([max_profit, prices[j] - prices[i]])
        return max_profit