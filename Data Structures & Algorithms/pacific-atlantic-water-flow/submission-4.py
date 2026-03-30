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
        
        print(cra)
        print(crp)
        moves = ((0, 1), (0, -1), (1, 0), (-1, 0))
        atlantic, pacific = list(cra), list(crp)
        

        while atlantic:
            na = []
            for r, c in atlantic:
                for mr, mc in moves:
                    nr, nc = r+mr, c+mc
                    if (nr, nc) not in cra and 0 <= nr < R and 0 <= nc < C and heights[nr][nc] >= heights[r][c]:
                        cra.add((nr, nc))
                        na.append((nr, nc))
            atlantic = na

        while pacific:
            np = []
            for r, c in pacific:
                for mr, mc in moves:
                    nr, nc = r+mr, c+mc
                    if (nr, nc) not in crp and 0 <= nr < R and 0 <= nc < C and heights[nr][nc] >= heights[r][c]:
                        crp.add((nr, nc))
                        np.append((nr, nc))
            pacific = np
        print(crp)
        print(cra)
        return list(cra.intersection(crp))