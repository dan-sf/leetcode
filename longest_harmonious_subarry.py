""" Problem statement: https://leetcode.com/problems/longest-harmonious-subsequence/description/ """

from collections import Counter

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        cnums = Counter(nums)
        for k in cnums:
            if k+1 in cnums:
                sub_count = cnums[k+1] + cnums[k]
                if sub_count > longest:
                    longest = sub_count
        return longest

if __name__ == '__main__':
    s = Solution()
    print s.findLHS([1,3,2,2,5,2,3,7])
    print s.findLHS(range(10))
    print s.findLHS([1,1,1,1,1,3])
    print s.findLHS([1,1,1,2,1,1])
    print s.findLHS([1])
    print s.findLHS([])
    print s.findLHS([1,1,1,2,1,22,1,8,1])

