class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        crp, cra = set(), set() # can reach pacific, can reach atlantic
        for r in range(R):
            for c in range(C):
                if r == 0 or c == 0:
                    crp.add((r, c))
                if r == R-1 or c == C-1:
                    cra.add((r, c))
        
        moves = ((0, 1), (0, -1), (1, 0), (-1, 0))
        def dfs(r, c, check_list):
            for mr, mc in moves:
                nr, nc = r+mr, c+mc
                if (nr, nc) not in check_list and 0 <= nr < R and 0 <= nc < C and heights[r][c] <= heights[nr][nc]:
                    check_list.add((nr, nc))
                    dfs(nr, nc, check_list)
        
        for r, c in list(cra):
            dfs(r, c, cra)
        for r, c in list(crp):
            dfs(r, c, crp)
        
        return list(cra.intersection(crp))