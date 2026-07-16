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
        if src not in self.mem:
            return False
        if dst in self.mem[src]:
            return True
        for v in self.mem[src]:
            if self.hasPath(v, dst):
                return True
        return False
    
