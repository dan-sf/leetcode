"""
Q242. Given two strings s and t, write a function to determine if t is an
anagram of s.
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = list(s); s.sort()
        t = list(t); t.sort()
        return s == t

if __name__ == '__main__':
    s = Solution()

    print s.isAnagram('anagram', 'nagaram')
    print s.isAnagram('rat', 'car')

