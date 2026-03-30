# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        f, s = head.next, head
        while f and f.next:
            if f == s:
                return True
            f, s = f.next.next, s.next
        return False