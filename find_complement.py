""" Problem statement: https://leetcode.com/problems/number-complement/description/ """

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return ((1<<(len(bin(num))-2))-1) & ~num

