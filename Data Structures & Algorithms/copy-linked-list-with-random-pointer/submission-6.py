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
        ref = {}
        temp = head
        while temp:
            ref[temp] = Node(temp.val)
            temp = temp.next
        
        temp = head
        while temp:
            ref[temp].next = ref.get(temp.next)
            ref[temp].random = ref.get(temp.random)
            temp = temp.next
        
        return ref.get(head)
