""" Problem statement: https://leetcode.com/problems/next-greater-element-i/description/ """

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        for i in findNums:
            appended = False
            for j in nums[nums.index(i):]:
                if j > i:
                    output.append(j)
                    appended = True
                    break
            if not appended:
                output.append(-1)
        return output

if __name__ == '__main__':
    s = Solution()
    print s.nextGreaterElement([4,1,2], [1,3,4,2])
    print s.nextGreaterElement([2,4], [1,2,3,4])

