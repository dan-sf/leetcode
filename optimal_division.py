""" Problem statement: https://leetcode.com/problems/optimal-division/description/ """

class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) <= 2:
            return '/'.join(map(str, nums))
        return '{}/({})'.format(str(nums[0]), '/'.join(map(str, nums[1:])))

if __name__ == '__main__':
    s = Solution()
    print s.optimalDivision([505, 327, 155, 314,1,2,3])
    print s.optimalDivision([1000,100,10,2])
    print s.optimalDivision([505])
    print s.optimalDivision([2,3])

