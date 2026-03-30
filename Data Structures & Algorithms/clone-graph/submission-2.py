"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.res = {}
        def dfs(node):
            if not node:
                return None
            temp = Node(node.val)
            self.res[node.val] = temp
            for neighbor in node.neighbors:
                if neighbor.val in self.res:
                    temp.neighbors.append(self.res[neighbor.val])
                else:
                    temp.neighbors.append(dfs(neighbor))
            return temp
        return dfs(node)