# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_number, carry = l1, 0
        last = None
        while l1 or l2:
            if l1 and not l1.next and l2 and l2.next:
                l1.next = l2.next
                l2.next = None
            
            last = l1
            if not l2:
                n = l1.val + carry
                l1.val = n % 10
                carry = n // 10
                l1 = l1.next
            elif l1 and l2:
                n = (l1.val + l2.val + carry)
                l1.val = n % 10
                carry = n // 10
                l1 = l1.next
                l2 = l2.next
        if carry:
            last.next = ListNode(val=carry)
        return new_number