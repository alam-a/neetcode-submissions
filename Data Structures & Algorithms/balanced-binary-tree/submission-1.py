# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0
            lh = dfs(root.left)
            rh = dfs(root.right)
            if lh == -1 or rh == -1 or abs(lh - rh) > 1:
                return -1
            return max(lh, rh) + 1
        if dfs(root) == -1:
            return False
        return True
