""" Problem statement: https://leetcode.com/problems/remove-duplicates-from-sorted-array/ """

class Solution(object):
    def removeDuplicates(self, nums):
        """
        Technically this solution isn't fully correct because I am storing the
        values to delete. I missed the part of the question that says "It
        doesn't matter what you leave beyond the new length." which allows you
        to solve this with O(1) space by just modifing the first n elements of
        the array (not modifying the array's length).
        """
        if len(nums) == 0:
            return 0

        del_list = []
        hold = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != hold:
                hold = nums[i]
            else:
                del_list.append(i)

        for d in del_list[::-1]:
            del nums[d]

        return len(nums)

if __name__ == '__main__':
    s = Solution()

    l = [1,2,2,2,2,2,2,3,3,3,4]
    print s.removeDuplicates(l), l

    l = [1,2,3,3,4,4,4]
    print s.removeDuplicates(l), l

    l = [1,2,2,2,3,3,3,4]
    print s.removeDuplicates(l), l

