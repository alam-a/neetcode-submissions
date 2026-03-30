from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # will store prerequisite map
        pm = {i: [] for i in range(numCourses)}

        for c, p in prerequisites:
            pm[c].append(p)
        
        visited = set()
        def dfs(c):
            if c in visited: #already visited, cycle detected
                return False

            if not pm[c]: # no prerequisites
                return True
            
            visited.add(c)
            for i in pm[c]:
                if not dfs(i):
                    return False
                pm[i] = []
            visited.remove(c)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
            
            