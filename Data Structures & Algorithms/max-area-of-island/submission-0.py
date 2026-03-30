class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        largest, self.curr = 0, 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(x, y):
            if x < 0 or y < 0 or x >= ROWS or y >= COLS or grid[x][y] == 0:
                return
            grid[x][y] = 0
            self.curr += 1
            for d in directions:
                dfs(x + d[0], y + d[1])

        #iterate over islands
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    self.curr = 0
                    dfs(r, c)
                    largest = max(largest, self.curr)
        return largest