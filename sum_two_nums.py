"""
Calculate the sum of two integers a and b, but you are not allowed to
use the operator + and -
"""

class Solution(object):
    def getSum(self, a, b):
        # could have done (better solution):
        # return a.__add__(b) 
        return sum([a,b])

if __name__ == '__main__':
    s = Solution()
    print s.getSum(1,3)
    print s.getSum(2,3)
    print s.getSum(5,3)
    print s.getSum(100,3)

