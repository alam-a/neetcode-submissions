# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_val = float("-inf")
        def dfs(root):
            if not root:
                return float("-inf")
            l = dfs(root.left)
            r = dfs(root.right)
            print(root.val, l, r, l+root.val, r+root.val, root.val, l+r+root.val)
            res = max(l+root.val, r+root.val, root.val)
            self.max_val = max(self.max_val, l, r, res, l+r+root.val)
            return res
        dfs(root)
        return self.max_val