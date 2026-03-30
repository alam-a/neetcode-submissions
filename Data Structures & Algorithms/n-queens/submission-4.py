class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        state = [["." for _ in range(n)] for _ in range(n)]
        res = []
        def can_put_queen_here(row, col):
            #check up
            i, j = 0, 0
            while i < row:
                if state[i][col] == 'Q':
                    return False
                i+=1
            
            #left diagonal
            i, j = row-1, col-1
            while i >= 0 and j >= 0:
                if state[i][j] == 'Q':
                    return False
                i-=1
                j-=1

            #right diagonal
            i, j = row-1, col+1
            while i >= 0 and j < n:
                if state[i][j] == 'Q':
                    return False
                i-=1
                j+=1
            return True            
                
        def dfs(row):
            if row == n:
                temp = []
                for r in state:
                    temp.append("".join(r[:]))
                res.append(temp)
                return
            for i in range(n):
                if can_put_queen_here(row, i):
                    state[row][i] = 'Q'
                    dfs(row+1)
                    state[row][i] = '.'
        dfs(0)
        return res