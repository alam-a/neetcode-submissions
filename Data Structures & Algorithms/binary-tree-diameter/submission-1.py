# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.res = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def compute(root):
            if root:
                l = compute(root.left)
                r = compute(root.right)
                self.res = max(self.res, l + r)
                return max(l, r) + 1
            return 0
        compute(root)
        return self.res
