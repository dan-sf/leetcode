"""
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9

to

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""

class Solution(object):
    def swap(self, node):
        if node is not None:
            node.left, node.right = node.right, node.left
            self.swap(node.left)
            self.swap(node.right)

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        else:
            self.swap(root)
            return root

if __name__ == '__main__':
    class TreeNode(object):
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    def print_tree(node):
        print node.val
        if node.left is not None:
            print_tree(node.left)
        if node.right is not None:
            print_tree(node.right)

    s = Solution()

    root = TreeNode(4)

    root.left = TreeNode(2)
    root.right = TreeNode(7)

    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    print_tree(root)
    print
    print_tree(s.invertTree(root))

