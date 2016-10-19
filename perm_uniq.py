"""
Given a collection of numbers that might contain duplicates, return all
possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

# This solution takes too long
# find a quicker algo
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        mem = []
        self.perms([],nums, output, mem)
        return output
    def perms(self, prefix, nums, output, mem):
        l = len(nums)
        if l == 0:
            output.append(prefix)
        else:
            for i in range(l):
                args = (prefix + [nums[i]], nums[0:i] + nums[i+1:l])
                if args not in mem:
                    self.perms(args[0], args[1], output, mem)
                    mem.append(args)

if __name__ == '__main__':
    s = Solution()
    print s.permuteUnique([3,3,1,2,3,2,3,1])

