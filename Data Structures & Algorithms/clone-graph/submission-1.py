"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.head = []
        self.nodes = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        if node not in self.nodes:
            head = Node(node.val)
            self.nodes[node.val] = head
            for neighbor in node.neighbors:
                if neighbor.val not in self.nodes:
                    self.cloneGraph(neighbor)
                head.neighbors.append(self.nodes[neighbor.val])
        return self.nodes[node.val]