""" Problem statement: https://leetcode.com/problems/remove-duplicates-from-sorted-list/ """

class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
    def add(self, item):
        n = Node(item)
        n.next = self.head
        self.head = n
    def print_this(self):
        n = self.head
        while n != None:
            print n.val
            n = n.next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        n = head
        while n != None:
            runner = n.next
            while runner != None and runner.val == n.val:
                runner = runner.next
            n.next = runner
            n = n.next
        return head

if __name__ == '__main__':
    l = LinkedList()
    l.add(1); l.add(1); l.add(2); l.add(3); l.add(3);
    l.print_this()

    print ""
    s = Solution()

    h = s.deleteDuplicates(l.head)
    while h != None:
        print h.val
        h = h.next

