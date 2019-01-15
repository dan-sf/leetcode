""" Problem statement: https://leetcode.com/problems/maximum-depth-of-n-ary-tree/ """

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        self.max_depth = 0

        def _max_depth(node, level):
            if node:
                if level > self.max_depth:
                    self.max_depth = level
                for n in node.children:
                    _max_depth(n, level+1)
        _max_depth(root, 1)
        return self.max_depth

