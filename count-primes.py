"""
Problem 204: https://leetcode.com/problems/count-primes/ @easy

Count the number of prime numbers less than a non-negative number, n.
"""

# Initial solution
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        primes = [True] * n
        primes[0], primes[1] = False, False

        output = 0
        for i in range(n):
            if primes[i]:
                output += 1

                comp = i * i
                while comp < n:
                    primes[comp] = False
                    comp += i
        return output

# Slightly faster sieve
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        primes = [True] * n
        primes[0], primes[1] = False, False

        prime = 2
        while (prime * prime) < n:
            if primes[prime]:
                comp = prime * prime
                while comp < n:
                    primes[comp] = False
                    comp += prime
            prime += 1
        return primes.count(True)

print(Solution().countPrimes(10))
print(Solution().countPrimes(11))

