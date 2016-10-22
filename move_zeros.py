"""
Given an array nums, write a function to move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums
should be [1, 3, 12, 0, 0].
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if i == 0:
                nums.append(i)
                nums.remove(0)
        return nums

if __name__ == '__main__':
    s = Solution()

    nums = [0, 1, 0, 3, 12]
    print s.moveZeroes(nums)
    nums = [0, 1, 0, 3, 12]*3
    print s.moveZeroes(nums)
    nums = [0,0,1]
    print s.moveZeroes(nums)

