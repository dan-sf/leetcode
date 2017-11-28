""" Problem statement: https://leetcode.com/problems/reshape-the-matrix/description/ """

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        flat_matrix = [ i for row in nums for i in row ] # sum(num, []) <- another cool way to flatten this matrix (seen in other solutions)
        if len(flat_matrix) != r * c:
            return nums

        output = []
        m_index = 0
        for row in range(r):
            output.append([])
            for col in range(c):
                output[row].append(flat_matrix[m_index])
                m_index += 1
        return output

if __name__ == '__main__':
    s = Solution()
    print s.matrixReshape([[1,2],[3,4]], 1, 4)
    print s.matrixReshape([[1,2],[3,4]], 1, 5)
    print s.matrixReshape([[1,2],[3,4],[1,1]], 2, 3)

