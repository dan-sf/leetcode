""" Problem statement: https://leetcode.com/problems/reverse-integer/description/ """

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x *= sign
        output = int(str(x)[::-1]) * sign
        if output < (-1*(1<<31)) or output > ((1<<31) - 1):
            return 0
        return output

if __name__ == '__main__':
    s = Solution()
    print s.reverse(100)
    print s.reverse(0)
    print s.reverse(-123)
    print s.reverse(123)
    print s.reverse(1230)
    print s.reverse(-1230)
    print s.reverse(1534236469)

