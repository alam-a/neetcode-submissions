# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        #find node after which we need to do reverse
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        node = slow.next
        #break the connection post pivot
        slow.next = None
        
        #reverse post pivot
        new_head = None
        while node:
            temp = node.next
            node.next = new_head
            new_head = node
            node = temp
        
        #reorder
        while head.next and new_head:
            temp = new_head.next
            new_head.next, head.next = head.next, new_head
            head = head.next.next
            new_head = temp
        
