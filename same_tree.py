"""
Q100
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and
the nodes have the same value.
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def xor_none(self, a, b):
        return (a is None) != (b is None)

    def isSameTree(self, p, q):
        if self.xor_none(p,q):
            return False
        if (q is None) and (p is None):
            return True
        level = [(p,q)]

        while level:
            q = []
            for node1, node2 in level:
                if node1.val != node2.val:
                    return False

                if node1.left and node2.left:
                    q.append( (node1.left, node2.left) )
                if self.xor_none(node1.left, node2.left):
                    return False

                if node1.right and node2.right:
                    q.append( (node1.right, node2.right) )
                if self.xor_none(node1.right, node2.right):
                    return False

            level = q

        return True

    def isSameTreeRecursive(self,p,q):
        """Recursive solution useing BFS"""
        if (p is None) and (q is None):
            return True
        if self.xor_none(p,q):
            return False
        return (p.val == q.val) and \
               self.isSameTreeRecursive(p.left,q.left) and \
               self.isSameTreeRecursive(p.right,q.right)

if __name__ == '__main__':

    s = Solution()

    tree1 = TreeNode(1)
    tree1.left = TreeNode(1)
    tree1.right = TreeNode(1)
    tree1.left.right = TreeNode(1)

    tree2 = TreeNode(1)

    assert(s.isSameTree(tree1, tree2) is False)

    tree1 = TreeNode(1)
    tree1.left = TreeNode(1)

    tree2 = None

    assert(s.isSameTree(tree1, tree2) is False)

    tree1 = TreeNode(1)
    tree1.left = TreeNode(1)
    tree1.left.left = TreeNode(1)

    tree2 = TreeNode(1)
    tree2.left = TreeNode(1)
    tree2.left.left = TreeNode(1)

    assert(s.isSameTree(tree1, tree2) is True)

    tree1 = TreeNode(1)

    tree2 = TreeNode(1)

    assert(s.isSameTree(tree1, tree2) is True)

    tree1 = TreeNode(0)
    tree1.left = TreeNode(-5)

    tree2 = TreeNode(0)
    tree2.left = TreeNode(-8)

    assert(s.isSameTree(tree1, tree2) is False)

    tree1 = TreeNode(0)

    tree2 = TreeNode(1)

    assert(s.isSameTree(tree1, tree2) is False)

