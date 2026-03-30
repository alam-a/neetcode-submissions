# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def dfs(self, root, subRoot):
        if not root and not subRoot:
            return True
        elif root and subRoot:
            if root.val == subRoot.val:
                left = self.dfs(root.left, subRoot.left)
                right = self.dfs(root.right, subRoot.right)
                return left and right
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:        
        if not root and not subRoot:
            return True
        elif root and subRoot and root.val == subRoot.val and self.dfs(root, subRoot):
            return True
        if root:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return False