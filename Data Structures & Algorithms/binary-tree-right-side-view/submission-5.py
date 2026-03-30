# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        from collections import deque
        q = deque()
        q.append(root)
        res = []
        while q:
            res.append(q[-1].val)
            l = len(q)
            while l > 0:
                temp = q.popleft()
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
                l -= 1
        return res