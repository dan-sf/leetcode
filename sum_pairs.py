""" Problem statement: https://leetcode.com/problems/array-partition-i/description/ """

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        buff = []
        output = 0
        # The problem isn't explicit about the nums needed to be sorted, which
        # is probably why it has been down voted so many times. I only added
        # this after testing with run code
        nums.sort()
        for i in nums:
            if len(buff) < 2:
                buff.append(i)
            else:
                output += min(buff)
                buff = [i]

        if len(buff) == 2:
            output += min(buff)
        elif len(buff) == 1:
            output += buff[0]

        return output

if __name__ == '__main__':

    s = Solution()

    print(s.arrayPairSum([1,4,3,2]))

