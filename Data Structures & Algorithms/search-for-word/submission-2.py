class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i, j, curr, crumbs):
            if curr == len(word):
                return True

            if curr == 0:
                print()
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
                return False
            if board[i][j] == word[curr]:
                h,v = False, False
                print(crumbs)
                nh, ph = (i, j+1), (i, j-1)
                if nh not in crumbs:
                    print("horizontal")
                    crumbs.add(nh)
                    h = backtrack(nh[0], nh[1], curr+1, crumbs)
                    crumbs.remove(nh)
                print(crumbs)

                if ph not in crumbs:
                    print("horizontal")
                    crumbs.add(ph)
                    h = h or backtrack(ph[0], ph[1], curr+1, crumbs)
                    crumbs.remove(ph)
                print(crumbs)

                # vertical
                nv, pv = (i+1, j), (i-1, j)
                if nv not in crumbs:
                    print("vertical")
                    crumbs.add(nv)
                    v = backtrack(nv[0], nv[1], curr+1, crumbs)
                    crumbs.remove(nv)
                print(crumbs)
                if pv not in crumbs:
                    print("vertical")
                    crumbs.add(pv)
                    v = v or backtrack(pv[0], pv[1], curr+1, crumbs)
                    crumbs.remove(pv)
                print(crumbs)
                print(nh, ph, nv, pv)
                if h or v:
                    return True
            return False
        crumbs = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                # crumbs.add((i, j))
                if backtrack(i, j, 0, set()):
                    return True
        return False
                    

                
        