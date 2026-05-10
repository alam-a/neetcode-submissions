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
        ldict = {}
        t_head = head
        while t_head:
            ldict[t_head] = Node(t_head.val)
            t_head = t_head.next
        t_head = head
        while t_head:
            if t_head.next:
                ldict[t_head].next = ldict[t_head.next]
            if t_head.random:
                ldict[t_head].random = ldict[t_head.random]
            t_head = t_head.next
        return ldict.get(head)
