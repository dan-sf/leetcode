""" Problem statement: https://leetcode.com/problems/binary-number-with-alternating-bits/description/ """

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bin_str = bin(n)
        if '00' in bin_str or '11' in bin_str:
            return False
        return True

if __name__ == '__main__':
    s = Solution()
    print s.hasAlternatingBits(5)
    print s.hasAlternatingBits(7)
    print s.hasAlternatingBits(11)
    print s.hasAlternatingBits(10)

