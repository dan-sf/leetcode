"""
Q383. Given an arbitrary ransom note string and another string containing
letters from all the magazines, write a function that will return true if the
ransom note can be constructed from the magazines; otherwise, it will return
false.  Each letter in the magazine string can only be used once in your ransom
note.
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        for letter in ransomNote:
            if letter in magazine:
                magazine.remove(letter)
            else:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    print s.canConstruct("a", "b") # -> false
    print s.canConstruct("aa", "ab") # -> false
    print s.canConstruct("aa", "aab") # -> true

