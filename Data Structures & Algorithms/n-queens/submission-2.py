class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for j in range(n)] for i in range(n)]
        res = []
        def solve(r):
            if r == n:
                res.append(["".join(row) for row in board[:]])
                return

            for c in range(n):
                if check(r, c):
                    board[r][c] = "Q"
                    solve(r+1)
                    board[r][c] = "."
        
        def check(r, c):
            i = r-1
            while i > -1:
                if board[i][c] == "Q":
                    return False
                i-=1
            
            i, j = r-1, c-1
            while i > -1 and j > -1:
                if board[i][j] == "Q":
                    return False
                i-=1
                j-=1

            i, j = r-1, c+1
            while i > -1 and j < len(board):
                if board[i][j] == "Q":
                    return False
                i-=1
                j+=1
            return True
        solve(0)
        return res