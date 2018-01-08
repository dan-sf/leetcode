""" Problem statement: https://leetcode.com/problems/number-of-boomerangs/description/ """

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        total = 0
        for i in points:
            pdict = {}
            for j in points:
                key = pow(j[0] - i[0], 2) + pow(j[1] - i[1], 2)
                if key in pdict:
                    pdict[key] += 1
                else:
                    pdict[key] = 1
            for k in pdict.values():
                total += k * (k - 1)
        return total

    def numberOfBoomerangsSlow(self, points):
        """
        Brute force solution, too slow
        """

        def is_boomerang(i, j, k):
            dist_a = pow(j[0] - i[0], 2) + pow(j[1] - i[1], 2)
            dist_b = pow(k[0] - i[0], 2) + pow(k[1] - i[1], 2)
            return dist_a == dist_b

        total = 0
        for i in points:
            for j in points:
                for k in points:
                    if i != j and j != k and is_boomerang(i, j, k):
                        total += 1
        return total

if __name__ == '__main__':
    s = Solution()
    print s.numberOfBoomerangs([[0,0],[1,0],[2,0]])
    print s.numberOfBoomerangs([[1,1],[2,2],[3,3]])
    print s.numberOfBoomerangs([[0,0],[1,0],[-1,0],[0,1],[0,-1]])

