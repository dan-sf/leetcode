""" Problem statement: https://leetcode.com/problems/ugly-number/description/ """

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        elif num < 1:
            return False
        elif num <= 6:
            return True

        ugly_primes = [2,3,5]
        while num > 1:
            div = [ num % p == 0 for p in ugly_primes ]
            if any(div):
                for i, d in enumerate(div):
                    if d:
                        num /= ugly_primes[i]
            else:
                return False

        return True

if __name__ == '__main__':
    s = Solution()

    for i in range(50):
        print i, s.isUgly(i)
    print s.isUgly(2147483648)

