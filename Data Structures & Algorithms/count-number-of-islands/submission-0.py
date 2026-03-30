class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cds = set([(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == "1"])
        def traverse_island(c):
            i, j = c[0], c[1]
            if i >= len(grid) or j >= len(grid[0]):
                return False
            if (i, j+1) in cds:
                cds.remove((i, j+1))
                traverse_island((i, j+1))
            if (i+1, j) in cds:
                cds.remove((i+1, j))
                traverse_island((i+1, j))
            if (i, j-1) in cds:
                cds.remove((i, j-1))
                traverse_island((i, j-1))
            if (i-1, j) in cds:
                cds.remove((i-1, j))
                traverse_island((i-1, j))
            
        counter = 0
        while cds:
            cd = list(cds)[0]
            cds.remove(cd)
            counter+=1
            print(f"iteration: {counter}")
            traverse_island(cd)

        return counter