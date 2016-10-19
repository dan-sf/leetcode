"""
Given a string which consists of lowercase or uppercase letters, find the
length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note: Assume the length of given string will not exceed 1,010.

Example:

Input: "abccccdd"

Output: 7

Explanation: One longest palindrome that can be built is "dccaccd", whose
length is 7.
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        pair = set()
        count = 0
        for ch in s:
            if ch in pair:
                pair.remove(ch)
                count += 1
            else:
                pair.add(ch)
        if len(pair) == 0:
            return len(s)
        else:
            return count*2+1

if __name__ == '__main__':
    s = Solution()
    print s.longest_pal('abccccdd')
    print s.longest_pal('abcb')
    print s.longest_pal('aabbce')

