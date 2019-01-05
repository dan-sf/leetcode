""" Problem statement: https://leetcode.com/problems/univalued-binary-tree/ """

import lib.tree_util as tu

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def _is_unival(node, val):
            if node is not None:
                if node.val != val:
                    return False
                return _is_unival(node.left, val) and _is_unival(node.right, val)
            return True
        return _is_unival(root, root.val)

if __name__ == '__main__':
    s = Solution()
    print(s.isUnivalTree(tu.deserialize('[1,1,1,1,1,null,1]')))
    print(s.isUnivalTree(tu.deserialize('[2,2,2,5,2]')))

