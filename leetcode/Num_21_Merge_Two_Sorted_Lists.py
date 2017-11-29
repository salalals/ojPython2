#!/usr/bin/python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        '''
        没意思
        '''
        header = ListNode(None)
        pointer = header
        while l1 is not None or l2 is not None:
            if l1 is None:
                pointer.next = l2
                pointer = pointer.next
                l2 = l2.next
            elif l2 is None:
                pointer.next = l1
                pointer = pointer.next
                l1 = l1.next
            else:
                if l1.val <= l2.val:
                    pointer.next = l1
                    pointer = pointer.next
                    l1 = l1.next
                else:
                    pointer.next = l2
                    pointer = pointer.next
                    l2 = l2.next

        return header.next

