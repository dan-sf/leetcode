""" Problem statement: https://leetcode.com/problems/average-of-levels-in-binary-tree/description/ """

from lib.tree_deserializer import *

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        levels = {}
        def _traverse(root, level=0):
            if root != None:
                if level in levels:
                    levels[level].append(root.val)
                else:
                    levels[level] = [ root.val ]
                _traverse(root.left, level + 1)
                _traverse(root.right, level + 1)

        _traverse(root, 0)
        output = []
        for level in levels:
            output.append( float(sum(levels[level])) / len(levels[level]) )
        return output

    def _averageOfLevels(self, root):
        """
        Nice BFS solution found in discuss
        """
        level = [ root ]
        averages = []
        while len(level) != 0:
            averages.append(float(sum(l.val for l in level)) / len(level))
            level = [kid for node in level for kid in (node.left, node.right) if kid]
        return averages

if __name__ == '__main__':
    s = Solution()
    print s._averageOfLevels(ex_one)

