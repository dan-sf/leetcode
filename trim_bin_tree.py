""" Problem statement: https://leetcode.com/problems/trim-a-binary-search-tree/description/ """

from lib.tree_util import deserialize, serialize, bst, bst2, copy_tree

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        def _get_next(root, L, R):
            if root is None or L <= root.val <= R:
                return root
            return _get_next(root.left, L, R) or _get_next(root.right, L, R)

        def _trim_tree(root, parent, L, R):
            if root != None:
                if root.val < L:
                    parent.left = _get_next(root.right, L, R)
                elif root.val > R:
                    parent.right = _get_next(root.left, L, R)
                _trim_tree(root.left, root, L, R)
                _trim_tree(root.right, root, L, R)

        root = _get_next(root, L, R)
        _trim_tree(root, None, L, R)

        return root

def test(actual, expected):
    sys.stdout.write("Expected: {}, Actual: {} ... ".format(expected, actual))
    assert actual == expected
    sys.stdout.write("Success\n")

def run(s, node, L, R, expected):
    tnode = copy_tree(node)
    test(serialize(s.trimBST(tnode, L, R)), expected)

if __name__ == '__main__':
    import sys
    s = Solution()

    ex1 = deserialize('[1,0,2]')
    ex2 = deserialize('[3,0,4,null,2,null,null,1]')

    run(s, ex1, 1, 2, '[1,null,2]')
    run(s, ex2, 1, 3, '[3,2,null,1]')

    run(s, bst, 2, 5, '[5,3,null,2,4]')
    run(s, bst, 0, 4, '[3,2,4]')
    run(s, bst, -4, 0, '[]')
    run(s, bst, 9, 11, '[9]')
    run(s, bst, 3, 7, '[5,3,7,null,4]')
    run(s, bst, 4, 5, '[5,4]')
    run(s, bst, 7, 10, '[8,7,9]')

    run(s, bst2, 2, 17, '[10,5,15,3,7,null,17]')
    run(s, bst2, 2, 9, '[5,3,7]')
    run(s, bst2, 10, 17, '[10,null,15,null,17]')
    run(s, bst2, 5, 21, '[20,10,null,5,15,null,7,null,17]')
    run(s, bst2, 5, 19, '[10,5,15,null,7,null,17]')

    w = deserialize('[2,0,33,null,1,25,40,null,null,11,31,34,45,10,18,29,32,null,36,43,46,4,null,12,24,26,30,null,null,35,39,42,44,null,48,3,9,null,14,22,null,null,27,null,null,null,null,38,null,41,null,null,null,47,49,null,null,5,null,13,15,21,23,null,28,37,null,null,null,null,null,null,null,null,8,null,null,null,17,19,null,null,null,null,null,null,null,7,null,16,null,null,20,6]')
    run(s, w, 25, 26, '[25,null,26]')

