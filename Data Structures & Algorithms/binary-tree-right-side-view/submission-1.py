# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        sol = []
        if not root:
            return sol
        from collections import deque
        curr = deque()
        curr.append(root)
        while curr:
            sol.append(curr[-1].val)
            n = deque()
            while curr:
                t = curr.popleft()
                if t.left:
                    n.append(t.left)
                if t.right:
                    n.append(t.right)
            curr = n
        return sol
