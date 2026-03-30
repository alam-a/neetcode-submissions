# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(l, r, node):
            if not node:
                return True
            if not (node.val > l and node.val < r):
                return False
            return validate(l, node.val, node.left) and validate(node.val, r, node.right)
        return validate(float("-inf"), float("inf"), root)
