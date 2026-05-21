# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        from collections import deque
        d = deque()
        d.append(root)

        while d:
            l = None
            for _ in range(len(d)):
                l = d.popleft()
                if l:
                    d.append(l.left)
                    d.append(l.right)
            if l:
                res.append(l.val)
        return res