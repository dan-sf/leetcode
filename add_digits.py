"""
Given a non-negative integer num, repeatedly add all its digits until the
result has only one digit.

For example: Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since
2 has only one digit, return it.

Follow up: Could you do it without any loop/recursion in O(1) runtime?
"""

class Solution(object):
    def addDigits(self, num):
        if num % 9 == 0 and num != 0:
            return 9
        else:
            return num % 9

    def addDigits_slow(num):
        if len(str(num)) == 1:
            return num
        else:
            while True:
                num = reduce(lambda a,b: int(a) + int(b), list(str(num)))
                if len(str(num)) == 1:
                    return num

if __name__ == '__main__':
    s = Solution()
    for i in range(100):
        print i, s.addDigits(i)

