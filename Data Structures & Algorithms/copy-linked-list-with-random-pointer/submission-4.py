"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        node_map = {}
        temp = head
        while temp:
            node_map[temp] = Node(temp.val)
            temp = temp.next
        
        new_head = node_map[head]
        temp = head
        while temp:
            if temp.next:
                node_map[temp].next = node_map[temp.next]
            if temp.random:
                node_map[temp].random = node_map[temp.random]
            temp = temp.next
        return new_head