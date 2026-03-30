class Solution:
    def __init__(self):
        self.cva = set()
        self.cvp = set()

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i in range(R):
            self.cvp.add((i, 0))
            self.cva.add((i, C-1))
        for i in range(C):
            self.cvp.add((0, i))
            self.cva.add((R-1, i))
        from collections import deque
        aq = list(self.cva)
        while aq:
            naq = deque()
            for r, c in list(aq):
                for i, j in directions:
                    if r+i < R and c+j < C and r+i >= 0 and c+j >= 0 and (r+i, c+j) not in self.cva and heights[r][c] <= heights[r+i][c+j]:
                        self.cva.add((r+i, c+j))
                        naq.append((r+i, c+j))
            aq = list(naq)
        pq = list(self.cvp)
        while pq:
            npq = deque()
            for r, c in list(pq):
                for i, j in directions:
                    if r+i < R and c+j < C and r+i >= 0 and c+j >= 0 and (r+i, c+j) not in self.cvp and heights[r][c] <= heights[r+i][c+j]:
                        self.cvp.add((r+i, c+j))
                        npq.append((r+i, c+j))
            pq = list(npq)
        return list(self.cva.intersection(self.cvp))
