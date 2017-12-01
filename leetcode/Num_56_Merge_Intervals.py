#!/usr/bin/python
# -*- coding: utf-8 -*-

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        '''
        没意思，先按照start排序，然后按照end进行merge
        '''
        if not intervals:
            return []
        merged_intervals = list()
        sorted_intervals = sorted(intervals, key=lambda interval: interval.start)
        current_interval = sorted_intervals[0]
        next = 1
        while next < len(intervals):
            if current_interval.end >= sorted_intervals[next].start:
                current_interval = Interval(current_interval.start, max(current_interval.end, sorted_intervals[next].end))
            else:
                merged_intervals.append(current_interval)
                current_interval = sorted_intervals[next]
            next = next + 1
        merged_intervals.append(current_interval)
        return merged_intervals
