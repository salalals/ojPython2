#!/usr/bin/python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        '''
        最简单的递归实现
        '''
        result = list()
        self.populate_post_order_traverse(root, result)
        return result


    def populate_post_order_traverse(self, node, result):
        if not node:
            return
        self.populate_post_order_traverse(node.left, result)
        self.populate_post_order_traverse(node.right, result)
        result.append(node.val)



class Solution2(object):
    def postorderTraversal(self, root):
        '''
        使用stack进行深度搜索
        使用set记录第一次访问过的节点
        '''
        stack = list()
        visited_set = set()
        result = list()
        stack.append(root)
        while len(stack) > 0:
            top = stack.pop()
            if not top:
                continue
            if top not in visited_set:
                visited_set.add(top)
                stack.append(top)
                stack.append(top.right)
                stack.append(top.left)
            else:
                result.append(top.val)
        return result


a = [1,2,3]
print a.pop()
print a
