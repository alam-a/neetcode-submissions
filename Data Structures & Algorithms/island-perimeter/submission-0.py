class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        sides = ((0, 1), (1, 0), (0, -1), (-1, 0))
        perimeter = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    for mi, mj in sides:
                        ni, nj = i + mi, j + mj
                        if 0 <= ni < R and 0 <= nj < C:
                            if grid[ni][nj] == 0:
                                perimeter += 1
                        else:
                            perimeter += 1
        return perimeter