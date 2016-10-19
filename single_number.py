"""
Given an array of integers, every element appears twice except for one. Find
that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it
without using extra memory?
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        for i in nums:
            if i in s:
                s.remove(i)
            else:
                s.add(i)
        for num in s:
            return num

    # Interesting fast solution using xor and reduce:
    # singleNumber([1,1,2,2,3,4,4]) -> ((((((1^1)^2)^2)^3)^4)^4)
    # x ^ y -> outputs x if x!=0 else output 0
    def singleNumberFast(nums):
        return reduce(lambda x,y: x ^ y, nums)

if __name__ == '__main__':
    print singleNumber([1,1,2,2,3,4,4,5,5])
    print singleNumber([1,2,2,3,3,4,4,5,5])
    print singleNumber([1,1,2,2,3,3,4,4,5])

