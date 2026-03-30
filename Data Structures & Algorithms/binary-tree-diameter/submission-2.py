# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root or ((not root.left) and (not root.right)):
                return 0
            left = dfs(root.left) + 1 if root.left else 0
            right = dfs(root.right) + 1 if root.right else 0 
            curr = left + right
            self.diameter = max(self.diameter, curr)
            return max(left, right)
        dfs(root)
        return self.diameter

        