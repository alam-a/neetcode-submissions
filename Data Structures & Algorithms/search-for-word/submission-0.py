class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i, j, curr):
            if curr == len(word):
                return True

            # print(board[i][j], word[curr])
            
            while i < len(board):
                while j < len(board[0]):
                    if board[i][j] == word[curr]:
                        h = backtrack(i, j+1, curr+1)
                        v = backtrack(i+1, j, curr+1)
                        if h or v:
                            return True
                    curr = 0
                    j+=1
                i+=1
            return False
        return backtrack(0, 0, 0)
                    

                
        