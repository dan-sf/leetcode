"""
Find the sum of all left leaves in a given binary tree.
"""

class Solution(object):
    def visit_left(self, node, left_leaves):
        if node.left is not None:
            if node.left.right is None and node.left.left is None:
                left_leaves.append(node.left.val)
            self.visit_left(node.left, left_leaves)
        if node.right is not None:
            self.visit_left(node.right, left_leaves)

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        left_leaves = []
        if root is None:
            return 0
        else:
            self.visit_left(root, left_leaves)
            return sum(left_leaves)

if __name__ == '__main__':
    class TreeNode(object):
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    tree = TreeNode(3)

    tree.left = TreeNode(9)
    tree.right = TreeNode(20)

    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)

    s = Solution()
    print s.sumOfLeftLeaves(tree)

