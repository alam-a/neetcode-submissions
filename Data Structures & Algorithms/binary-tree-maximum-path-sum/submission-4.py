# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float("-inf")
        def dfs(node):
            if not node:
                return float("-inf")
            l = dfs(node.left)
            r = dfs(node.right)
            result = max(l+node.val, r+node.val, node.val)
            self.res = max(self.res, result, l, r, l+r+node.val)
            return result
        dfs(root)
        return self.res