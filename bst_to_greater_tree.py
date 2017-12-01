""" Problem statement: https://leetcode.com/problems/convert-bst-to-greater-tree/description/ """

from lib.tree_deserializer import *

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        class _int_p(object):
            val = 0
        def traverse(root):
            if root == None:
                return
            traverse(root.right)
            root.val += _int_p.val
            _int_p.val = root.val
            traverse(root.left)
        traverse(root)
        return root

    def convertBST_slow(self, root):
        """
        Original slow solution to this problem (TLE)
        """
        return self.create_greater_tree(root, root)

    def create_greater_tree(self, node, root):
        if node == None:
            return node
        greater_sum = node.val + self.sum_greater(root, node.val)
        n = TreeNode(greater_sum)
        n.left = self.create_greater_tree(node.left, root)
        n.right = self.create_greater_tree(node.right, root)
        return n

    def sum_greater(self, node, val):
        if node == None:
            return 0
        elif node.val > val:
            return node.val + self.sum_greater(node.left, val) + self.sum_greater(node.right, val)
        else:
            return self.sum_greater(node.right, val)

if __name__ == '__main__':
    s = Solution()

    t = deserialize('[5,2,13]')
    s.convertBST(t)
    assert serialize(t) == [18, 13, 20]

    t = deserialize('[0,-3,2,-4,null,1]')
    s.convertBST(t)
    assert serialize(t) == [3, 2, 3, 0, -4]

    t = deserialize('[4,2,6,1,3,5,7]')
    s.convertBST(t)
    assert serialize(t) == [22, 13, 7, 18, 27, 25, 28]

