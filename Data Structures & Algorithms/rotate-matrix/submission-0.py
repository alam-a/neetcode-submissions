class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        res = []
        n = len(matrix)
        for i in range(len(matrix)):
            temp = []
            for j in range(len(matrix)):
                temp.append(matrix[j][i])
            res.append(temp[::-1])
        for i in range(n):
            for j in range(n):
                matrix[i][j] = res[i][j]
