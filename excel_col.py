"""
Given a column title as appear in an Excel sheet, return its corresponding
column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
"""

import string
import math

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s.lower())
        s.reverse()
        letter_map = {}
        for key, value in zip(list(string.lowercase), range(1,27)):
            letter_map[key] = value

        output = 0
        for i, letter in enumerate(s):
            output += letter_map[letter] * math.pow(26, i)

        return int(output)


if __name__ == '__main__':
    s = Solution()
    print s.title_to_number('A')
    print s.title_to_number('B')
    print s.title_to_number('C')
    print s.title_to_number('Z')
    print s.title_to_number('AA')
    print s.title_to_number('AB')
    print s.title_to_number('AC')

