class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        movements = ((0, 1), (0, -1), (1, 0), (-1, 0))
        curr_pass, num_passes = [], 0
        good_fruits = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    curr_pass.append((i, j))
                elif grid[i][j] == 1:
                    good_fruits += 1

        while curr_pass:
            next_pass = set()
            for i, j in list(curr_pass):
                for mi, mj in movements:
                    ni, nj = mi + i, mj + j
                    if ni >= R or ni < 0 or nj >= C or nj < 0:
                        continue
                    if grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        good_fruits -= 1
                        next_pass.add((ni, nj))
            if next_pass:
                curr_pass = next_pass
                num_passes += 1
            else:
                break
                
        if good_fruits:
            return -1
        return num_passes
