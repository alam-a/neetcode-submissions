class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = [[] for _ in range(n)]
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        def dfs(curr: int) -> None:
            if curr not in visited:
                visited.add(curr)
                for v in adj[curr]:
                    dfs(v)
        res = 0
        for v in range(n):
            if v not in visited:
                res += 1
                dfs(v)
        return res