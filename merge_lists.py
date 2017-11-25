""" Problem Statement: https://leetcode.com/problems/merge-two-sorted-lists/description/ """

class LinkedList(object):
    def __init__(self):
        self.head = None

    def add(self, val):
        tmp = self.head
        self.head = ListNode(val)
        self.head.next = tmp

    @classmethod
    def from_list(cls, alist):
        output = cls()
        for val in alist:
            output.add(val)
        return output

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        vals = self.get_list()
        return "ListNode: {}".format(vals)

    def get_list(self):
        output = []
        n = self
        while n != None:
            output.append(n.val)
            n = n.next
        return output

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # Handle None cases
        if l1 == None and l2 == None:
            return None
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        # Set first runner to smallest value
        if l1.val <= l2.val:
            r1 = l1
            r2 = l2
        else:
            r1 = l2
            r2 = l1
        output = ListNode(r1.val)
        head = output
        r1 = r1.next

        while r1 != None or r2 != None:
            if r1 == None or r2 == None:
                if r1 != None:
                    while r1 != None:
                        output.next = ListNode(r1.val)
                        output = output.next
                        r1 = r1.next
                else:
                    while r2 != None:
                        output.next = ListNode(r2.val)
                        output = output.next
                        r2 = r2.next
            else:
                if r1.val <= r2.val:
                    output.next = ListNode(r1.val)
                    output = output.next
                    r1 = r1.next
                else:
                    output.next = ListNode(r2.val)
                    output = output.next
                    r2 = r2.next
        return head

if __name__ == '__main__':
    s = Solution()

    l1 = LinkedList.from_list([7,5,3,1])
    l2 = LinkedList.from_list([8,6,4,2])
    output = s.mergeTwoLists(l1.head, l2.head)
    print output.get_list()

    l1 = LinkedList.from_list([])
    l2 = LinkedList.from_list([8,6,4,2])
    output = s.mergeTwoLists(l1.head, l2.head)
    print output.get_list()

    l1 = LinkedList.from_list([7,5,3,1])
    l2 = LinkedList.from_list([])
    output = s.mergeTwoLists(l1.head, l2.head)
    print output.get_list()

    l1 = LinkedList.from_list([7])
    l2 = LinkedList.from_list([8,6,4,2])
    output = s.mergeTwoLists(l1.head, l2.head)
    print output.get_list()

    l1 = LinkedList.from_list([7,5,3,1])
    l2 = LinkedList.from_list([8,6,2])
    output = s.mergeTwoLists(l1.head, l2.head)
    print output.get_list()

    l1 = LinkedList.from_list([7,5,3,1])
    l2 = LinkedList.from_list([8])
    output = s.mergeTwoLists(l1.head, l2.head)
    print output.get_list()

    l1 = LinkedList.from_list([3,3,2,1,1,1])
    l2 = LinkedList.from_list([8,6,4,2])
    output = s.mergeTwoLists(l1.head, l2.head)
    print output.get_list()

