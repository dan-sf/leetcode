""" Problem statement: https://leetcode.com/problems/merge-two-binary-trees/description/ """

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 != None and t2 != None:
            queue = [ (t1, t2) ]
        else:
            return t1 or t2

        root = t1
        while len(queue) != 0:
            n1, n2 = queue.pop(0)

            n1.val += n2.val
            if n1.left is None or n2.left is None:
                n1.left = n1.left or n2.left
            else:
                queue.append((n1.left, n2.left))
            if n1.right is None or n2.right is None:
                n1.right = n1.right or n2.right
            else:
                queue.append((n1.right, n2.right))
        return root

if __name__ == '__main__':
    from lib.tree_deserializer import *
    t1 = deserialize('[1,3,2,5]')
    t2 = deserialize('[2,1,3,null,4,null,7]')

    s = Solution()
    r = s.mergeTrees(t1, t2)
    drawtree(r)

