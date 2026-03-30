# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        f, s = head, head
        while f and f.next:
            f = f.next.next
            s = s.next
        
        prev = s.next
        new_head = None
        s.next = None
        while prev:
            temp = prev.next
            prev.next = new_head
            new_head = prev
            prev = temp
        t = new_head
        while t:
            print(t.val)
            t = t.next
        print()
        t = head
        while t:
            print(t.val)
            t = t.next
        
        while new_head and head:
            print(head.val, new_head.val)
            t1, t2 = head.next, new_head.next
            new_head.next = t1
            head.next = new_head
            head, new_head = t1, t2
        