# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def min_max(l1, l2):
            if not l1 and not l2:
                return l1, l2
            if not l1:
                return l2, l1
            elif not l2:
                return l1, l2
            elif l1.val < l2.val:
                return l1, l2
            else:
                return l2, l1

        list1, list2 = min_max(list1, list2)
        if not list1:
            return list1
        nl = list1
        head = nl
        list1 = list1.next

        while True:
            list1, list2 = min_max(list1, list2)
            if not list1:
                break
            nl.next = list1
            list1, nl = list1.next, nl.next
                
        return head
            
