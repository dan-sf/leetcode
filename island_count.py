""" Problem statement: https://leetcode.com/problems/number-of-islands/description/ """

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        output = 0
        rows = len(grid)
        if rows == 0:
            return output
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    output += 1
                    self.zero_island(grid, row, col)
        return output

    def zero_island(self, grid, row, col):
        queue = [(row, col)]
        while queue != []:
            r, c = queue.pop()
            grid[r][c] = '0'
            if self.is_valid(grid, r+1, c):
                if grid[r+1][c] == '1':
                    queue.append((r+1, c))
            if self.is_valid(grid, r-1, c):
                if grid[r-1][c] == '1':
                    queue.append((r-1, c))
            if self.is_valid(grid, r, c+1):
                if grid[r][c+1] == '1':
                    queue.append((r, c+1))
            if self.is_valid(grid, r, c-1):
                if grid[r][c-1] == '1':
                    queue.append((r, c-1))

    def is_valid(self, grid, row, col):
        rows = len(grid)
        cols = len(grid[0])

        if row < 0 or col < 0:
            return False
        if col >= cols or row >= rows:
            return False
        return True

if __name__ == '__main__':
    s = Solution()
    grid = [['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']]
    print s.numIslands(grid)
    grid = [['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1']]
    print s.numIslands(grid)

