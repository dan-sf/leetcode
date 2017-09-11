""" Problem statement: https://leetcode.com/problems/distribute-candies/description/ """

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        candy_types = len(set(candies))
        total_candy = len(candies)
        if candy_types >= total_candy / 2:
            return  total_candy / 2
        else:
            return candy_types

if __name__ == '__main__':
    s = Solution()
    print s.distributeCandies([1,1,2,2,3,3])
    print s.distributeCandies([1,2,3,4])
    print s.distributeCandies([1,1,2,2,3,3,8,8,8,8,8,8])

