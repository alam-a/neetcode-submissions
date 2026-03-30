from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # stores where can one go after taking a course
        adj = [[] for _ in range(numCourses)]

        # stores all the courses at the start, and then courses who 
        # have a dependency are removed
        rem = set(range(numCourses))
        for i in range(len(prerequisites)):
            adj[prerequisites[i][1]].append(prerequisites[i][0])
            if prerequisites[i][0] in rem:
                rem.remove(prerequisites[i][0])
        if len(rem) == 0:
            return False


        path = set()
        def dfs(v):

            #if previously seen in path, there is a cyclic dependency
            if v in path:
                return False

            # add current vertex to path, and later remove it for backtracking
            path.add(v)

            # recursively check courses which can be taken after this
            # and return False if a cycle is detected
            for n in adj[v]:
                if not dfs(n):
                    return False
            path.remove(v)
            return True # if no cycle detected

        # start iterating from courses for which there are no prerequisites
        for v in list(rem)+list(set(range(numCourses))-rem):
            if not dfs(v):
                return False
        return True
        
