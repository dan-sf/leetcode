""" Problem statement: https://leetcode.com/problems/max-consecutive-ones/description/ """

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_max = 0
        final_max = 0

        for n in nums:
            if n:
                current_max += n
            else:
                if current_max > final_max:
                    final_max = current_max
                current_max = n

        return max(final_max, current_max)

    def findMaxConsecutiveOnesShort(self, nums):
        """
        Interesting one liner from Discuss
        """
        return max(map(len, ''.join(map(str, nums)).split('0')))

if __name__ == '__main__':
    s = Solution()
    print s.findMaxConsecutiveOnes([1,0,1,1,0,1])

