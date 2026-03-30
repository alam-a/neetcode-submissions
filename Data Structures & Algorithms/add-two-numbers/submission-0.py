# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def s_and_c(a, b=0, c=0):
            if a + b + c >= 10:
                return (a + b + c) % 10, (a + b + c) // 10
            return a + b + c, 0
        s, c = s_and_c(l1.val, l2.val)
        h = t = ListNode(s)
        l1, l2 = l1.next, l2.next
        while l1 and l2:
            s, c = s_and_c(l1.val, l2.val, c)
            t.next = ListNode(s)
            l1, l2, t = l1.next, l2.next, t.next
        if l1 is None:
            l1 = l2
        while l1:
            s, c = s_and_c(l1.val, c)
            t.next = ListNode(s)
            l1, t = l1.next, t.next
        while c:
            s, c = s_and_c(c, 0)
            t.next = ListNode(s)
        return h
