"""
Q401. A binary watch has 4 LEDs on the top which represent the hours (0-11),
and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.

Given a non-negative integer n which represents the number of LEDs that are
currently on, return all possible times the watch could represent.
"""

import math
from collections import Counter

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """

        # Very slow solution, should have realized I don't need to check all
        # binary combinations :(
        possible_values = []

        for i in range(int(math.pow(2,10))):
            c = Counter(bin(i))
            if c['1'] == num:
                b = bin(i).split('b')[1]
                zeros = 10 - len(b)
                zeros = '0' * zeros
                b = zeros + b
                possible_values.append(b)

        output = []
        for time in possible_values:
            bhr = time[0:4]
            bmin = time[4:]
            dhr = 0
            dmin = 0

            bhr = list(bhr); bhr.reverse()
            bmin = list(bmin); bmin.reverse()

            for i,b in enumerate(bhr):
                dhr += int(math.pow(2,i)) * int(b)
            for i,b in enumerate(bmin):
                dmin += int(math.pow(2,i)) * int(b)

            valid_time = dhr >= 0 and dhr <= 11 and dmin >= 0 and dmin <= 59

            dhr = str(dhr)
            dmin = str(dmin)
            if len(dmin) == 1: dmin = '0' + dmin

            if valid_time:
                output.append(":".join([ str(dhr), str(dmin) ]))

        return output

    def readBinaryWatchBetterSolution(self, num):
        """ Much better solution found in discuss (not my code) """
        return ['%d:%02d' % (h, m)
                for h in range(12) for m in range(60)
                if (bin(h) + bin(m)).count('1') == num]

if __name__ == '__main__':
    s = Solution()
    print s.readBinaryWatch(2)

