""" Problem statement: https://leetcode.com/problems/number-of-1-bits/ """

class Solution(object):
    def hammingWeight(self, n):
        """
        Easy solution using python builtins
        """
        return bin(n).count('1')

    def hammingWeightBits(self, n):
        """
        Bit manipulation solution
        """
        count = 0
        bits_needed = 0
        while 1<<bits_needed <= n:
            bits_needed += 1
        # Convert number of bits needed to all 1's
        max_val = (1<<bits_needed) - 1
        # If each bit is a one or not
        for i in range(max_val):
            if 1<<i & n:
                count += 1
        return count

if __name__ == '__main__':
    s = Solution()

    for i in range(20):
        print i, s.hammingWeight(i), s.hammingWeightBits(i)

