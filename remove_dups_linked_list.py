class list_node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list(object):
    def __init__(self):
        self.next = None
        self.head = None

    def add(self, data):
        n = list_node(data)
        n.next  = self.head
        self.head = n
    
    def add_list(self, ldata):
        for d in ldata:
            self.add(d)

    def size(self):
        counter = 0
        current = self.head
        while current != None:
            counter += 1
            current = current.next
        return counter

    def print_list(self):
        current = self.head
        while current != None:
            print current.data,
            current = current.next
        print

    def remove(self, item):
        found = False
        current = self.head
        previous = None
        while not found:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next

        if previous == None:
            self.head = current.next
        else:
            previous.next = current.next

    def remove_dups(self):
        current = self.head
        previous = self.head
        b = False
        while current != None:
            if current.next != None:
                while current.data == current.next.data:
                    current = current.next
                    b = True
                    if current.next == None:
                        break
            if b:
                previous.next = current.next
                current = current.next
                b = False
            else:
                current = current.next
                previous = current

    def remove_dups_uniq(self):
        """
        Given a sorted linked list, delete all nodes that have duplicate
        numbers, leaving only distinct numbers from the original list.

        For example,
        Given 1->2->3->3->4->4->5, return 1->2->5.
        Given 1->1->1->2->3, return 2->3.
        """
        current = self.head
        previous = self.head
        _previous = None
        did_loop = False
        while current != None:
            if current.next != None:
                while current.data == current.next.data:
                    current = current.next
                    did_loop = True
                    if current.next == None:
                        break
            if did_loop:
                if previous == self.head:
                    self.head = current.next
                    previous = self.head
                else:
                    _previous.next = current.next
                    previous = current.next
                current = current.next
                did_loop = False
            else:
                _previous = previous
                previous = current.next
                current = current.next

if __name__ == '__main__':
    ll = linked_list(); ll.add(1); ll.add(1); ll.add(2); ll.add(3); ll.add(4); ll.add(4);
    ll.print_list()
    ll.remove_dups_uniq()
    ll.print_list()

