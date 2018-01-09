""" Problem statement: https://leetcode.com/problems/map-sum-pairs/description/ """

class Node(object):
    def __init__(self):
        self.value = 0
        self.kids = {}

class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Node()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        node = self.trie
        i = 0
        while i < len(key):
            if key[i] in node.kids:
                node = node.kids[key[i]]
                i += 1
            else:
                break

        while i < len(key):
            node.kids[key[i]] = Node()
            node = node.kids[key[i]]
            i += 1
        node.value = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        output = 0
        node = self.trie
        for ch in prefix:
            if ch in node.kids:
                node = node.kids[ch]
            else:
                return output

        queue = [node]
        while len(queue) != 0:
            n = queue.pop()
            output += n.value
            queue += n.kids.values()
        return output

if __name__ == '__main__':
    m = MapSum()
    m.insert('apple', 3)
    print m.sum('app')
    m.insert('app', 2)
    m.insert('apps', 2)
    print m.sum('app')
    m.insert('ten', 7)
    m.insert('tens', 7)
    m.insert('test', 1)
    m.insert('testing', 11)
    print m.sum('t')
    print m.sum('te')
    print m.sum('ten')
    print m.sum('tens')
    print m.sum('test')
    print m.sum('testi')

