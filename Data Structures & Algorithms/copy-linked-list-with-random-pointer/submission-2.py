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
        node_map = {}
        temp = head
        while temp:
            node_map[temp.val] = Node(temp.val)
            temp = temp.next
        
        new_head = node_map[head.val]
        temp = head
        while temp:
            if temp.next:
                node_map[temp.val].next = node_map[temp.next.val]
            if temp.random:
                node_map[temp.val].random = node_map[temp.random.val]
            temp = temp.next
        return new_head