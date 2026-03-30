# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root, subRoot):
            if not root and not subRoot:
                return True
            elif root and subRoot and root.val == subRoot.val:
                return dfs(root.left, subRoot.left) and dfs(root.right, subRoot.right)
            else:
                return False

        if not root and not subRoot:
            return True
        elif root and subRoot and root.val == subRoot.val:
            print(root.val, subRoot.val)
            if dfs(root, subRoot):
                return True
        if root:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return False