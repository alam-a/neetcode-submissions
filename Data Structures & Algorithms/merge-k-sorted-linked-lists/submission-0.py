# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = merged = ListNode()
        length = len(lists)
        i = 0
        # while i < length:
        #     if not lists[i]:
        #         lists[length-1], lists[i] = lists[i], lists[length-1]
        #         length -= 1

        if len(lists) == 0:# or len(lists[0]) == 0:
            return None
        
        i = 0
        while length > 0:
            m, j = ListNode(float("inf")), 0
            for i in range(length):
                if m.val >= lists[i].val:
                    m = lists[i]
                    j = i
            print(m.val)
            if not m.next:
                merged.next = m
                lists[j], lists[length-1] = lists[length-1], lists[j]
                length -= 1
            else:
                lists[j] = m.next
                merged.next = m
                merged.next.next = None
            merged = merged.next
        
        return head.next
            

