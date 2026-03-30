# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        f, s = head.next, head
        while f and f.next:
            f = f.next.next
            s = s.next
        
        prev, new = None, s
        # s.next = None
        while new:
            temp = new.next
            new.next = prev
            prev = new
            new = temp

        f, s = head, prev
        while f and s:
            temp = f.next
            f.next = s
            s = s.next
            f.next.next = temp
            f = temp
        