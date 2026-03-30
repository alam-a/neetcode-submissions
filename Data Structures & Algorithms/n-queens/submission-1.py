class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for i in range(n)] for j in range(n)]
        res = []
        def backtrack(row):
            # print(board, row, n)
            if row == n:
                
                res.append(["".join(row) for row in board[:]])
                return
            
            for c in range(n):
                if self.check(row, c, board):
                    # print(board)
                    board[row][c] = "Q"
                    # print(board)
                    # print()
                    backtrack(row+1)
                    board[row][c] = "."
        backtrack(0)
        return res


    
    def check(self, r, c, board):
        i, j = r, c
        # print(i, j, board)
        while i > -1:
            if board[i][j] == 'Q':
                return False
            i -= 1
        i, j = r, c
        while i > -1 and j > -1:
            if board[i][j] == 'Q':
                return False
            i-=1
            j-=1
        i, j = r, c
        while i > -1 and j < len(board):
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        # print("safe")
        return True