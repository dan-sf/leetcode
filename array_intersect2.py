"""
Q350. Given two arrays, write a function to compute their intersection.

Example:
    Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

    Note:
        Each element in the result should appear as many times as it shows in
        both arrays.  The result can be in any order.
"""

from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        output = []
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        s1 = set(nums1)
        s2 = set(nums2)
        intersect = s1.intersection(s2)

        for element in intersect:
            if c1[element] < c2[element]:
                output += [element] * c1[element]
            else:
                output += [element] * c2[element]

        return output

if __name__ == '__main__':
    s = Solution()
    print s.intersect([1,2,2,33,3,3], [1,2,2,3,3,3,3])
    print s.intersect([3,1,2], [1,1])

