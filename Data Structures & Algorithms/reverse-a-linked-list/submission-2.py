# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h, nh = head, None

        while h:
            temp = nh
            nh = h
            h = h.next
            nh.next = temp
        
        return nh
        
        
        if not head:
            return head

        h, nh = head, None
        while h and h.next:
            o = h
            h = h.next
            o.next = nh
            nh = o
        h.next = nh
        return h
        