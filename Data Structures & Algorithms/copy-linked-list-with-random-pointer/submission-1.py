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
        ch = {} #copy helper
        h = head
        while h:
            ch[h] = Node(h.val)
            h = h.next

        for o, n in ch.items():
            if o.next:
                n.next = ch[o.next]
            if o.random:
                n.random = ch[o.random]
        return ch.get(head, None)
