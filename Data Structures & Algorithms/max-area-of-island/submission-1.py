class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        self.res, self.curr = 0, 0
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(i, j):
            if i >= R or j >= C or i < 0 or j < 0 or grid[i][j] == 0:
                return
            self.curr += 1
            self.res = max(self.res, self.curr)
            grid[i][j] = 0
            for move in moves:
                dfs(i + move[0], j + move[1])
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    self.curr = 0
                    dfs(r, c)
        return self.res