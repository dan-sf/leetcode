""" Problem statement: https://leetcode.com/problems/longest-uncommon-subsequence-i/description/ """

class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        subsets = set()
        if len(a) >= len(b):
            larger, smaller = a, b
        else:
            larger, smaller = b, a

        for i in range(len(larger)):
            for j in range(len(larger)):
                subsets.add(larger[i:j+1])

        longest = -1
        for s in sorted(subsets, key=lambda x: len(x), reverse=True):
            if s not in smaller:
                longest = len(s)
                break
        return longest

    def findLUSlengthBetter(self, a, b):
        """
        This solution was found by another user much faster/simple than my
        original take. When the size of a != size of b the larger string will
        always be the longest uncommon substring. I didn't realize this which
        makes my solution rather slow.
        """
        if a == b:
            return -1
        return max(len(a), len(b))

if __name__ == '__main__':
    s = Solution()
    print s.findLUSlength('this is a test', 'my new test')
    print s.findLUSlength("aba", "cdc")
    print s.findLUSlength("abc", "abcz")
    print s.findLUSlength("abcz", "abc")

