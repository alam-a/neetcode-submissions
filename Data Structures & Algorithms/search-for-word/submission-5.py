class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C, N = len(board), len(board[0]), len(word)
        self.visited = set()
        self.movements = ((0, 1), (0, -1), (1, 0), (-1, 0))
        def dfs(bi, bj, wi):
            if wi == N:
                return True
            for mi, mj in self.movements:
                i, j = bi + mi, bj + mj
                if i < 0 or i >= R or j < 0 or j >= C or (i, j) in self.visited or board[i][j] != word[wi]:
                    continue
                self.visited.add((i, j))
                if dfs(i, j, wi + 1):
                    return True
                self.visited.remove((i, j))
            return False
        
        for i in range(R):
            for j in range(C):
                if board[i][j] == word[0]:
                    self.visited.add((i, j))
                    if dfs(i, j, 1):
                        return True
                    self.visited.remove((i, j))
        return False
                    