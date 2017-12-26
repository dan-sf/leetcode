""" Problem statement: https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/ """

from lib.tree_util import *

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        def _traverse(node, level=1):
            if node is not None:
                if len(output) < level:
                    output.append(node.val)
                elif node.val > output[level-1]:
                    output[level-1] = node.val
                _traverse(node.left, level+1)
                _traverse(node.right, level+1)
        _traverse(root)
        return output

def test(f, stree, expected):
    tree = deserialize(stree)
    actual = f(tree)
    print 'Testing -> expected: {}, actual {}'.format(expected, actual)
    assert expected == actual

if __name__ == '__main__':
    s = Solution()

    test(s.largestValues, '[1,3,2,5,3,null,9]', [1, 3, 9])
    test(s.largestValues, '[4]', [4])
    test(s.largestValues, '[1,2,3,null,null,4,null,null,5]', [1,3,4,5])
    test(s.largestValues, '[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]', [2,3,9,8,7])
    test(s.largestValues, '[]', [])

