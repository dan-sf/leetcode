""" Problem statement: https://leetcode.com/problems/valid-palindrome/description/ """

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        start = 0
        end = len(s) - 1
        while start < end:
            while start < end and not s[start].isalnum():
                start += 1
            while start < end and not s[end].isalnum():
                end -= 1
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

if __name__ == '__main__':
    s = Solution()
    print s.isPalindrome("A man, a plan, a canal: Panama")
    print s.isPalindrome("race a car")
    print s.isPalindrome("")
    print s.isPalindrome(",.")

