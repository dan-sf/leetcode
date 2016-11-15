"""
Q206. Reverse a singly linked list.
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        list_hold = []
        input_node = head
        while input_node is not None:
            list_hold.insert(0,input_node.val)
            input_node = input_node.next

        output_node = ListNode(list_hold[0])
        output_head = output_node
        for n in list_hold[1:]:
            output_node.next = ListNode(n)
            output_node = output_node.next

        return output_head

if __name__ == '__main__':
    s = Solution()

    ll = ListNode(1)
    ll.next = ListNode(2)
    ll.next.next = ListNode(3)
    ll.next.next.next = ListNode(4)
    ll.next.next.next.next = ListNode(5)

    rev = s.reverseList(ll)

    while rev is not None:
        print rev.val,
        rev = rev.next
    print

    while ll is not None:
        print ll.val,
        ll = ll.next
    print

