"""
Q415. Given two non-negative numbers num1 and num2 represented as string,
return the sum of num1 and num2.

Note:
    - The length of both num1 and num2 is < 5100.
    - Both num1 and num2 contains only digits 0-9.
    - Both num1 and num2 does not contain any leading zero.
    - You must not use any built-in BigInteger library or convert the inputs to
      integer directly.
"""

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = [ int(n) for n in num1 ]
        num2 = [ int(n) for n in num2 ]
        num1.reverse()
        num2.reverse()

        big_num = num1 if len(num1) >= len(num2) else num2
        small_num = num1 if len(num1) < len(num2) else num2

        for i, n in enumerate(small_num):
            big_num[i] = big_num[i] + n

        hold = 0
        for i in range(len(big_num)):
            if big_num[i] + hold >= 10:
                big_num[i] = (big_num[i] + hold) % 10
                hold = 1
            else:
                big_num[i] = big_num[i] + hold
                hold = 0

        if hold:
            big_num.append(hold)

        big_num.reverse()
        return "".join([ str(n) for n in big_num ])

if __name__ == '__main__':
    s = Solution()
    print s.addStrings('1234', '2345')
    print s.addStrings('99999999', '1234')
    print s.addStrings("5656605999999999999999999999", "1324132413241423132324142341434124321")

