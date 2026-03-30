# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            p, q = q, p
        
        while root:
            print(root.val, p.val, q.val)
            if root.val == p.val or root.val == q.val:
                return root
            elif root.val > p.val and root.val < q.val:
                return root
            elif root.val > q.val:
                root = root.left
            else:
                root = root.right
        