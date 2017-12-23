""" Problem statement: https://leetcode.com/problems/construct-string-from-binary-tree/description/ """

from lib.tree_util import *

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is not None:
            val = str(t.val)
            if t.left is None and t.right is None:
                output = val
            elif t.left is None:
                output = '{}()({})'.format(val, self.tree2str(t.right))
            elif t.right is None:
                output = '{}({})'.format(val, self.tree2str(t.left))
            else:
                output = '{}({})({})'.format(val, self.tree2str(t.left), self.tree2str(t.right))
        else:
            return ''

        return output

def test(s, stree, expected):
    tree = deserialize(stree)
    actual = s.tree2str(tree)
    print 'Testing -> expected: {}, actual {}'.format(expected, actual)
    assert expected == actual

if __name__ == '__main__':
    s = Solution()
    test(s, '[1,2,3,4]', '1(2(4))(3)')
    test(s, '[1,2,3,null,4]', '1(2()(4))(3)')
    test(s, '[20,10,30,5,15,null,null,3,7,null,17]', '20(10(5(3)(7))(15()(17)))(30)')

