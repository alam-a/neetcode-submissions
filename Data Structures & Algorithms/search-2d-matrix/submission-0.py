class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])
        l, r = 0, R-1
        row_head = [matrix[i][0] for i in range(R)]
        print(row_head)
        while l <= r:
            mid = (l + r) // 2
            print(l, r, mid)
            if matrix[mid][0] == target:
                return True
            if l == mid:
                break
            if target < matrix[mid][0]:
                r = l - 1
            else:
                l = mid
        row = matrix[l]
        print(l, row)
        l, r = 0, C-1
        while l <= r:
            mid = (l+r)//2
            print(l, r, mid, row[mid])
            if row[mid] == target:
                return True
            elif target > row[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return False