"""
Q237. Write a function to delete a node (except the tail) in a singly linked
list, given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node
with value 3, the linked list should become 1 -> 2 -> 4 after calling your
function.
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def add(self, val):
        node = ListNode(val)
        node.next  = self.head
        self.head = node

    def print_list(self):
        current = self.head
        while current != None:
            print current.val,
            current = current.next
        print

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node is not None:
            if node.next is not None:
                node.val = node.next.val
                node.next = node.next.next
            else:
                node.next = None

if __name__ == '__main__':
    s = Solution()
    ll = LinkedList(); ll.add(4); ll.add(3); ll.add(2); ll.add(1);
    ll.print_list()
    print ll.head.next.next.val
    s.deleteNode(ll.head.next.next)
    ll.print_list()

