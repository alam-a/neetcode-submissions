# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, minimum, maximum):
            if not node:
                return True
            if not (node.val < maximum and node.val > minimum):
                return False            
            if not validate(node.left, minimum, node.val):
                return False
            if not validate(node.right, node.val, maximum):
                return False
            return True
        return validate(root, float("-inf"), float("inf")) 
            
        