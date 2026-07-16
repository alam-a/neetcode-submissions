class Graph:
    
    def __init__(self):
        self.mem = defaultdict(set)

    def addEdge(self, src: int, dst: int) -> None:
        self.mem[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if dst in self.mem[src]:
            self.mem[src].remove(dst)
            return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        def dfs(src: int) -> bool:
            if src == dst:
                return True
            visited.add(src)
            for neighbor in self.mem[src]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            return False
        return dfs(src)    
