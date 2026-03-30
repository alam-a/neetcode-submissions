# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recursion(new, old):
            if not old:
                return new
            temp = old
            old = old.next
            temp.next = new
            return recursion(temp, old)
        return recursion(None, head)
        
        #working version using iteration
        h, nh = head, None

        while h:
            temp = nh
            nh = h
            h = h.next
            nh.next = temp
        
        return nh
        
        
        #working version using iteration
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
        