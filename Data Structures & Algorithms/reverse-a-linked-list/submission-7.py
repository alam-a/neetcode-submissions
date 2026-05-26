# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nhead = None
        while head:
            temp, head = head, head.next
            nhead, temp.next = temp, nhead
        return nhead