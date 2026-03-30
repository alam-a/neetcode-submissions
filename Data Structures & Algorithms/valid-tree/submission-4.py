class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        adj = [set() for _ in range(n)]
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
        
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for nn in adj[node]: #next node
                if nn == parent:
                    continue
                if not dfs(nn, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n