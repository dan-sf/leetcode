""" Problem statement: https://leetcode.com/problems/reverse-words-in-a-string-iii/description/ """

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = []
        for word in s.split():
            output.append(word[::-1])
        return ' '.join(output)

