# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_val = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return float("-inf")
            l = dfs(root.left)
            r = dfs(root.right)
            return max(l, r, l+root.val, r+root.val, root.val, l+r+root.val)
        return dfs(root)