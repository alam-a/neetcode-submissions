from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)] #stores where can one go after taking a course
        rem = set(range(numCourses))
        for i in range(len(prerequisites)):
            adj[prerequisites[i][1]].append(prerequisites[i][0])
            if prerequisites[i][0] in rem:
                rem.remove(prerequisites[i][0])
        print(adj)
        print(rem)
        if len(rem) == 0:
            return False
        # return True

        path = set()
        visited = set()
        def dfs(v):
            if v in path:
                return False
            path.add(v)
            for n in adj[v]:
                if not dfs(n):
                    return False
            path.remove(v)
            return True
        print(list(rem)+list(range(numCourses)))
        for v in list(rem)+list(range(numCourses)):
            print(v)
            if not dfs(v):
                return False
        return True
        
