# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compare(root, subRoot):
            if root is None and subRoot is None:
                return True
            elif root is not None and subRoot is not None:
                if root.val == subRoot.val:
                    return compare(root.left, subRoot.left) and compare(root.right, subRoot.right)
                else:
                    return False
            else:
                return False
    
        if not root:
            return False
        is_same = False
        if root.val == subRoot.val:
            is_same = compare(root, subRoot)
        return is_same or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

