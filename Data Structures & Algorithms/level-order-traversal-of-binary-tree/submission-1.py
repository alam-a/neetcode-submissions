# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        from collections import deque
        d = deque()
        d.append(root)
        res = []
        while d:
            t = []
            for _ in range(len(d)):
                node = d.popleft()
                t.append(node.val)
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
            res.append(t)
        return res