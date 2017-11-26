#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        time limit exceeded
        '''
        longest_length = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if len(set(s[i:j])) < len(s[i:j]):
                    continue
                else:
                    longest_length = \
                        longest_length \
                            if len(s[i:j]) < longest_length \
                            else len(s[i:j])
        return longest_length


class Solution2(object):
    def lengthOfLongestSubstring(self, s):
        '''
        sliding window..
        i, j 开始都是0，然后j开始增长
        如果s[i,j+1]出现重复，说明从i开始的substring最长就到这里了，所以i可以增长一个,重新验证
        '''
        longest_length = 0
        i, j = 0, 0
        char_set = set()
        while j < len(s):
            if s[j] not in char_set:
                char_set.add(s[j])
                j = j + 1
                longest_length = longest_length if (j - i) < longest_length else (j - i)
            else:
                if s[i] == s[j]:
                    i = i + 1
                    j = j + 1
                else:
                    char_set.remove(s[i])
                    i = i + 1
        return longest_length
