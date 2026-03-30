# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        parent = root

        def invert(parent: Optional[TreeNode]):
            if not parent:
                return
            left = parent.left
            parent.left = parent.right
            parent.right = left
            invert(parent.left)
            invert(parent.right)
        invert(root)
        return parent

