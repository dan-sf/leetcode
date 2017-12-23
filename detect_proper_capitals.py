""" Problem statement: https://leetcode.com/problems/detect-capital/description/ """

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.isupper() or word.islower():
            return True
        if word[0].isupper() and word[1:].islower():
            return True
        return False

def test(s, arg, expected):
    actual = s.detectCapitalUse(arg)
    print 'Testing -> expected: {}, actual {}'.format(expected, actual)
    assert actual == expected

if __name__ == '__main__':
    s = Solution()
    test(s, 'USA', True)
    test(s, 'leetcode', True)
    test(s, 'test 123', True)
    test(s, 'usA', False)
    test(s, 'Usa', True)
    test(s, 'Google', True)
    test(s, 'FlaG', False)

