class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])
        l, r = 0, R-1
        row_head = [matrix[i][0] for i in range(R)]
        print(row_head)
        while l <= r:
            mid = (l + r) // 2
            print(l, r, mid)
            if matrix[mid][0] == target or target == matrix[mid][-1]:
                return True
            elif matrix[mid][0] < target < matrix[mid][-1]:
                l = mid
                break
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1
        
        if l >= R:
            return False
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