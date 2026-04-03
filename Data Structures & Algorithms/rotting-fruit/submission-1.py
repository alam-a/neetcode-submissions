class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        q = collections.deque()
        ffc = 0 #fresh fruit count

        #add rotten fruits for first pass
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q.append((r, c))
                    grid[r][c] = 0
                elif grid[r][c] == 1:
                    ffc += 1

        time = 0
        moves = ((1, 0), (0, 1), (-1, 0), (0, -1))
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for move in moves:
                    nr, nc = r + move[0], c + move[1]
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        q.append((nr, nc))
                        ffc -= 1
            if q:
                time += 1
        return time if ffc == 0 else -1

