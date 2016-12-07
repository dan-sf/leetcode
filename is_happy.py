"""
Q202. Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any
positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay), or it
loops endlessly in a cycle which does not include 1. Those numbers for which
this process ends in 1 are happy numbers.
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        seen = set()

        def is_happy_rec(n, seen):
            if n in seen:
                return False
            seen.add(n)
            output_num = sum([ int(i)*int(i) for i in str(n) ])

            if output_num != 1:
                return is_happy_rec(output_num, seen)

            return True

        return is_happy_rec(n, seen)

    def isHappyBetter(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = {1}
        while n not in seen:
            seen.add(n)
            n = sum([ int(i)*int(i) for i in str(n) ])
        return n == 1

if __name__ == '__main__':
    s = Solution()
    print s.isHappy(11)
    print s.isHappy(18)
    print s.isHappy(19)
    print s.isHappy(190)
    print s.isHappy(338)

