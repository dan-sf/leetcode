"""
Q231. Given an integer, write a function to determine if it is a power of two.
"""

import math
from collections import Counter

class Solution(object):
    def isPowerOfTwoLog(self, n):
        """
        :type n: int
        :rtype: bool

        A more math solution with log, however, doesn't work with large numbers
        due to rounding errors: math.pow(X, Y) = Z => math.log(Z, X) = Y
        """
        if n > 0 and math.log(n ,2) == math.floor(math.log(n ,2)):
            return True
        return False

    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        
        Basic loop solution
        """
        if n <= 0:
            return False

        n = float(n)
        while n != 1:
            n = n / 2
            if n != math.floor(n):
                return False
        return True

    def isPowerOfTwoBin(self, n):
        """
        :type n: int
        :rtype: bool

        Binary conversion solution
        """
        if n <= 0:
            return False
        return bin(n).count('1') == 1

if __name__ == '__main__':
    s = Solution()

    for i in range(10000):
        if s.isPowerOfTwo(i):
            print i, s.isPowerOfTwo(i)

