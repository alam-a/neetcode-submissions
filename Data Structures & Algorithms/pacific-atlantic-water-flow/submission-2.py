class Solution:
    def __init__(self):
        self.pacific = set()
        self.atlantic = set()
        self.movements = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        l, b = len(heights), len(heights[0])
        for i in range(l):
            self.pacific.add((i, 0))
            self.atlantic.add((i, b-1))    
        for i in range(b):
            self.pacific.add((0, i))
            self.atlantic.add((l-1, i))
        
        def dfs(points, accessible):
            print(points)
            print(accessible)
            npoints = []
            for point in points:
                x, y = point
                height = heights[x][y]
                for move in self.movements:
                    nx, ny = x + move[0], y + move[1]
                    if nx >= 0 and ny >= 0 and nx < l and ny < b and heights[nx][ny] >= height and (nx, ny) not in accessible:
                        accessible.add((nx, ny))
                        npoints.append((nx, ny))
            if npoints: dfs(npoints, accessible)

        dfs(list(self.pacific), self.pacific)
        dfs(list(self.atlantic), self.atlantic)
        return [list(point) for point in self.pacific.intersection(self.atlantic)]