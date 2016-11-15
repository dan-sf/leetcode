"""
Q13. Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        subtract = {"IV":-1*2, "IX":-1*2,"XL":-10*2, "XC":-10*2, "CD":-100*2, "CM":-100*2}
        output = 0

        for i in range(len(s)):
            if i != len(s) - 1:
                if s[i] + s[i+1] in subtract:
                    output += subtract[s[i] + s[i+1]]
            output += roman_map[s[i]]
        return output

if __name__ == '__main__':
    s = Solution()
    print s.romanToInt("MCMXCVI")
