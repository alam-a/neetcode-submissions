# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next or not head.next.next:
            return

        ntm = [] #nodes to move
        f, s = head, head
        c = 0
        while f and f.next:
            f = f.next.next
            s = s.next
            
        #start gathering nodes after middle
        while s:
            t = s.next
            s.next = None
            if t:
                ntm.append(t)
            s = t

        s = head
        for n in ntm[::-1]:
            n.next = s.next
            s.next = n
            s = s.next.next
        
        return

