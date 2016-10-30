"""
Q349
Given two arrays, write a function to compute their intersection.

Example:
    Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        output = nums1.intersection(nums2)
        return list(output)

if __name__ == '__main__':
    s = Solution()
    print s.intersection([1, 2, 2, 1], [2, 2])

