"""
Q387
Given a string, find the first non-repeating character in it and return it's
index. If it doesn't exist, return -1.
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_count = {}
        for ch in s:
            if ch not in char_count:
                char_count[ch] = 1
            else:
                char_count[ch] += 1
        for i, ch in enumerate(s):
            if char_count[ch] == 1:
                return i
        return -1

if __name__ == '__main__':
    s = Solution()
    print s.firstUniqChar('leetcode')
    print s.firstUniqChar('loveleetcode')
    print s.firstUniqChar('')

