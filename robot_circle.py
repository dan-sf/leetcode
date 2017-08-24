""" Problem statement: https://leetcode.com/problems/judge-route-circle/description/ """

class Robot(object):
    origin = (0, 0)
    _move_map = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}

    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, direction):
        self.x += self._move_map[direction][0]
        self.y += self._move_map[direction][1]

    def get_position(self):
        return self.x, self.y

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        moves = moves.upper()
        robot = Robot()
        for m in moves:
            robot.move(m)
        return robot.get_position() == Robot.origin

if __name__ == '__main__':
    s = Solution()

    print(s.judgeCircle("UD"))
    print(s.judgeCircle("LL"))

