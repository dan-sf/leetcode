""" Problem statement: https://leetcode.com/problems/search-insert-position/ """

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i, n in enumerate(nums):
            if n > target:
                return i
            elif n == target:
                return i
        return i + 1

    def searchInsertBin(self, nums, target):
        """ Binary search for the index, faster solution """
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) / 2
            if nums[mid] < target:
                start = mid + 1
            else:
                if nums[mid] == target and nums[mid-1] != target:
                    return mid
                end = mid-1
        return start

if __name__ == '__main__':
    s = Solution()

    print s.searchInsert([1,2,3], 2)
    print s.searchInsert([1,2,3], 4)
    print s.searchInsert([1,2,3], -1)
    print s.searchInsert([1,2,3], 1)
    print s.searchInsert([1,2,10], 7)
    print s.searchInsert([1,2,2,2,2,10], 7)
    print s.searchInsert([1,2,2,2,2,10], 2)

