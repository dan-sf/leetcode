""" Problem statement: https://leetcode.com/problems/keyboard-row/description/ """

class Solution(object):
    def createMap(self, key_dict, row, value):
        for key in row:
            key_dict[key] = value

    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        top = set(list('qwertyuiop'))
        mid = set(list('asdfghjkl'))
        bot = set(list('zxcvbnm'))

        key_map = {}
        self.createMap(key_map, top, 1)
        self.createMap(key_map, mid, 2)
        self.createMap(key_map, bot, 3)

        output = []
        for word in words:
            check = []
            for letter in word:
                check.append(key_map[letter.lower()])
            if len(set(check)) == 1:
                output.append(word)

        return output

if __name__ == '__main__':
    s = Solution()
    print(s.findWords(["Hello","Alaska","Dad","Peace"]))

