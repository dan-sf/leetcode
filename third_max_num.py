"""
Given an array of integers, return the 3rd Maximum Number in this array, if it
doesn't exist, return the Maximum Number. The time complexity must be O(n) or
less.
"""

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        if (len(nums)<3):
            return max(nums)
        else:
            nums.remove(max(nums))
            nums.remove(max(nums))
            return max(nums)

if __name__ == '__main__':
    s = Solution()
    print s.thirdMax(range(10))
    print s.thirdMax([4,3])
    print s.thirdMax([0])
    print s.thirdMax([0,1,1,2,3])
    print s.thirdMax([1,2,2,5,3,5])

