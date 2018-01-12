""" Problem statement: https://leetcode.com/problems/find-all-duplicates-in-an-array/description/ """

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        check = set()
        for num in nums:
            if num in check:
                output.append(num)
            else:
                check.add(num)
        return output

if __name__ == '__main__':
    s = Solution()
    print s.findDuplicates([4,3,2,7,8,2,3,1])

