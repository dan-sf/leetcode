""" Problem statement: https://leetcode.com/problems/climbing-stairs/ """

class Solution(object):
    def climbStairs(self, n):
        """ Iterative solution using the fibonacci sequence """
        fib = [0,1,2]
        if n <= len(fib)-1:
            return fib[n]

        for i in range(3, n):
            current = fib[i-1] + fib[i-2]
            fib.append(current)

        return fib[n-1] + fib[n-2]

    def climbStairsRecur(self, n):
        """ My recursive original solution, too slow (however, most intuitive),
        TLE. After running tests on this function I realized this was just
        creating fibonacci numbers. """
        count = 0
        return self._climbStairs(n, count)

    def _climbStairs(self, n, count):
        if n == 0:
            count += 1
            return count
        elif n < 0:
            return 0
        else:
            return self._climbStairs(n-1, count) + self._climbStairs(n-2, count)

    def climbStairsFib(self, n):
        """ Classic recursive fibonacci sequence """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairsFib(n-1) + self.climbStairsFib(n-2)

if __name__ == '__main__':
    s = Solution()

    for i in range(50):
        print s.climbStairs(i),

