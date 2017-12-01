#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        没意思
        '''
        return 0 if not s else len(s.strip().split(" ")[-1])

