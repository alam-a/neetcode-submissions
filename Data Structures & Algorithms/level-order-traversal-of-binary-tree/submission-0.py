# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.traversal = []
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def traverse(root, depth):
            if not root:
                return
            if len(self.traversal) < depth:
                self.traversal.append([])
            self.traversal[depth-1].append(root.val)
            traverse(root.left, depth+1)
            traverse(root.right, depth+1)
        traverse(root, 1)
        return self.traversal            