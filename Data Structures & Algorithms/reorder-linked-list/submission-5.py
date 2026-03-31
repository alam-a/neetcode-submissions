# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s, f = head, head
        while f.next and f.next.next:
            f = f.next.next
            s = s.next
        
        curr, prev = None, s.next
        s.next = None
        while prev:
            prev.next, curr, prev  = curr, prev, prev.next

        while curr:
            head.next, curr.next, head, curr = curr, head.next, head.next, curr.next