""" Problem statement: https://leetcode.com/problems/construct-the-rectangle/description/ """

import math

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        if area == 0 or area == 1:
            return [ area, area ]

        output = [ area, 1 ]
        dif = area - 1
        x = 2
        while x <= int(math.sqrt(area))+1:
            if area % x == 0:
                i, j = (area / x, x)
                if abs(i - j) < dif:
                    dif = abs(i - j)
                    output = [ max(i, j), min(i, j) ]
            x += 1
        return output

if __name__ == '__main__':
    s = Solution()
    for i in range(20):
        print i, s.constructRectangle(i)
    import unittest
    class Test(unittest.TestCase):
        def test(self):
            s = Solution()
            self.assertEqual(s.constructRectangle(12), [4, 3])
            self.assertEqual(s.constructRectangle(9999997), [1428571, 7])
    unittest.main()

