class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        R, C = len(matrix), len(matrix[0])
        r, c = [1] * R, [1] * C
        i, j = 0, 0
        while i < R:
            while j < C:
                if matrix[i][j] == 0:
                    r[i], c[j] = 0, 0
                    break
                j += 1
            j = 0
            i += 1

        
        for i in range(R):
            for j in range(C):
                if r[i] == 0 or c[j] == 0:
                    matrix[i][j] = 0
