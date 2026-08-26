class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C, W = len(board), len(board[0]), len(word)
        moves = ((0, 1), (0, -1), (1, 0), (-1, 0))
        visited = set()
        def dfs(r, c, wi):
            if wi == W:
                return True
            for mi, mj in moves:
                ni, nj = r + mi, c + mj
                if (ni, nj) not in visited and 0 <= ni < R and 0 <= nj < C and board[ni][nj] == word[wi]:
                    visited.add((ni, nj))
                    if dfs(ni, nj, wi+1):
                        return True
                    visited.remove((ni, nj))
            return False
        for i in range(R):
            for j in range(C):
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    if dfs(i, j, 1):
                        return True
                    visited.remove((i, j))
        return False