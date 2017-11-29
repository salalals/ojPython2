#!/usr/bin/python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        '''
        没意思，超时了，但是Solution说这样可以, O(kN)
        k way merge
        '''
        header = ListNode(None)
        pointer = header
        while any(lists):
            # list_node = reduce(lambda n1, n2: n1 if n2 is None or n1 is not None and n1.val <= n2.val else n2, lists)
            smallest_val = None
            smallest_val_index = None
            for i in range(len(lists)):
                if lists[i] is not None and (smallest_val is None or lists[i].val < smallest_val):
                    smallest_val = lists[i].val
                    smallest_val_index = i
            pointer.next = lists[smallest_val_index]
            pointer = pointer.next
            lists[smallest_val_index] = lists[smallest_val_index].next
        return header.next


class Solution2(object):
    def mergeKLists(self, lists):
        '''
        reduce两两merge减少一些无用的比较，还是超时了
        '''
        return None if not any(lists) else reduce(lambda l1, l2: self.mergeTwoLists(l1, l2), lists)


    def mergeTwoLists(self, l1, l2):
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


class Solution3(object):
    def mergeKLists(self, lists):
        '''
        树形两两merge减少无用比较, 通过了
        '''
        '''
        注意Python的for循环实现partition
        '''
        if not any(lists):
            return None

        partition = lists
        while True:
            partition = [partition[i:i + 2] for i in range(0, len(partition), 2)]
            partition = [ele for ele in map(lambda sub: self.mergeTwoLists(sub[0], sub[1]) if len(sub) > 1 else sub[0], partition)]
            if len(partition) == 1:
                break
        return partition[0]

    def mergeTwoLists(self, l1, l2):
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
