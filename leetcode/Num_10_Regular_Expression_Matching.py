#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        '''
        最快的就是直接使用Python的re包
        '''
        import re
        return re.match(p, s) is not None and re.match(p, s).group() == s

class Solution2(object):
    def isMatch(self, s, p):
        '''
        主要就是针对*的递归，遇到*并且match时，可以砍掉s里面的1个char或者砍掉p里面的2个char，然后继续递归。
        具体edge case没必要深究
        '''
        '''
        python中空串""和None转为bool的时候都是False
        '''

        # 如果p为空，那么s空不空有两种情况。展开写会比较清楚，这里只是做了coding的简化
        if not p:
            return not s

        # s first char matches
        if s.startswith(p[0]) or len(s) > 0 and p[0] == ".":
            if len(p) == 1:
                return len(s) == 1
            else:
                if p[1] == "*":
                    return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
                else:
                    return self.isMatch(s[1:], p[1:])
        else:
            if len(p) <= 1 or p[1] != "*":
                return False
            else:
                return self.isMatch(s, p[2:])

