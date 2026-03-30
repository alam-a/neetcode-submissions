class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #row and col check
        for r in range(9):
            row = set()
            col = set()
            for c in range(9):
                if board[r][c] in row:
                    return False
                if board[c][r] in col:
                    return False
                if board[r][c] != ".":
                    row.add(board[r][c])
                if board[c][r] != ".":
                    col.add(board[c][r])
        
        #mini board check:
        for br in range(3):
            for bc in range(3):
                visited = set()
                for r in range(3*br, (3*br)+3):
                    for c in range(3*bc, (3*bc)+3):
                        if board[r][c] == ".":
                            continue
                        if board[r][c] in visited:
                            return False
                        visited.add(board[r][c])
        return True