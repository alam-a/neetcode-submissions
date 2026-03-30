class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [set() for i in range(n)]
        for e in edges:
            if e[0] != e[1]:
                adj[e[0]].add(e[1])
                adj[e[1]].add(e[0])
            else:
                return False
        print(adj)
        
        once = set()
        visited = set()
        def dfs(v):
            once.add(v)
            visited.add(v)
            for e in adj[v]:
                adj[e].remove(v)
                if visited.intersection(adj[e]) or not dfs(e):
                    return False
                adj[e].add(v)
            visited.remove(v)
            return True
        
        print(adj)
        res = dfs(0)
        print(visited)
        print(once)
        if len(once) != n or not res:
            return False
        return True

        