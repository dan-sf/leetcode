""" Problem statement: https://leetcode.com/problems/longest-substring-without-repeating-characters/ """

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Initial solution, passes, but isn't that fast...
        if not s:
            return 0
        if len(s) == 1:
            return 1

        output = ''
        start = 0
        end = 1

        def is_unique(s):
            return len(s) == len(set(s))

        while end <= len(s):
            substr = s[start:end]
            if is_unique(substr):
                if len(substr) > len(output):
                    output = substr
                end += 1
            else:
                if start < end:
                    start += 1
        return len(output)

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Improved solution from leetcode, this is much cleaner
        slen = len(s)
        check = set()
        ans, i, j = 0, 0, 0

        while i < slen and j < slen:
            if s[j] not in check:
                check.add(s[j])
                j += 1
                ans = max(ans, j - i)
            else:
                check.remove(s[i])
                i += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring('abcabcbb'))
    print(s.lengthOfLongestSubstring('bbbbb'))
    print(s.lengthOfLongestSubstring('pwwkew'))
    print(s.lengthOfLongestSubstring('x'))
    print(s.lengthOfLongestSubstring('xx'))
    print(s.lengthOfLongestSubstring('au'))

