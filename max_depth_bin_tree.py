"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root
node down to the farthest leaf node.
"""

class Solution(object):
    """
    Visit all nodes in the tree, counting levels as you go. Once you get to the
    last node add that level to a list then return the max level from that
    list.
    """
    def visit(self, node, level, end_points):
        if node.right == None and node.left == None:
            end_points.append(level)
        if node.left != None:
            self.visit(node.left, level+1, end_points)
        if node.right != None:
            self.visit(node.right, level+1, end_points)
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            ends = []
            self.visit(root, 1, ends)
            return max(ends)

if __name__ == '__main__':
    """Solution tests"""
    class TreeNode(object):
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    root = TreeNode(3)
    root.left = TreeNode(3)
    root.right = TreeNode(3)

    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(3)

    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(3)
    root.left.right.right = TreeNode(3)

    s = Solution()
    print s.maxDepth(root)

