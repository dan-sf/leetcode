"""
Problem 190: https://leetcode.com/problems/reverse-bits/ @easy

Reverse bits of a given 32 bits unsigned integer.
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        string = bin(n)[2:]
        string = '0' * (32 - len(string)) + string
        output = 0
        for i, ch in enumerate(string):
            if ch == '1':
                output += 1<<i
        return output

class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0
        for i in range(32):
            if 1<<(31-i) & n:
                output += 1<<i
        return output

print(Solution().reverseBits(17))
print(Solution().reverseBits(43261596))

