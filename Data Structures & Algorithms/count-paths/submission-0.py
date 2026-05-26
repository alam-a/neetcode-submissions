class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[0] * n] * m
        for i in range(n):
            res[0][i] = 1
        
        for i in range(1, m):
            res[i][0] = res[i-1][0]
            for j in range(1, n):
                res[i][j] = res[i-1][j] + res[i][j-1]
        
        return res[-1][-1]