# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s, f = head, head
        while f and f.next:
            s, f = s.next, f.next.next
        h, s.next, nh = s.next, None, None
        while h:
            temp, h = h, h.next
            temp.next, nh = nh, temp
        
        s = head
        while nh:
            s.next, nh.next, temp = nh, s.next, nh.next
            nh, s = temp, s.next.next