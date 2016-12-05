"""
Q455. Assume you are an awesome parent and want to give your children some
cookies. But, you should give each child at most one cookie. Each child i has a
greed factor gi, which is the minimum size of a cookie that the child will be
content with; and each cookie j has a size sj. If sj >= gi, we can assign the
cookie j to the child i, and the child i will be content. Your goal is to
maximize the number of your content children and output the maximum number.
"""

class Solution(object):
    def findContentChildrenSlow(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        content = 0
        for cookie in s:
            kid_index = self.can_give(cookie, g)
            if kid_index >= 0:
                content += 1
                del g[kid_index]

        return content

    def can_give(self, cookie, kids):
        possible_kids = {}
        max_greedy = -1
        for i in range(len(kids)):
            if cookie == kids[i]:
                return i
            elif cookie >= kids[i] and kids[i] > max_greedy:
                max_greedy = kids[i]
                possible_kids[max_greedy] = i

        if max_greedy >= 0:
            return possible_kids[max_greedy]
        return -1

    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        content_count = 0
        cookie_index = 0

        while content_count < len(g) and cookie_index < len(s):
            if s[cookie_index] >= g[content_count]:
                content_count += 1
            cookie_index += 1
        return content_count

if __name__ == '__main__':
    s = Solution()

    print s.findContentChildren([1,2,3], [1,1])
    print s.findContentChildren([1,2], [1,2,3])
    print s.findContentChildren([10,9,8,7], [10,9,8,7])

