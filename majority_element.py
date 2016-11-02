"""
Q169. Given an array of size n, find the majority element. The majority element
is the element that appears more than n/2 times.

You may assume that the array is non-empty and the majority element always
exist in the array.
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj_count = len(nums)/2.0
        hold = {}

        for i in nums:
            if i not in hold:
                hold[i] = 1
                if maj_count <= 1:
                    return i
            else:
                hold[i] += 1

            if hold[i] >= maj_count:
                return i

    def majorityElementCounter(self, nums):
        from collections import Counter
        c = Counter(nums)
        for i in nums:
            if c[i] > len(nums)/2:
                return i

