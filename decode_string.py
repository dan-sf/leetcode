""" Problem statement: https://leetcode.com/problems/decode-string/ """

import string

class Solution(object):
    def matching_bracket(self, s, start):
        index = start + 1
        count = 0
        while index < len(s) and (s[index] != ']' or count != 0):
            if s[index] == '[':
                count += 1
            if s[index] == ']':
                count -= 1
            index += 1
        return index

    def find_number(self, s):
        for i in range(len(s)):
            if s[i] in string.digits:
                return i
        return -1

    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        find_bracket = s.find('[')
        if find_bracket == -1:
            return s

        num_index = self.find_number(s)
        prepend = s[0:num_index]
        matched_bracket = self.matching_bracket(s, find_bracket)
        postpend = s[s.rfind(']')+1:]
        multiplier = int(s[num_index:find_bracket])

        return prepend + \
               multiplier * \
               self.decodeString(s[find_bracket+1:matched_bracket]) + \
               self.decodeString(s[matched_bracket+1:s.rfind(']')+1]) + \
               postpend

if __name__ == '__main__':
    s = Solution()
    def h(st):
        print("Input: '{}' -> '{}'".format(st, s.decodeString(st)))
    h('X3[as2[n]]X')
    h('3[a]2[bc]')
    h('3[a2[c]]')
    h('2[abc]3[cd]ef')
    h('10[so]')
    h('one2[a]two')
    h('')
    h('test')
    h('2[test2[a]ing3[b]]')

