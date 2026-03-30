# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.res = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            l = self.maxDepth(root.left)
            r = self.maxDepth(root.right)
            return max(l, r) + 1
        return 0
        
        """
        #diameter code, should have spent more time reading the question
        if not root:
            return 0
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        n = l+r+1
        self.res = max(self.res, n)
        return n
        """