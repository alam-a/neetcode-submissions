class Solution:
    def __init__(self):
        self.pacific = set()
        self.atlantic = set()
        self.no_pacific = set()
        self.no_atlantic = set()
        self.movements = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        l, b = len(heights), len(heights[0])
        for i in range(l):
            self.pacific.add((i, 0))
            self.atlantic.add((i, b-1))    
        for i in range(b):
            self.pacific.add((0, i))
            self.atlantic.add((l-1, i))
        
        def dfs(points, accessible, inaccessible):
            print(accessible)
            print(inaccessible)
            new_points = []
            for point in points:
                for move in self.movements:
                    np = (point[0]+move[0], point[1]+move[1])
                    if np in accessible:
                        continue
                    elif np[0] >= 0 and np[0] < l and np[1] >= 0 and np[1] < b \
                        and heights[point[0]][point[1]] < heights[np[0]][np[1]]:
                        accessible.add(np)
                        new_points.append(np)
                    # else:
                    #     inaccessible.add(np)
            if new_points:
                dfs(new_points, accessible, inaccessible)
        dfs(list(self.pacific), self.pacific, self.no_pacific)
        print()
        dfs(list(self.atlantic), self.atlantic, self.no_atlantic)
        return [list(point) for point in self.pacific.intersection(self.atlantic)]