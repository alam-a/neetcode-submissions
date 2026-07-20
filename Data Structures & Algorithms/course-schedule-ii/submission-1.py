class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = {v: 0 for v in range(numCourses)}
        q = deque()
        res = []
        adj = [[] for _ in range(numCourses)]
        for c, p in prerequisites:
            adj[p].append(c)
            indegree[c] += 1
        
        for v in indegree:
            if indegree[v] == 0:
                q.append(v)
                res.append(v)
            
        while q:
            for _ in range(len(q)):
                v = q.popleft()
                for nv in adj[v]:
                    indegree[nv] -= 1
                    if not indegree[nv]:
                        q.append(nv)
                        res.append(nv)
        return res if len(res) == numCourses else []