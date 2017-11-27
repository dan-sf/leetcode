""" Problem statement: https://leetcode.com/problems/maximum-subarray/description/ """

class Solution(object):
    def maxSubArraySlow(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = nums[0]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sub_sum = sum(nums[i:j+1])
                if sub_sum > max_val:
                    max_val = sub_sum
        return max_val

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        running_max = nums[0]
        current_max = nums[0]
        for i in range(1, len(nums)):
            current_max = max(current_max+nums[i], nums[i])
            running_max = max(running_max, current_max)
        return running_max

if __name__ == '__main__':
    s = Solution()

    print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), s.maxSubArraySlow([-2,1,-3,4,-1,2,1,-5,4])
    print s.maxSubArray([-2,1,-3,4,-1,2,1,5,4]), s.maxSubArraySlow([-2,1,-3,4,-1,2,1,5,4])
    print s.maxSubArray([4,3,2]), s.maxSubArraySlow([4,3,2])
    print s.maxSubArray([4,3,2,-10]), s.maxSubArraySlow([4,3,2,-10])
    print s.maxSubArray(range(10)), s.maxSubArraySlow(range(10))

