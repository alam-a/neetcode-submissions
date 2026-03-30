# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.depth = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def calculate(root, depth):
            if not root:
                return
            depth+=1
            self.depth = max(depth, self.depth)
            calculate(root.left, depth)
            calculate(root.right, depth)
        calculate(root, 0)
        return self.depth            