class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i, j, curr, crumbs):
            if curr == len(word):
                return True

            if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
                return False

            # print(board[i][j], word[curr], crumbs)
            if board[i][j] == word[curr]:
                possibilities = [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]
                for p in possibilities:
                    if p not in crumbs:
                        crumbs.add(p)
                        if backtrack(p[0], p[1], curr+1, crumbs):
                            return True
                        crumbs.remove(p)
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0, {(i, j)}):
                    return True
        return False

# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         def backtrack(i, j, curr, crumbs):
#             if curr == len(word):
#                 return True

#             if curr == 0:
#                 print()
#             if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
#                 return False
#             if board[i][j] == word[curr]:
#                 h,v = False, False
#                 nh, ph = (i, j+1), (i, j-1)
#                 nv, pv = (i+1, j), (i-1, j)

#                 if nh not in crumbs:
#                     crumbs.add(nh)
#                     h = backtrack(nh[0], nh[1], curr+1, crumbs)
#                     crumbs.remove(nh)

#                 if ph not in crumbs:
#                     crumbs.add(ph)
#                     h = h or backtrack(ph[0], ph[1], curr+1, crumbs)
#                     crumbs.remove(ph)

#                 # vertical
#                 if nv not in crumbs:
#                     crumbs.add(nv)
#                     v = backtrack(nv[0], nv[1], curr+1, crumbs)
#                     crumbs.remove(nv)
#                 if pv not in crumbs:
#                     crumbs.add(pv)
#                     v = v or backtrack(pv[0], pv[1], curr+1, crumbs)
#                     crumbs.remove(pv)
#                 if h or v:
#                     return True
#             return False
#         crumbs = set()
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 # crumbs.add((i, j))
#                 if backtrack(i, j, 0, {(i, j)}):
#                     return True
#         return False
#                     # [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]. "ABCCED"

                
        