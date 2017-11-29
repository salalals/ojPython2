#!/usr/bin/python
# -*- coding: utf-8 -*-

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        header = ListNode(0)
        pointer = header
        carrier = 0
        while l1 is not None and l2 is not None:
            pointer_sum = l1.val + l2.val + carrier
            if pointer_sum >= 10:
                carrier = 1
                pointer.next = ListNode(pointer_sum - 10)
            else:
                carrier = 0
                pointer.next = ListNode(pointer_sum)
            pointer = pointer.next
            l1 = l1.next
            l2 = l2.next

        if l1 is None and l2 is None:
            if carrier == 1:
                pointer.next = ListNode(1)
            return header.next


        if l1 is None:
            left_over = l2
        else:
            left_over = l1

        while left_over is not None:
            pointer_sum = left_over.val + carrier
            if pointer_sum >= 10:
                carrier = 1
                pointer.next = ListNode(pointer_sum - 10)
            else:
                carrier = 0
                pointer.next = ListNode(pointer_sum)
            pointer = pointer.next
            left_over = left_over.next

        if carrier == 1:
            pointer.next = ListNode(1)
        return header.next


class Solution2(object):
    '''
    更简洁的写法
    python中的 x = stat ? a : b 的形式是 x = a if stat else b
    '''
    def addTwoNumbers(self, l1, l2):
        header = ListNode(None)
        tail = header
        carrier = 0;
        while l1 is not None or l2 is not None or carrier > 0:
            x = 0 if l1 is None else l1.val
            y = 0 if l2 is None else l2.val
            sum = x + y + carrier
            carrier = 1 if sum >= 10 else 0
            digit = sum if carrier == 0 else (sum - 10)
            tail.next = ListNode(digit)
            tail = tail.next
            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next
        return header.next








