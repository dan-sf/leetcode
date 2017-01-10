""" Problem statement: https://leetcode.com/problems/power-of-three/ """

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n % 3 != 0 or n == 0:
            return False
        return self.isPowerOfThree(n/3)

if __name__ == '__main__':
    s = Solution()

    print s.isPowerOfThree(27)
    print s.isPowerOfThree(9)
    print s.isPowerOfThree(81)
    print s.isPowerOfThree(10)
    print s.isPowerOfThree(1234)

