class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R, C, inf = len(grid), len(grid[0]), 2147483647
        q = deque()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        wave = 0
        while q:
            wave += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for x, y in moves:
                    nr, nc = r + x, c + y
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] not in (0, -1) and grid[nr][nc] > wave:
                            grid[nr][nc] = wave
                            q.append((nr, nc))
