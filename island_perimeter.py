""" 
Q463. You are given a map in form of a two-dimensional integer grid where 1
represents land and 0 represents water. Grid cells are connected
horizontally/vertically (not diagonally). The grid is completely surrounded by
water, and there is exactly one island (i.e., one or more connected land
cells). The island doesn't have "lakes" (water inside that isn't connected to
the water around the island). One cell is a square with side length 1. The grid
is rectangular, width and height don't exceed 100. Determine the perimeter of
the island.
"""

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0

        for row_index, row in enumerate(grid):
            for col_index, col in enumerate(row):
                top, bottom, left, right = self.is_edge(grid, row_index, col_index)
                if col == 1:
                    if left:
                        perimeter += 1
                    else:
                        if grid[row_index][col_index-1] == 0:
                            perimeter += 1
                    if right:
                        perimeter += 1
                    else:
                        if grid[row_index][col_index+1] == 0:
                            perimeter += 1
                    if top:
                        perimeter += 1
                    else:
                        if grid[row_index-1][col_index] == 0:
                            perimeter += 1
                    if bottom:
                        perimeter += 1
                    else:
                        if grid[row_index+1][col_index] == 0:
                            perimeter += 1

        return perimeter

    def is_edge(self, grid, row_index, col_index):
        rows = len(grid)
        columns = len(grid[0])
        top = True if row_index == 0 else False
        bottom = True if row_index == rows-1 else False
        left = True if col_index == 0 else False
        right = True if col_index == columns-1 else False
        return top,bottom,left,right

    def islandPerimeterBetter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0

        for row_index, row in enumerate(grid):
            for col_index, col in enumerate(row):
                if col == 1:
                    if col_index - 1 < 0 or grid[row_index][col_index-1] == 0:
                        perimeter += 1
                    if col_index + 1 > len(row)-1 or grid[row_index][col_index+1] == 0:
                        perimeter += 1
                    if row_index - 1 < 0 or grid[row_index-1][col_index] == 0:
                        perimeter += 1
                    if row_index + 1 > len(grid)-1 or grid[row_index+1][col_index] == 0:
                        perimeter += 1

        return perimeter

if __name__ == '__main__':
    s = Solution()

    print s.islandPerimeter([[0,1,0,0],
                             [1,1,1,0],
                             [0,1,0,0],
                             [1,1,0,0]])

