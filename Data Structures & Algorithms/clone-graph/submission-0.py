"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.visited = {}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        elif node.val in self.visited:
            return self.visited[node.val]
        
        clone = Node(node.val)
        self.visited[node.val] = clone
        
        neighbors = [self.cloneGraph(n) for n in node.neighbors]
        clone.neighbors = neighbors
        return clone