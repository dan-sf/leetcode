""" Problem statement: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/ """

from lib import tree_util as t

class Solution(object):
    def levelOrderBottom(self, root):
        """
        Even though this question asks for level order, use depth first search
        to keep track of the levels of the tree. Just append values at each
        level pre-order dfs then reverse the output array
        """
        output = []
        def dfs(node, level=1):
            if node != None:
                if len(output) < level:
                    output.append([])
                output[level-1].append(node.val)
                dfs(node.left, level+1)
                dfs(node.right, level+1)
        dfs(root)
        output.reverse()
        return output

if __name__ == '__main__':
    s = Solution()

    print s.levelOrderBottom(t.deserialize('[3,9,20,null,null,15,7]'))
    print s.levelOrderBottom(t.deserialize('[1]'))
    print s.levelOrderBottom(t.deserialize('[3,null,4,null,5]'))
    print s.levelOrderBottom(t.deserialize('[3,4,null,5]'))

