# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        h, l = head, 0
        while h:
            l+=1
            h=h.next
        
        if l == n:
            return head.next

        h = head
        while l > n+1:
            h = h.next
            l -= 1
        h.next = h.next.next
        return head