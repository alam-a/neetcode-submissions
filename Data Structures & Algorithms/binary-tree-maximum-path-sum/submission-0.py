# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_val = 0

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            else:
                l = dfs(root.left)
                r = dfs(root.right)
                max_val = max(l, r, l + root.val, r + root.val, l + r + root.val)
                print(root.val, l, r, max_val)
                self.max_val = max(self.max_val, max_val)
                return max_val
        dfs(root)
        return self.max_val
