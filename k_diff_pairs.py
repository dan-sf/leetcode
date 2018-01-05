""" Problem statement: https://leetcode.com/problems/k-diff-pairs-in-an-array/description/ """

from collections import Counter

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0

        count = Counter(nums)
        if k == 0:
            return sum(map(lambda r: 0 if count[r] // 2 == 0 else 1, count))

        total = 0
        for key in count:
            if key + k in count:
                total += 1
        return total

def test(f, nums, k, expected):
    actual = f(nums, k)
    print 'Testing ---> actual: {}, expected: {}'.format(actual, expected)
    assert actual == expected

if __name__ == '__main__':
    s = Solution()

    test(s.findPairs, range(6), 3, 3)
    test(s.findPairs, [1, 3, 1, 5, 4], 0, 1)
    test(s.findPairs, [1,2,3,-2,-4,-8], 5, 2)
    test(s.findPairs, [1, 3, 1, 5, 4], 0, 1)
    test(s.findPairs, [-5,0,5], 5, 2)
    test(s.findPairs, [1,2,3,4,5], -1, 0)

